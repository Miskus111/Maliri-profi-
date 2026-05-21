#!/usr/bin/env python3
"""
Rebuilds the Malíři Profi website as plain HTML/CSS/JS (no Next.js / React runtime).
Output: /tmp/plain_build/ directory + /tmp/maliriprofi-static.zip
"""

import os, re, shutil, zipfile
from bs4 import BeautifulSoup, Comment, NavigableString

# ── Paths ──────────────────────────────────────────────────────────────────
REPO       = "/home/user/Maliri-profi-"
OUT_DIR    = os.path.join(REPO, "out")
BUILD_DIR  = "/tmp/plain_build"
ZIP_PATH   = "/tmp/maliriprofi-static.zip"
ASSETS_DIR = os.path.join(BUILD_DIR, "assets")
IMAGES_DIR = os.path.join(BUILD_DIR, "images")

# ── Clean slate ────────────────────────────────────────────────────────────
shutil.rmtree(BUILD_DIR, ignore_errors=True)
os.makedirs(ASSETS_DIR)
os.makedirs(IMAGES_DIR)

# ── Copy images ────────────────────────────────────────────────────────────
src_images = os.path.join(OUT_DIR, "images")
for f in os.listdir(src_images):
    shutil.copy2(os.path.join(src_images, f), os.path.join(IMAGES_DIR, f))
print(f"Copied {len(os.listdir(IMAGES_DIR))} images")

# ── Copy GSAP files ────────────────────────────────────────────────────────
gsap_src = os.path.join(REPO, "node_modules/gsap/dist")
shutil.copy2(os.path.join(gsap_src, "gsap.min.js"),
             os.path.join(ASSETS_DIR, "gsap.min.js"))
shutil.copy2(os.path.join(gsap_src, "ScrollTrigger.min.js"),
             os.path.join(ASSETS_DIR, "ScrollTrigger.min.js"))
print("Copied GSAP files")

# ── Copy compiled Tailwind CSS ─────────────────────────────────────────────
css_dir = os.path.join(OUT_DIR, "_next/static/css")
css_files = os.listdir(css_dir)
if css_files:
    shutil.copy2(os.path.join(css_dir, css_files[0]),
                 os.path.join(ASSETS_DIR, "style.css"))
    print(f"Copied CSS: {css_files[0]}")

# ── Parse pre-rendered HTML ────────────────────────────────────────────────
with open(os.path.join(OUT_DIR, "index.html"), "r", encoding="utf-8") as f:
    raw_html = f.read()

soup = BeautifulSoup(raw_html, "html.parser")

# ── Extract head meta info ─────────────────────────────────────────────────
head = soup.head
title_tag   = head.find("title")
title_text  = title_tag.string if title_tag else "Malíři Profi Praha"
desc_meta   = head.find("meta", attrs={"name": "description"})
author_meta = head.find("meta", attrs={"name": "author"})
kw_meta     = head.find("meta", attrs={"name": "keywords"})
robots_meta = head.find("meta", attrs={"name": "robots"})
og_title    = head.find("meta", attrs={"property": "og:title"})
og_desc     = head.find("meta", attrs={"property": "og:description"})
og_locale   = head.find("meta", attrs={"property": "og:locale"})
og_type     = head.find("meta", attrs={"property": "og:type"})
tw_card     = head.find("meta", attrs={"name": "twitter:card"})

def attr(tag, key, default=""):
    return tag[key] if tag and tag.get(key) else default

# ── Extract body content (nav + main + footer + FloatingCTA) ──────────────
body         = soup.body
content_div  = list(body.children)[1]   # <div class="relative"> wrapper
nav_tag      = content_div.find("nav")
main_tag     = content_div.find("main")
footer_tag   = content_div.find("footer")
floating_divs = [c for c in content_div.children
                 if hasattr(c, "name") and c.name in ("div", "a")
                 and "fixed" in " ".join(c.get("class", []))]

# ── Fix /images/ paths in HTML strings ────────────────────────────────────
def fix_paths(tag):
    """Replace /images/ with ./images/ in src attributes."""
    for img in tag.find_all("img"):
        src = img.get("src", "")
        if src.startswith("/images/"):
            img["src"] = "." + src
    for a in tag.find_all("a"):
        href = a.get("href", "")
        if href.startswith("/images/"):
            a["href"] = "." + href

for t in [nav_tag, main_tag, footer_tag] + floating_divs:
    if t:
        fix_paths(t)

# ── Remove React event attributes (they'll do nothing anyway) ─────────────
# Keep onclick on anchor/button since we'll override via JS

# ── Serialize sections ─────────────────────────────────────────────────────
nav_html      = str(nav_tag)
main_html     = str(main_tag)
footer_html   = str(footer_tag)
floating_html = "\n".join(str(d) for d in floating_divs)

# ── Mobile menu HTML (React state = never pre-rendered) ───────────────────
mobile_menu_html = """
<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 z-40 lg:hidden hidden">
  <div id="mobile-backdrop" class="absolute inset-0 bg-black/20 backdrop-blur-sm"></div>
  <div class="absolute top-16 left-0 right-0 bg-[#F6F5F1]/95 backdrop-blur-xl border-b border-[#E3E1DC]/60 p-6 flex flex-col gap-1">
    <a href="#services" class="nav-link font-body text-[15px] text-[#111111] py-3 px-2 hover:text-[#5F6F65] transition-colors">Služby</a>
    <a href="#process"  class="nav-link font-body text-[15px] text-[#111111] py-3 px-2 hover:text-[#5F6F65] transition-colors">Proces</a>
    <a href="#gallery"  class="nav-link font-body text-[15px] text-[#111111] py-3 px-2 hover:text-[#5F6F65] transition-colors">Realizace</a>
    <a href="#pricing"  class="nav-link font-body text-[15px] text-[#111111] py-3 px-2 hover:text-[#5F6F65] transition-colors">Ceník</a>
    <a href="#contact"  class="nav-link font-body text-[15px] text-[#111111] py-3 px-2 hover:text-[#5F6F65] transition-colors">Kontakt</a>
    <a href="tel:+420737171208" class="mt-3 font-body font-medium text-[13px] bg-[#5F6F65] text-white px-5 py-3 rounded-full text-center">
      Zavolat: +420 737 171 208
    </a>
  </div>
</div>
"""

# ── Gallery lightbox HTML (React state = never pre-rendered) ───────────────
lightbox_html = """
<!-- Gallery Lightbox -->
<div id="lightbox" class="fixed inset-0 z-50 bg-black/95 items-center justify-center hidden">
  <button id="lb-close" class="absolute top-5 right-5 text-white/60 hover:text-white z-10">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
  </button>
  <button id="lb-prev" class="absolute left-4 top-1/2 -translate-y-1/2 text-white/40 hover:text-white z-10 hidden sm:block">
    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <button id="lb-next" class="absolute right-4 top-1/2 -translate-y-1/2 text-white/40 hover:text-white z-10 hidden sm:block">
    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
  </button>
  <div id="lb-content" class="max-w-[90vw] max-h-[88vh]">
    <img id="lb-img" src="" alt="" class="max-w-full max-h-[88vh] object-contain rounded-sm"/>
  </div>
</div>
"""

# ── Write main.js ──────────────────────────────────────────────────────────
main_js = r"""
// ── Smooth scroll helpers ──────────────────────────────────────────────────
function smoothScroll(selector) {
  var el = document.querySelector(selector);
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

// Intercept all anchor links that start with # for smooth scroll
document.addEventListener('click', function(e) {
  var a = e.target.closest('a[href^="#"]');
  if (!a) return;
  var href = a.getAttribute('href');
  if (href === '#') {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    return;
  }
  e.preventDefault();
  closeMobileMenu();
  smoothScroll(href);
});

// ── Navigation scroll behaviour ────────────────────────────────────────────
var nav = document.querySelector('nav');
var lastScrollY = 0;

window.addEventListener('scroll', function() {
  var y = window.scrollY;
  // hide/show
  if (y > lastScrollY && y > 200) {
    nav.style.transform = 'translateY(-100%)';
  } else {
    nav.style.transform = 'translateY(0)';
  }
  // background
  if (y > 80) {
    nav.style.backgroundColor = 'rgba(246,245,241,0.9)';
    nav.style.backdropFilter   = 'blur(20px)';
    nav.style.webkitBackdropFilter = 'blur(20px)';
    nav.style.boxShadow        = '0 1px 0 rgba(0,0,0,0.04)';
  } else {
    nav.style.backgroundColor = 'transparent';
    nav.style.backdropFilter   = '';
    nav.style.webkitBackdropFilter = '';
    nav.style.boxShadow        = '';
  }
  lastScrollY = y;
}, { passive: true });

// ── Mobile menu ────────────────────────────────────────────────────────────
var mobileMenu    = document.getElementById('mobile-menu');
var mobileBackdrop= document.getElementById('mobile-backdrop');
var menuBtn       = document.querySelector('button.lg\\:hidden');

function openMobileMenu() {
  mobileMenu.classList.remove('hidden');
  mobileMenu.classList.add('flex');
}
function closeMobileMenu() {
  mobileMenu.classList.add('hidden');
  mobileMenu.classList.remove('flex');
}
if (menuBtn) {
  menuBtn.addEventListener('click', function() {
    if (mobileMenu.classList.contains('hidden')) {
      openMobileMenu();
    } else {
      closeMobileMenu();
    }
  });
}
if (mobileBackdrop) {
  mobileBackdrop.addEventListener('click', closeMobileMenu);
}

// ── GSAP Animations ────────────────────────────────────────────────────────
gsap.registerPlugin(ScrollTrigger);

// Hero fade-in
(function() {
  var heroContent = document.querySelector('#hero .max-w-\\[640px\\]');
  if (!heroContent) return;
  var els = Array.from(heroContent.children);
  gsap.fromTo(els,
    { opacity: 0, y: 30 },
    { opacity: 1, y: 0, duration: 0.9, stagger: 0.12, ease: 'power3.out', delay: 0.3 }
  );
})();

// Services cards
(function() {
  var section = document.getElementById('services');
  if (!section) return;
  gsap.fromTo(section.querySelectorAll('.service-card'),
    { opacity: 0, y: 50 },
    {
      opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: 'power3.out',
      scrollTrigger: { trigger: section, start: 'top 78%' }
    }
  );
})();

// Process steps
(function() {
  var section = document.getElementById('process');
  if (!section) return;
  gsap.fromTo(section.querySelectorAll('.process-step'),
    { opacity: 0, x: -40 },
    {
      opacity: 1, x: 0, duration: 0.7, stagger: 0.08, ease: 'power3.out',
      scrollTrigger: { trigger: section, start: 'top 75%' }
    }
  );
})();

// Gallery grid
(function() {
  var grid = document.querySelector('#gallery .columns-2');
  if (!grid) return;
  gsap.fromTo(Array.from(grid.children),
    { opacity: 0, y: 30, scale: 0.97 },
    {
      opacity: 1, y: 0, scale: 1, duration: 0.7, stagger: 0.06, ease: 'power3.out',
      scrollTrigger: { trigger: grid, start: 'top 80%' }
    }
  );
})();

// References cards
(function() {
  var section = document.getElementById('references');
  if (!section) return;
  gsap.fromTo(section.querySelectorAll('.ref-card'),
    { opacity: 0, x: 40 },
    {
      opacity: 1, x: 0, duration: 0.8, stagger: 0.08, ease: 'power3.out',
      scrollTrigger: { trigger: section, start: 'top 75%' }
    }
  );
})();

// Pricing cards
(function() {
  var section = document.getElementById('pricing');
  if (!section) return;
  gsap.fromTo(section.querySelectorAll('.price-card'),
    { opacity: 0, y: 40 },
    {
      opacity: 1, y: 0, duration: 0.7, stagger: 0.09, ease: 'power3.out',
      scrollTrigger: { trigger: section, start: 'top 78%' }
    }
  );
})();

// FAQ items
(function() {
  var section = document.getElementById('faq');
  if (!section) return;
  gsap.fromTo(section.querySelectorAll('.faq-item'),
    { opacity: 0, y: 20 },
    {
      opacity: 1, y: 0, duration: 0.6, stagger: 0.05, ease: 'power3.out',
      scrollTrigger: { trigger: section, start: 'top 80%' }
    }
  );
})();

// Contact elements
(function() {
  var section = document.getElementById('contact');
  if (!section) return;
  gsap.fromTo(section.querySelectorAll('.contact-el'),
    { opacity: 0, y: 30 },
    {
      opacity: 1, y: 0, duration: 0.7, stagger: 0.08, ease: 'power3.out',
      scrollTrigger: { trigger: section, start: 'top 78%' }
    }
  );
})();

// ── FAQ Accordion ──────────────────────────────────────────────────────────
(function() {
  var items = document.querySelectorAll('.faq-item');
  items.forEach(function(item) {
    var btn    = item.querySelector('button');
    var panel  = item.querySelector('.faq-answer');
    var icon   = item.querySelector('.faq-icon');
    if (!btn || !panel) return;
    btn.addEventListener('click', function() {
      var isOpen = panel.style.maxHeight && panel.style.maxHeight !== '0px';
      // Close all
      items.forEach(function(it) {
        var p = it.querySelector('.faq-answer');
        var ic = it.querySelector('.faq-icon');
        if (p) { p.style.maxHeight = '0px'; p.style.paddingBottom = '0'; }
        if (ic) {
          ic.style.transform = 'rotate(0deg)';
          ic.style.backgroundColor = 'transparent';
          ic.style.borderColor = '#E3E1DC';
          ic.style.color = '#5F6F65';
        }
      });
      // Open clicked if it was closed
      if (!isOpen) {
        panel.style.maxHeight = panel.scrollHeight + 'px';
        panel.style.paddingBottom = '24px';
        if (icon) {
          icon.style.transform = 'rotate(45deg)';
          icon.style.backgroundColor = '#5F6F65';
          icon.style.borderColor = '#5F6F65';
          icon.style.color = '#ffffff';
        }
      }
    });
  });
})();

// ── References carousel buttons ────────────────────────────────────────────
(function() {
  var scrollEl = document.querySelector('#references .overflow-x-auto');
  var btnLeft  = document.getElementById('ref-prev');
  var btnRight = document.getElementById('ref-next');
  if (!scrollEl) return;
  if (btnLeft)  btnLeft.addEventListener('click',  function() { scrollEl.scrollBy({ left: -460, behavior: 'smooth' }); });
  if (btnRight) btnRight.addEventListener('click', function() { scrollEl.scrollBy({ left:  460, behavior: 'smooth' }); });
})();

// ── Gallery Lightbox ───────────────────────────────────────────────────────
(function() {
  var lightbox  = document.getElementById('lightbox');
  var lbImg     = document.getElementById('lb-img');
  var lbClose   = document.getElementById('lb-close');
  var lbPrev    = document.getElementById('lb-prev');
  var lbNext    = document.getElementById('lb-next');
  var lbContent = document.getElementById('lb-content');
  if (!lightbox) return;

  var images = [];
  var currentIdx = 0;

  // Collect gallery images
  var grid = document.querySelector('#gallery .columns-2');
  if (grid) {
    images = Array.from(grid.querySelectorAll('img')).map(function(img) {
      return img.getAttribute('src');
    });
    // Wire up clicks
    Array.from(grid.children).forEach(function(item, idx) {
      item.addEventListener('click', function() { openLightbox(idx); });
    });
  }

  function openLightbox(idx) {
    currentIdx = idx;
    lbImg.src = images[currentIdx];
    lightbox.classList.remove('hidden');
    lightbox.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() {
    lightbox.classList.add('hidden');
    lightbox.classList.remove('flex');
    document.body.style.overflow = '';
    lbImg.src = '';
  }
  function showPrev() {
    currentIdx = (currentIdx === 0) ? images.length - 1 : currentIdx - 1;
    lbImg.src = images[currentIdx];
  }
  function showNext() {
    currentIdx = (currentIdx === images.length - 1) ? 0 : currentIdx + 1;
    lbImg.src = images[currentIdx];
  }

  lbClose.addEventListener('click', closeLightbox);
  if (lbPrev) lbPrev.addEventListener('click', function(e) { e.stopPropagation(); showPrev(); });
  if (lbNext) lbNext.addEventListener('click', function(e) { e.stopPropagation(); showNext(); });

  // Close on backdrop click (not on image)
  lightbox.addEventListener('click', closeLightbox);
  if (lbContent) lbContent.addEventListener('click', function(e) { e.stopPropagation(); });

  // Keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (lightbox.classList.contains('hidden')) return;
    if (e.key === 'Escape')     closeLightbox();
    if (e.key === 'ArrowLeft')  showPrev();
    if (e.key === 'ArrowRight') showNext();
  });
})();
"""

js_path = os.path.join(ASSETS_DIR, "main.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write(main_js)
print("Wrote main.js")

# ── Post-process: add .faq-answer and .faq-icon classes to FAQ items ───────
# (They are in pre-rendered HTML as overflow-hidden divs — we need to ID them)
# Also add process-step, price-card, contact-el classes where needed.

def post_process_html(html_str):
    """Add vanilla-JS target classes and fix paths."""
    # Fix image paths
    html_str = html_str.replace('src="/images/', 'src="./images/')
    html_str = html_str.replace("src='/images/", "src='./images/")
    html_str = html_str.replace('href="/images/', 'href="./images/')

    # The FAQ answer panel: the overflow-hidden div inside .faq-item
    # BeautifulSoup already handled structural tags; we'll do string-level class injection
    # This is done below separately.
    return html_str

# ── Re-parse for targeted class injection ─────────────────────────────────
# We need to modify: FAQ answer divs → add class "faq-answer"
#                    FAQ icon span   → add class "faq-icon"
#                    Process divs    → add class "process-step"
#                    Pricing cards   → add class "price-card"
#                    Contact els     → add class "contact-el"

# We'll inject a post-processing pass on the main section HTML
def inject_classes(html_str):
    sp = BeautifulSoup(html_str, 'html.parser')

    # FAQ: find faq-item divs, mark answer panel and icon
    for faq_item in sp.select('.faq-item'):
        # the overflow-hidden div is the answer panel
        answer_div = faq_item.find('div', class_=lambda c: c and 'overflow-hidden' in c)
        if answer_div:
            cls = answer_div.get('class', [])
            if 'faq-answer' not in cls:
                cls.append('faq-answer')
                answer_div['class'] = cls
            # Reset inline style to 0 (JS will control it)
            answer_div['style'] = 'max-height:0px; overflow:hidden; transition:max-height 0.4s ease, padding-bottom 0.4s ease;'
        # The icon span (flex-shrink-0 + rounded-full + border)
        icon_span = faq_item.find('span', class_=lambda c: c and 'flex-shrink-0' in c)
        if icon_span:
            cls = icon_span.get('class', [])
            if 'faq-icon' not in cls:
                cls.append('faq-icon')
                icon_span['class'] = cls

    # Process steps: each numbered step div
    process_section = sp.find('section', id='process')
    if process_section:
        # The step items have a numbered circle; look for grid children
        steps_grid = process_section.find('div', class_=lambda c: c and 'grid' in c)
        if steps_grid:
            for child in steps_grid.find_all('div', recursive=False):
                cls = child.get('class', [])
                if 'process-step' not in cls:
                    cls.append('process-step')
                    child['class'] = cls

    # Pricing cards
    pricing_section = sp.find('section', id='pricing')
    if pricing_section:
        for card in pricing_section.select('.group'):
            cls = card.get('class', [])
            if 'price-card' not in cls:
                cls.append('price-card')
                card['class'] = cls

    # Contact elements: direct children of the contact content area
    contact_section = sp.find('section', id='contact')
    if contact_section:
        content_area = contact_section.find('div', class_=lambda c: c and 'grid' in c)
        if content_area:
            for child in content_area.find_all('div', recursive=False):
                cls = child.get('class', [])
                if 'contact-el' not in cls:
                    cls.append('contact-el')
                    child['class'] = cls

    return str(sp)

processed_main = inject_classes(str(main_tag))
# Fix image paths globally in all sections
processed_main = processed_main.replace('src="/images/', 'src="./images/')
nav_html       = nav_html.replace('src="/images/', 'src="./images/')
footer_html    = footer_html.replace('src="/images/', 'src="./images/')
floating_html  = floating_html.replace('src="/images/', 'src="./images/')

# Fix og:image path to relative-safe  (just update references to localhost)
# (og:image doesn't need relative path; keep as-is or remove localhost)

# ── Add References carousel button IDs ────────────────────────────────────
processed_main = processed_main.replace(
    'class="hidden lg:flex gap-2">',
    'class="hidden lg:flex gap-2" id="ref-nav">',
    1
)
# Add IDs to the two carousel buttons
# They appear in the references section heading area
refs_soup = BeautifulSoup(processed_main, 'html.parser')
ref_section = refs_soup.find('section', id='references')
if ref_section:
    nav_div = ref_section.find('div', id='ref-nav')
    if nav_div:
        btns = nav_div.find_all('button')
        if len(btns) >= 2:
            btns[0]['id'] = 'ref-prev'
            btns[1]['id'] = 'ref-next'
processed_main = str(refs_soup.find('main'))

# ── Build the full HTML document ───────────────────────────────────────────
# Google Fonts URL
fonts_url = ("https://fonts.googleapis.com/css2?"
             "family=Playfair+Display:wght@400;500;600&"
             "family=Inter:wght@300;400;500;600&display=swap")

html_doc = f"""<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title_text}</title>
  <meta name="description" content="{attr(desc_meta, 'content')}"/>
  <meta name="author" content="{attr(author_meta, 'content')}"/>
  <meta name="keywords" content="{attr(kw_meta, 'content')}"/>
  <meta name="robots" content="{attr(robots_meta, 'content', 'index, follow')}"/>
  <meta property="og:title" content="{attr(og_title, 'content')}"/>
  <meta property="og:description" content="{attr(og_desc, 'content')}"/>
  <meta property="og:locale" content="{attr(og_locale, 'content', 'cs_CZ')}"/>
  <meta property="og:type" content="{attr(og_type, 'content', 'website')}"/>
  <meta name="twitter:card" content="{attr(tw_card, 'content', 'summary_large_image')}"/>
  <link rel="preload" as="image" href="./images/img-21.jpg"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link href="{fonts_url}" rel="stylesheet"/>
  <link rel="stylesheet" href="./assets/style.css"/>
</head>
<body>
  <div class="relative">
    {nav_html}
    {processed_main}
    {footer_html}
    {floating_html}
  </div>

{mobile_menu_html}
{lightbox_html}

  <script src="./assets/gsap.min.js"></script>
  <script src="./assets/ScrollTrigger.min.js"></script>
  <script src="./assets/main.js"></script>
</body>
</html>
"""

# Write index.html
index_path = os.path.join(BUILD_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_doc)
print(f"Wrote index.html ({len(html_doc)//1024}KB)")

# ── Write 404.html ─────────────────────────────────────────────────────────
page404 = """<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>404 – Stránka nenalezena | Malíři Profi Praha</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="./assets/style.css"/>
</head>
<body class="min-h-screen flex items-center justify-center bg-[#F6F5F1]">
  <div class="text-center px-6">
    <p class="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-6">Chyba 404</p>
    <h1 class="font-display text-[60px] lg:text-[80px] leading-none tracking-tight text-[#111111] mb-6">Stránka<br/>nenalezena</h1>
    <p class="font-body text-[#4A4A4A] mb-10 max-w-md mx-auto">Tato stránka neexistuje nebo byla přesunuta. Vraťte se na hlavní stránku.</p>
    <a href="./index.html" class="font-body font-medium text-[14px] bg-[#5F6F65] text-white px-7 py-3.5 rounded-full hover:bg-[#4A5A50] transition-colors duration-200">
      Zpět na hlavní stránku
    </a>
  </div>
</body>
</html>
"""
with open(os.path.join(BUILD_DIR, "404.html"), "w", encoding="utf-8") as f:
    f.write(page404)
print("Wrote 404.html")

# ── Copy .htaccess ─────────────────────────────────────────────────────────
htaccess = """Options -Indexes
AddDefaultCharset UTF-8

# MIME types
AddType text/css                 .css
AddType application/javascript   .js
AddType image/jpeg               .jpg .jpeg
AddType image/png                .png
AddType image/webp               .webp
AddType image/svg+xml            .svg

# Custom 404
ErrorDocument 404 /404.html

# Compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>

# Cache static assets
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html              "access plus 0 seconds"
  ExpiresByType text/css               "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/jpeg             "access plus 1 month"
  ExpiresByType image/png              "access plus 1 month"
  ExpiresByType image/webp             "access plus 1 month"
</IfModule>
"""
with open(os.path.join(BUILD_DIR, ".htaccess"), "w") as f:
    f.write(htaccess)
print("Wrote .htaccess")

# ── Create ZIP ─────────────────────────────────────────────────────────────
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)

with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(BUILD_DIR):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, BUILD_DIR)
            zf.write(abs_path, rel_path)

print(f"\nZIP created: {ZIP_PATH}")
print(f"ZIP size: {os.path.getsize(ZIP_PATH) // 1024} KB")
print("\nZIP contents:")
with zipfile.ZipFile(ZIP_PATH) as zf:
    names = sorted(zf.namelist())
    for n in names:
        info = zf.getinfo(n)
        print(f"  {n}  ({info.file_size//1024}KB)")
