#!/usr/bin/env python3
"""
Builds the Malíři Profi website as 100% plain HTML/CSS/JS written from scratch.
No Next.js build output used. All content taken directly from source components.
Output: /tmp/scratch_build/ + /tmp/maliriprofi-plain.zip
"""

import os, shutil, zipfile

REPO       = "/home/user/Maliri-profi-"
BUILD_DIR  = "/tmp/scratch_build"
ZIP_PATH   = "/tmp/maliriprofi-plain.zip"

shutil.rmtree(BUILD_DIR, ignore_errors=True)
os.makedirs(f"{BUILD_DIR}/css")
os.makedirs(f"{BUILD_DIR}/js")
os.makedirs(f"{BUILD_DIR}/images")

# ── Copy images ────────────────────────────────────────────────────────────
src_img = f"{REPO}/out/images"
for f in os.listdir(src_img):
    shutil.copy2(f"{src_img}/{f}", f"{BUILD_DIR}/images/{f}")
print(f"Copied {len(os.listdir(src_img))} images")

# ── Copy GSAP ──────────────────────────────────────────────────────────────
gsap = f"{REPO}/node_modules/gsap/dist"
shutil.copy2(f"{gsap}/gsap.min.js",          f"{BUILD_DIR}/js/gsap.min.js")
shutil.copy2(f"{gsap}/ScrollTrigger.min.js", f"{BUILD_DIR}/js/ScrollTrigger.min.js")
print("Copied GSAP")

# ══════════════════════════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════════════════════════
CSS = """
/* ── Reset & base ─────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Inter', system-ui, sans-serif;
  font-weight: 400;
  background: #F6F5F1;
  color: #242424;
  -webkit-font-smoothing: antialiased;
}
img { display: block; max-width: 100%; }
a  { color: inherit; text-decoration: none; }
button { cursor: pointer; border: none; background: none; font: inherit; }

/* ── Typography helpers ────────────────────────────────────────────────── */
.font-display { font-family: 'Playfair Display', Georgia, serif; }
.overline {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: .12em;
  color: #5F6F65;
  font-family: 'Inter', sans-serif;
}

/* ── Layout helpers ───────────────────────────────────────────────────── */
.container { max-width: 1280px; margin: 0 auto; padding: 0 20px; }
@media (min-width: 1024px) { .container { padding: 0 40px; } }

/* ─────────────────────────────────────────────────────────────────────── */
/* NAVIGATION                                                               */
/* ─────────────────────────────────────────────────────────────────────── */
#nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 50;
  transition: transform .3s ease, background .3s ease, box-shadow .3s ease;
}
#nav .inner {
  max-width: 1280px;
  margin: 0 auto;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}
@media (min-width: 1024px) { #nav .inner { height: 80px; padding: 0 40px; } }

.nav-logo {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 15px;
  letter-spacing: -.01em;
  color: #111111;
}
.nav-links {
  display: none;
  align-items: center;
  gap: 36px;
  list-style: none;
}
@media (min-width: 1024px) { .nav-links { display: flex; } }
.nav-links a {
  font-size: 13px;
  letter-spacing: .06em;
  color: #4A4A4A;
  transition: color .2s;
}
.nav-links a:hover { color: #111111; }

.nav-right { display: flex; align-items: center; gap: 12px; }
.btn-cta {
  display: none;
  font-size: 13px;
  font-weight: 500;
  background: #5F6F65;
  color: #fff;
  padding: 10px 20px;
  border-radius: 999px;
  transition: background .2s;
}
.btn-cta:hover { background: #4A5A50; }
@media (min-width: 640px) { .btn-cta { display: inline-flex; } }

.btn-phone-icon {
  display: none;
  width: 36px; height: 36px;
  border-radius: 50%;
  border: 1px solid #E3E1DC;
  align-items: center;
  justify-content: center;
  color: #4A4A4A;
  transition: border-color .2s, color .2s;
}
.btn-phone-icon:hover { border-color: #5F6F65; color: #5F6F65; }
@media (min-width: 768px) { .btn-phone-icon { display: flex; } }

.btn-menu {
  display: flex;
  width: 36px; height: 36px;
  align-items: center;
  justify-content: center;
  color: #111111;
}
@media (min-width: 1024px) { .btn-menu { display: none; } }

/* ── Mobile menu ─────────────────────────────────────────────────────── */
#mobile-menu {
  position: fixed;
  inset: 0;
  z-index: 40;
  display: none;
}
#mobile-menu.open { display: block; }
.mm-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,.18);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}
.mm-panel {
  position: absolute;
  top: 64px; left: 0; right: 0;
  background: rgba(246,245,241,.96);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(227,225,220,.6);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.mm-panel a {
  font-size: 15px;
  color: #111111;
  padding: 12px 8px;
  transition: color .2s;
}
.mm-panel a:hover { color: #5F6F65; }
.mm-cta {
  margin-top: 12px;
  background: #5F6F65;
  color: #fff !important;
  font-weight: 500;
  font-size: 13px;
  padding: 12px 20px;
  border-radius: 999px;
  text-align: center;
}
.mm-cta:hover { background: #4A5A50; color: #fff !important; }

/* ─────────────────────────────────────────────────────────────────────── */
/* HERO                                                                     */
/* ─────────────────────────────────────────────────────────────────────── */
#hero {
  position: relative;
  width: 100%;
  min-height: 100dvh;
  display: flex;
  align-items: flex-end;
}
@media (min-width: 1024px) { #hero { align-items: center; } }

#hero .hero-bg {
  position: absolute;
  inset: 0;
}
#hero .hero-bg img {
  width: 100%; height: 100%;
  object-fit: cover;
  object-position: center;
}
#hero .hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,
    rgba(246,245,241,.82) 0%,
    rgba(246,245,241,.60) 35%,
    rgba(246,245,241,.38) 65%,
    rgba(246,245,241,.88) 100%);
}
#hero .hero-content {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 128px 20px 64px;
}
@media (min-width: 1024px) {
  #hero .hero-content { padding: 80px 40px; }
}
#hero .hero-inner { max-width: 640px; }

.hero-eyebrow {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: .12em;
  color: #5F6F65;
  margin-bottom: 20px;
}
.hero-h1 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(42px, 6vw, 80px);
  line-height: .95;
  letter-spacing: -.025em;
  color: #111111;
  font-weight: 500;
}
.hero-body {
  font-size: 16px;
  line-height: 1.65;
  color: #242424;
  max-width: 420px;
  margin-top: 24px;
}
@media (min-width: 1024px) { .hero-body { font-size: 18px; } }

.hero-btns {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 40px;
}
@media (min-width: 640px) { .hero-btns { flex-direction: row; } }

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  font-size: 14px;
  background: #5F6F65;
  color: #fff;
  padding: 14px 28px;
  border-radius: 999px;
  transition: background .2s;
  text-align: center;
}
.btn-primary:hover { background: #4A5A50; }
.btn-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  font-size: 14px;
  border: 1px solid #111111;
  color: #111111;
  padding: 14px 28px;
  border-radius: 999px;
  transition: background .2s, color .2s;
  text-align: center;
}
.btn-outline:hover { background: #111111; color: #fff; }

.hero-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 32px;
  margin-top: 56px;
}
.hero-stat-num {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(24px, 3vw, 32px);
  line-height: 1;
  color: #111111;
}
.hero-stat-label {
  font-size: 13px;
  color: #4A4A4A;
  margin-top: 4px;
}

/* ─────────────────────────────────────────────────────────────────────── */
/* SECTION SHARED STYLES                                                    */
/* ─────────────────────────────────────────────────────────────────────── */
.section-label {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: .12em;
  color: #5F6F65;
  margin-bottom: 16px;
}
.section-h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(32px, 4vw, 60px);
  line-height: 1;
  letter-spacing: -.02em;
  color: #111111;
  font-weight: 500;
}

/* ─────────────────────────────────────────────────────────────────────── */
/* SERVICES                                                                 */
/* ─────────────────────────────────────────────────────────────────────── */
#services {
  padding: 96px 20px;
  background: #FAFAF7;
}
@media (min-width: 1024px) { #services { padding: 144px 40px; } }

#services .section-head { max-width: 600px; margin-bottom: 64px; }
@media (min-width: 1024px) { #services .section-head { margin-bottom: 96px; } }

.services-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}
@media (min-width: 640px)  { .services-grid { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1024px) { .services-grid { grid-template-columns: repeat(4,1fr); gap: 24px; } }

.service-card {
  background: #fff;
  border-radius: 16px;
  padding: 28px;
  box-shadow: 0 1px 3px rgba(0,0,0,.04);
  transition: background .4s, box-shadow .4s;
  cursor: default;
}
@media (min-width: 1024px) { .service-card { padding: 32px; } }
.service-card:hover { background: #5F6F65; box-shadow: 0 8px 24px rgba(95,111,101,.18); }

.service-icon {
  width: 36px; height: 36px;
  color: #5F6F65;
  transition: color .4s;
}
.service-card:hover .service-icon { color: #fff; }

.service-title {
  font-weight: 600;
  font-size: 17px;
  color: #111111;
  margin: 24px 0 8px;
  transition: color .4s;
}
.service-card:hover .service-title { color: #fff; }

.service-desc {
  font-size: 14px;
  color: #242424;
  line-height: 1.6;
  transition: color .4s;
}
.service-card:hover .service-desc { color: rgba(255,255,255,.85); }

.service-footer {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #E3E1DC;
  transition: border-color .4s;
}
.service-card:hover .service-footer { border-color: rgba(255,255,255,.2); }

.service-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-weight: 500;
  font-size: 13px;
  color: #5F6F65;
  transition: color .4s;
}
.service-card:hover .service-link { color: #fff; }

/* ─────────────────────────────────────────────────────────────────────── */
/* PROCESS                                                                  */
/* ─────────────────────────────────────────────────────────────────────── */
#process {
  padding: 96px 20px;
  background: #F6F5F1;
}
@media (min-width: 1024px) { #process { padding: 144px 40px; } }

#process .section-head { max-width: 600px; margin-bottom: 64px; }
@media (min-width: 1024px) { #process .section-head { margin-bottom: 96px; } }

.process-steps { display: flex; flex-direction: column; gap: 64px; }
@media (min-width: 1024px) { .process-steps { gap: 96px; } }

.process-step {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  align-items: center;
}
@media (min-width: 1024px) {
  .process-step { grid-template-columns: 1fr 1fr; gap: 64px; }
  .process-step.reverse .step-img  { order: 2; }
  .process-step.reverse .step-text { order: 1; padding-right: 40px; }
  .process-step:not(.reverse) .step-text { padding-left: 40px; }
}

.step-img { border-radius: 16px; overflow: hidden; }
.step-img img {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  transition: transform .7s ease;
}
.step-img:hover img { transform: scale(1.03); }

.step-num {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(64px, 8vw, 96px);
  line-height: 1;
  color: #D8CEC2;
  font-weight: 500;
}
.step-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(22px, 2.5vw, 32px);
  line-height: 1.15;
  color: #111111;
  margin: 8px 0 16px;
  font-weight: 500;
}
.step-desc {
  font-size: 15px;
  color: #242424;
  line-height: 1.7;
  max-width: 400px;
}

/* ─────────────────────────────────────────────────────────────────────── */
/* GALLERY                                                                  */
/* ─────────────────────────────────────────────────────────────────────── */
#gallery {
  padding: 96px 20px;
  background: #FAFAF7;
}
@media (min-width: 1024px) { #gallery { padding: 144px 40px; } }

#gallery .section-head { max-width: 600px; margin-bottom: 64px; }
@media (min-width: 1024px) { #gallery .section-head { margin-bottom: 96px; } }

.gallery-grid {
  columns: 2;
  gap: 12px;
}
@media (min-width: 768px) { .gallery-grid { columns: 3; gap: 16px; } }

.gallery-item {
  break-inside: avoid;
  margin-bottom: 12px;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
}
@media (min-width: 768px) { .gallery-item { margin-bottom: 16px; } }
.gallery-item img {
  width: 100%;
  object-fit: cover;
  transition: transform .7s ease;
}
.gallery-item:hover img { transform: scale(1.04); }

/* ── Lightbox ────────────────────────────────────────────────────────── */
#lightbox {
  position: fixed;
  inset: 0;
  z-index: 50;
  background: rgba(0,0,0,.95);
  display: none;
  align-items: center;
  justify-content: center;
}
#lightbox.open { display: flex; }
#lb-close {
  position: absolute;
  top: 20px; right: 20px;
  color: rgba(255,255,255,.6);
  transition: color .2s;
  z-index: 1;
}
#lb-close:hover { color: #fff; }
#lb-prev, #lb-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255,255,255,.4);
  transition: color .2s;
  z-index: 1;
  display: none;
}
@media (min-width: 640px) { #lb-prev, #lb-next { display: block; } }
#lb-prev:hover, #lb-next:hover { color: #fff; }
#lb-prev { left: 16px; }
#lb-next { right: 16px; }
#lb-content { max-width: 90vw; max-height: 88vh; }
#lb-img { max-width: 100%; max-height: 88vh; object-fit: contain; border-radius: 4px; }

/* ─────────────────────────────────────────────────────────────────────── */
/* REFERENCES                                                               */
/* ─────────────────────────────────────────────────────────────────────── */
#references {
  padding: 96px 0;
  background: #F6F5F1;
}
@media (min-width: 1024px) { #references { padding: 144px 0; } }

#references .ref-head {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 48px;
}
@media (min-width: 1024px) {
  #references .ref-head { padding: 0 40px; margin-bottom: 64px; }
}
.ref-nav { display: none; gap: 8px; }
@media (min-width: 1024px) { .ref-nav { display: flex; } }
.ref-nav button {
  width: 40px; height: 40px;
  border-radius: 50%;
  border: 1px solid #E3E1DC;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4A4A4A;
  cursor: pointer;
  transition: border-color .2s, color .2s;
}
.ref-nav button:hover { border-color: #5F6F65; color: #5F6F65; }

.ref-scroll {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  padding-left: 20px;
  padding-right: 20px;
  scroll-snap-type: x mandatory;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.ref-scroll::-webkit-scrollbar { display: none; }
@media (min-width: 1024px) { .ref-scroll { padding-left: 40px; gap: 20px; } }

.ref-card {
  flex-shrink: 0;
  width: 320px;
  background: #fff;
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 1px 3px rgba(0,0,0,.04);
  border: 1px solid rgba(227,225,220,.6);
  scroll-snap-align: start;
}
@media (min-width: 1024px) { .ref-card { width: 420px; padding: 36px; } }

.ref-stars { display: flex; gap: 2px; }
.ref-stars svg { fill: #f59e0b; color: #f59e0b; }
.ref-text {
  font-size: 15px;
  color: #242424;
  line-height: 1.7;
  margin-top: 24px;
}
@media (min-width: 1024px) { .ref-text { font-size: 16px; } }
.ref-footer {
  margin-top: 32px;
  padding-top: 20px;
  border-top: 1px solid rgba(227,225,220,.6);
}
.ref-name { font-weight: 600; font-size: 14px; color: #111111; }
.ref-loc  { font-size: 13px; color: #5A5A5A; }

/* ─────────────────────────────────────────────────────────────────────── */
/* PRICING                                                                  */
/* ─────────────────────────────────────────────────────────────────────── */
#pricing {
  padding: 96px 20px;
  background: #FAFAF7;
}
@media (min-width: 1024px) { #pricing { padding: 144px 40px; } }

#pricing .section-head { text-align: center; max-width: 520px; margin: 0 auto 64px; }
@media (min-width: 1024px) { #pricing .section-head { margin-bottom: 96px; } }

.pricing-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}
@media (min-width: 768px) { .pricing-grid { grid-template-columns: repeat(3,1fr); } }
@media (min-width: 1024px) { .pricing-grid { gap: 24px; } }

.price-card {
  position: relative;
  background: #fff;
  border-radius: 24px;
  padding: 32px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0,0,0,.04);
}
@media (min-width: 1024px) { .price-card { padding: 40px; } }
.price-card.featured { outline: 2px solid #5F6F65; }

.price-badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: #5F6F65;
  color: #fff;
  font-size: 11px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: .06em;
  padding: 4px 16px;
  border-radius: 999px;
  white-space: nowrap;
}
.price-icon { color: #5F6F65; margin: 0 auto; }
.price-title {
  font-weight: 600;
  font-size: 18px;
  color: #111111;
  margin-top: 20px;
}
.price-amount {
  margin-top: 16px;
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 4px;
}
.price-num {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(44px, 4vw, 56px);
  color: #111111;
  line-height: 1;
  font-weight: 500;
}
.price-unit { font-size: 16px; color: #5A5A5A; }
.price-note { font-size: 13px; color: #5A5A5A; margin-top: 4px; }
.price-divider { width: 100%; height: 1px; background: #E3E1DC; margin: 28px 0; }
.price-features {
  list-style: none;
  text-align: left;
  max-width: 240px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.price-features li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 14px;
  color: #242424;
}
.price-check { color: #5F6F65; flex-shrink: 0; margin-top: 2px; }
.price-btn {
  display: block;
  width: 100%;
  margin-top: 32px;
  font-weight: 500;
  font-size: 14px;
  padding: 14px;
  border-radius: 999px;
  transition: background .2s, color .2s;
  text-align: center;
}
.price-btn.dark { background: #1F1F1F; color: #fff; }
.price-btn.dark:hover { background: #000; }
.price-btn.green { background: #5F6F65; color: #fff; }
.price-btn.green:hover { background: #4A5A50; }
.pricing-note { font-size: 14px; color: #5A5A5A; text-align: center; margin-top: 40px; }

/* ─────────────────────────────────────────────────────────────────────── */
/* FAQ                                                                      */
/* ─────────────────────────────────────────────────────────────────────── */
#faq {
  padding: 96px 20px;
  background: #F6F5F1;
}
@media (min-width: 1024px) { #faq { padding: 144px 40px; } }

#faq .section-head { text-align: center; margin-bottom: 48px; }
@media (min-width: 1024px) { #faq .section-head { margin-bottom: 80px; } }
#faq .faq-inner { max-width: 720px; margin: 0 auto; }

.faq-item { border-bottom: 1px solid #E3E1DC; }
.faq-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 24px 0;
  text-align: left;
  gap: 24px;
  cursor: pointer;
  background: none;
  border: none;
  font-family: inherit;
}
.faq-q {
  font-weight: 600;
  font-size: 16px;
  color: #111111;
  line-height: 1.4;
  transition: color .2s;
}
@media (min-width: 1024px) { .faq-q { font-size: 18px; } }
.faq-btn:hover .faq-q { color: #5F6F65; }
.faq-icon {
  flex-shrink: 0;
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid #E3E1DC;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #5F6F65;
  transition: transform .3s, background .3s, border-color .3s, color .3s;
}
.faq-icon.open {
  transform: rotate(45deg);
  background: #5F6F65;
  border-color: #5F6F65;
  color: #fff;
}
.faq-answer {
  overflow: hidden;
  max-height: 0;
  transition: max-height .4s ease, padding-bottom .4s ease;
}
.faq-answer p {
  font-size: 15px;
  color: #242424;
  line-height: 1.7;
  padding-bottom: 24px;
}

/* ─────────────────────────────────────────────────────────────────────── */
/* CONTACT                                                                  */
/* ─────────────────────────────────────────────────────────────────────── */
#contact {
  padding: 112px 20px;
  background: #FAFAF7;
}
@media (min-width: 1024px) { #contact { padding: 176px 40px; } }

.contact-inner {
  max-width: 680px;
  margin: 0 auto;
  text-align: center;
}
.contact-eyebrow {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: .14em;
  color: #5F6F65;
  margin-bottom: 20px;
}
.contact-h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(40px, 5vw, 68px);
  line-height: .98;
  letter-spacing: -.025em;
  color: #111111;
  font-weight: 500;
}
.contact-body {
  font-size: 16px;
  color: #242424;
  line-height: 1.65;
  max-width: 460px;
  margin: 24px auto 0;
}
@media (min-width: 1024px) { .contact-body { font-size: 18px; } }

.contact-btns {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  margin-top: 40px;
}
@media (min-width: 640px) { .contact-btns { flex-direction: row; justify-content: center; } }

.btn-contact-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  justify-content: center;
  background: #5F6F65;
  color: #fff;
  font-weight: 500;
  font-size: 14px;
  padding: 16px 32px;
  border-radius: 999px;
  transition: background .3s, box-shadow .3s, transform .3s;
}
.btn-contact-primary:hover {
  background: #4A5A50;
  box-shadow: 0 8px 24px rgba(95,111,101,.15);
  transform: translateY(-2px);
}
@media (min-width: 640px) { .btn-contact-primary { width: auto; } }

.btn-contact-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  justify-content: center;
  border: 1px solid #111111;
  color: #111111;
  font-weight: 500;
  font-size: 14px;
  padding: 16px 32px;
  border-radius: 999px;
  transition: background .3s, color .3s, transform .3s;
}
.btn-contact-secondary:hover {
  background: #111111;
  color: #fff;
  transform: translateY(-2px);
}
@media (min-width: 640px) { .btn-contact-secondary { width: auto; } }

.contact-divider { width: 48px; height: 1px; background: #E3E1DC; margin: 56px auto 0; }

.contact-meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 32px 12px;
  margin-top: 40px;
}
.contact-meta-item { text-align: center; }
.contact-meta-label {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: #5A5A5A;
  margin-bottom: 2px;
}
.contact-meta-value { font-size: 13px; color: #111111; }
.contact-meta-sep { width: 1px; height: 24px; background: #E3E1DC; display: none; }
@media (min-width: 640px) { .contact-meta-sep { display: block; } }

.contact-badges {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 40px;
}
.badge {
  font-size: 12px;
  background: #F6F5F1;
  color: #4A4A4A;
  padding: 6px 14px;
  border-radius: 999px;
}

/* ─────────────────────────────────────────────────────────────────────── */
/* FOOTER                                                                   */
/* ─────────────────────────────────────────────────────────────────────── */
footer {
  padding: 56px 20px;
  background: #1F1F1F;
}
@media (min-width: 1024px) { footer { padding: 80px 40px; } }

.footer-grid {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
}
@media (min-width: 640px)  { .footer-grid { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1024px) { .footer-grid { grid-template-columns: repeat(4,1fr); gap: 32px; } }

.footer-brand { font-weight: 500; font-size: 17px; color: #fff; }
.footer-sub   { font-size: 13px; color: rgba(255,255,255,.6); margin-top: 2px; }
.footer-desc  { font-size: 13px; color: rgba(255,255,255,.55); margin-top: 12px; max-width: 220px; line-height: 1.6; }
.footer-contacts { margin-top: 20px; display: flex; flex-direction: column; gap: 8px; }
.footer-contacts a { font-size: 13px; color: rgba(255,255,255,.7); transition: color .2s; }
.footer-contacts a:hover { color: #fff; }
.footer-col-head { font-size: 11px; text-transform: uppercase; letter-spacing: .1em; color: rgba(255,255,255,.5); margin-bottom: 16px; }
.footer-col-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.footer-col-links a, .footer-col-links span {
  font-size: 14px;
  color: rgba(255,255,255,.75);
  transition: color .2s;
  cursor: pointer;
}
.footer-col-links a:hover, .footer-col-links span:hover { color: #fff; }
.footer-bottom {
  max-width: 1280px;
  margin: 48px auto 0;
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
@media (min-width: 640px) {
  .footer-bottom { flex-direction: row; justify-content: space-between; }
}
.footer-copy { font-size: 12px; color: rgba(255,255,255,.45); }

/* ─────────────────────────────────────────────────────────────────────── */
/* FLOATING CTA                                                             */
/* ─────────────────────────────────────────────────────────────────────── */
#float-mobile {
  position: fixed;
  bottom: 0; left: 0; right: 0;
  z-index: 40;
  background: rgba(250,250,247,.96);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid rgba(225,224,220,.6);
  padding: 12px;
  display: flex;
  gap: 10px;
}
@media (min-width: 1024px) { #float-mobile { display: none; } }
#float-mobile .fm-call {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: #111111;
  color: #fff;
  font-weight: 500;
  font-size: 13px;
  padding: 14px;
  border-radius: 999px;
  transition: background .2s;
}
#float-mobile .fm-call:hover { background: #333; }
#float-mobile .fm-cta {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #5F6F65;
  color: #fff;
  font-weight: 500;
  font-size: 13px;
  padding: 14px;
  border-radius: 999px;
  transition: background .2s;
}
#float-mobile .fm-cta:hover { background: #4A5A50; }

#float-desktop {
  position: fixed;
  bottom: 24px; right: 24px;
  z-index: 40;
  width: 48px; height: 48px;
  background: #5F6F65;
  color: #fff;
  border-radius: 50%;
  display: none;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0,0,0,.15);
  transition: background .2s, transform .2s;
}
#float-desktop:hover { background: #4A5A50; transform: scale(1.05); }
@media (min-width: 1024px) { #float-desktop { display: flex; } }
"""

css_path = f"{BUILD_DIR}/css/style.css"
with open(css_path, "w", encoding="utf-8") as f:
    f.write(CSS)
print(f"Wrote style.css ({len(CSS)//1024}KB)")

# ══════════════════════════════════════════════════════════════════════════
# JavaScript
# ══════════════════════════════════════════════════════════════════════════
JS = r"""
// ── GSAP setup ─────────────────────────────────────────────────────────────
gsap.registerPlugin(ScrollTrigger);

// ── Smooth scroll for all internal links ───────────────────────────────────
document.addEventListener('click', function(e) {
  var a = e.target.closest('a[href^="#"]');
  if (!a) return;
  var href = a.getAttribute('href');
  e.preventDefault();
  closeMobileMenu();
  if (href === '#') { window.scrollTo({ top: 0, behavior: 'smooth' }); return; }
  var target = document.querySelector(href);
  if (target) target.scrollIntoView({ behavior: 'smooth' });
});

// ── Navigation ─────────────────────────────────────────────────────────────
var nav = document.getElementById('nav');
var lastY = 0;

window.addEventListener('scroll', function() {
  var y = window.scrollY;
  nav.style.transform = (y > lastY && y > 200) ? 'translateY(-100%)' : 'translateY(0)';
  if (y > 80) {
    nav.style.background = 'rgba(246,245,241,0.92)';
    nav.style.backdropFilter = 'blur(20px)';
    nav.style.webkitBackdropFilter = 'blur(20px)';
    nav.style.boxShadow = '0 1px 0 rgba(0,0,0,0.04)';
  } else {
    nav.style.background = 'transparent';
    nav.style.backdropFilter = '';
    nav.style.webkitBackdropFilter = '';
    nav.style.boxShadow = '';
  }
  lastY = y;
}, { passive: true });

// ── Mobile menu ────────────────────────────────────────────────────────────
var mobileMenu = document.getElementById('mobile-menu');
var menuBtn    = document.getElementById('menu-btn');
var backdrop   = document.getElementById('mm-backdrop');

function openMobileMenu()  { mobileMenu.classList.add('open'); }
function closeMobileMenu() { mobileMenu.classList.remove('open'); }

if (menuBtn)  menuBtn.addEventListener('click', function() {
  mobileMenu.classList.contains('open') ? closeMobileMenu() : openMobileMenu();
});
if (backdrop) backdrop.addEventListener('click', closeMobileMenu);

// ── Hero GSAP ──────────────────────────────────────────────────────────────
(function() {
  var els = document.querySelectorAll('#hero .hero-inner > *');
  if (!els.length) return;
  gsap.fromTo(els,
    { opacity: 0, y: 30 },
    { opacity: 1, y: 0, duration: 0.9, stagger: 0.12, ease: 'power3.out', delay: 0.3 }
  );
})();

// ── Services GSAP ──────────────────────────────────────────────────────────
gsap.fromTo('.service-card',
  { opacity: 0, y: 50 },
  { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: 'power3.out',
    scrollTrigger: { trigger: '#services', start: 'top 78%' } }
);

// ── Process GSAP (alternating) ─────────────────────────────────────────────
document.querySelectorAll('.process-step').forEach(function(el, i) {
  gsap.fromTo(el,
    { opacity: 0, x: i % 2 === 0 ? -40 : 40 },
    { opacity: 1, x: 0, duration: 0.9, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 80%' } }
  );
});

// ── Gallery GSAP ───────────────────────────────────────────────────────────
gsap.fromTo('.gallery-item',
  { opacity: 0, y: 30, scale: 0.97 },
  { opacity: 1, y: 0, scale: 1, duration: 0.7, stagger: 0.06, ease: 'power3.out',
    scrollTrigger: { trigger: '#gallery', start: 'top 80%' } }
);

// ── References GSAP ────────────────────────────────────────────────────────
gsap.fromTo('.ref-card',
  { opacity: 0, x: 40 },
  { opacity: 1, x: 0, duration: 0.8, stagger: 0.08, ease: 'power3.out',
    scrollTrigger: { trigger: '#references', start: 'top 75%' } }
);

// ── Pricing GSAP ───────────────────────────────────────────────────────────
gsap.fromTo('.price-card',
  { opacity: 0, y: 50 },
  { opacity: 1, y: 0, duration: 0.8, stagger: 0.12, ease: 'power3.out',
    scrollTrigger: { trigger: '#pricing', start: 'top 75%' } }
);

// ── FAQ GSAP ───────────────────────────────────────────────────────────────
gsap.fromTo('.faq-item',
  { opacity: 0, y: 20 },
  { opacity: 1, y: 0, duration: 0.6, stagger: 0.05, ease: 'power3.out',
    scrollTrigger: { trigger: '#faq', start: 'top 80%' } }
);

// ── Contact GSAP ───────────────────────────────────────────────────────────
gsap.fromTo('.contact-el',
  { opacity: 0, y: 30 },
  { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: 'power3.out',
    scrollTrigger: { trigger: '#contact', start: 'top 75%' } }
);

// ── FAQ Accordion ──────────────────────────────────────────────────────────
document.querySelectorAll('.faq-item').forEach(function(item) {
  var btn  = item.querySelector('.faq-btn');
  var ans  = item.querySelector('.faq-answer');
  var icon = item.querySelector('.faq-icon');
  if (!btn) return;
  btn.addEventListener('click', function() {
    var open = ans.style.maxHeight && ans.style.maxHeight !== '0px';
    // Close all
    document.querySelectorAll('.faq-item').forEach(function(it) {
      it.querySelector('.faq-answer').style.maxHeight = '0px';
      it.querySelector('.faq-icon').classList.remove('open');
    });
    if (!open) {
      ans.style.maxHeight = ans.scrollHeight + 48 + 'px';
      icon.classList.add('open');
    }
  });
});

// ── References carousel ────────────────────────────────────────────────────
var refScroll = document.querySelector('.ref-scroll');
document.getElementById('ref-prev') && document.getElementById('ref-prev').addEventListener('click', function() {
  refScroll.scrollBy({ left: -460, behavior: 'smooth' });
});
document.getElementById('ref-next') && document.getElementById('ref-next').addEventListener('click', function() {
  refScroll.scrollBy({ left: 460, behavior: 'smooth' });
});

// ── Gallery Lightbox ───────────────────────────────────────────────────────
(function() {
  var lightbox = document.getElementById('lightbox');
  var lbImg    = document.getElementById('lb-img');
  var lbClose  = document.getElementById('lb-close');
  var lbPrev   = document.getElementById('lb-prev');
  var lbNext   = document.getElementById('lb-next');
  var lbContent= document.getElementById('lb-content');
  if (!lightbox) return;

  var imgs = [];
  var cur  = 0;

  document.querySelectorAll('.gallery-item').forEach(function(item, i) {
    imgs.push(item.querySelector('img').getAttribute('src'));
    item.addEventListener('click', function() { open(i); });
  });

  function open(i) {
    cur = i;
    lbImg.src = imgs[cur];
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
    lbImg.src = '';
  }
  function prev() { cur = cur === 0 ? imgs.length-1 : cur-1; lbImg.src = imgs[cur]; }
  function next() { cur = cur === imgs.length-1 ? 0 : cur+1; lbImg.src = imgs[cur]; }

  lbClose.addEventListener('click', close);
  lightbox.addEventListener('click', close);
  if (lbContent) lbContent.addEventListener('click', function(e) { e.stopPropagation(); });
  if (lbPrev)    lbPrev.addEventListener('click', function(e) { e.stopPropagation(); prev(); });
  if (lbNext)    lbNext.addEventListener('click', function(e) { e.stopPropagation(); next(); });

  document.addEventListener('keydown', function(e) {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape')     close();
    if (e.key === 'ArrowLeft')  prev();
    if (e.key === 'ArrowRight') next();
  });
})();
"""

js_path = f"{BUILD_DIR}/js/script.js"
with open(js_path, "w", encoding="utf-8") as f:
    f.write(JS)
print(f"Wrote script.js ({len(JS)//1024}KB)")

# ══════════════════════════════════════════════════════════════════════════
# SVG icons (inline, so no icon font needed)
# ══════════════════════════════════════════════════════════════════════════
ICON_PHONE  = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 9.91a16 16 0 0 0 6.29 6.29l1.08-.97a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
ICON_PHONE_S= '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 9.91a16 16 0 0 0 6.29 6.29l1.08-.97a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
ICON_MAIL   = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
ICON_ARROW  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
ICON_ARROWR = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7l10 10M17 7v10H7"/></svg>'
ICON_CHECK  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
ICON_PLUS   = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'
ICON_X      = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
ICON_MENU   = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/></svg>'
ICON_PREV   = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>'
ICON_NEXT   = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>'
ICON_PREVS  = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>'
ICON_NEXTS  = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>'
ICON_CLOSE  = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
ICON_STAR   = '<svg width="15" height="15" viewBox="0 0 24 24" fill="#f59e0b" stroke="#f59e0b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'

# Service icons
ICON_BRUSH  = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="service-icon"><path d="m9.06 11.9 8.07-8.06a2.85 2.85 0 1 1 4.03 4.03l-8.06 8.08"/><path d="M7.07 14.94c-1.66 0-3 1.35-3 3.02 0 1.33-2.5 1.52-2 2.02 1 1 2.49 2.02 4 2.02 2.2 0 4-1.8 4-4.04a3.01 3.01 0 0 0-3-3.02z"/></svg>'
ICON_HOME   = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="service-icon"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
ICON_BLDG   = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="service-icon"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>'
ICON_SPARKL = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="service-icon"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/><path d="M5 3v4"/><path d="M19 17v4"/><path d="M3 5h4"/><path d="M17 19h4"/></svg>'
ICON_GRID   = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="price-icon"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>'
ICON_HOME2  = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="price-icon"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
ICON_BLDG2  = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="price-icon"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>'

STARS5 = ICON_STAR * 5

# Gallery images are img-05 through img-24
gallery_imgs = [f'./images/img-{i:02d}.jpg' for i in range(5, 25)]
gallery_items = "\n".join(
    f'          <div class="gallery-item"><img src="{src}" alt="" loading="lazy"/></div>'
    for src in gallery_imgs
)

# ══════════════════════════════════════════════════════════════════════════
# HTML
# ══════════════════════════════════════════════════════════════════════════
HTML = f"""<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Malíři Profi Praha | Profesionální malířské služby od roku 1992</title>
  <meta name="description" content="Profesionální malířské služby v Praze — malování bytů, domů a kanceláří. 30 let zkušeností, čistá práce, férové ceny. Nezávazná kalkulace zdarma."/>
  <meta name="author" content="David Telvak - Malíři Profi"/>
  <meta name="keywords" content="malíř pokojů Praha,malování bytů Praha,malířské práce Praha,malování kanceláří Praha,malíři Praha"/>
  <meta name="robots" content="index, follow"/>
  <meta property="og:title" content="Malíři Profi Praha | Profesionální malířské služby"/>
  <meta property="og:description" content="Malování bytů, domů a kanceláří po celé Praze a okolí. 30 let zkušeností, čistá práce, férové ceny."/>
  <meta property="og:locale" content="cs_CZ"/>
  <meta property="og:type" content="website"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <link rel="preload" as="image" href="./images/img-21.jpg"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="./css/style.css"/>
</head>
<body>

<!-- ═══════════════════════════════ NAVIGATION ═══════════════════════════ -->
<nav id="nav">
  <div class="inner">
    <a href="#" class="nav-logo">Malíři Profi</a>

    <ul class="nav-links">
      <li><a href="#services">Služby</a></li>
      <li><a href="#process">Proces</a></li>
      <li><a href="#gallery">Realizace</a></li>
      <li><a href="#pricing">Ceník</a></li>
      <li><a href="#contact">Kontakt</a></li>
    </ul>

    <div class="nav-right">
      <a href="#contact" class="btn-cta">Kalkulace zdarma</a>
      <a href="tel:+420737171208" class="btn-phone-icon" aria-label="Zavolat">
        {ICON_PHONE_S}
      </a>
      <button id="menu-btn" class="btn-menu" aria-label="Menu">
        {ICON_MENU}
      </button>
    </div>
  </div>
</nav>

<!-- Mobile menu -->
<div id="mobile-menu">
  <div class="mm-backdrop" id="mm-backdrop"></div>
  <div class="mm-panel">
    <a href="#services">Služby</a>
    <a href="#process">Proces</a>
    <a href="#gallery">Realizace</a>
    <a href="#pricing">Ceník</a>
    <a href="#contact">Kontakt</a>
    <a href="tel:+420737171208" class="mm-cta">Zavolat: +420 737 171 208</a>
  </div>
</div>

<!-- ═══════════════════════════════ HERO ═════════════════════════════════ -->
<section id="hero">
  <div class="hero-bg">
    <img src="./images/img-21.jpg" alt="Malířské práce Praha"/>
    <div class="hero-overlay"></div>
  </div>
  <div class="hero-content">
    <div class="hero-inner">
      <p class="hero-eyebrow">Profesionální malířské služby v Praze od roku 1992</p>
      <h1 class="hero-h1">Precizní malířské práce, na které se můžete spolehnout</h1>
      <p class="hero-body">Malování bytů, domů a kanceláří v Praze a okolí. Třicet let zkušeností, čistá práce, férové ceny.</p>
      <div class="hero-btns">
        <a href="#contact" class="btn-primary">Nezávazná kalkulace zdarma</a>
        <a href="tel:+420737171208" class="btn-outline">Zavolat nyní</a>
      </div>
      <div class="hero-stats">
        <div>
          <p class="hero-stat-num">30+</p>
          <p class="hero-stat-label">let zkušeností</p>
        </div>
        <div>
          <p class="hero-stat-num">500+</p>
          <p class="hero-stat-label">realizací</p>
        </div>
        <div>
          <p class="hero-stat-num">50 km</p>
          <p class="hero-stat-label">okolí Prahy</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ SERVICES ═════════════════════════════ -->
<section id="services">
  <div class="container">
    <div class="section-head">
      <p class="section-label">Naše služby</p>
      <h2 class="section-h2">Kompletní malířské řešení</h2>
    </div>
    <div class="services-grid">

      <div class="service-card">
        {ICON_BRUSH}
        <h3 class="service-title">Malování bytů a domů</h3>
        <p class="service-desc">Kompletní vymalování bytů všech velikostí i rodinných domů. Od přípravy povrchu až po finální úklid.</p>
        <div class="service-footer">
          <a href="#contact" class="service-link">Zjistit více {ICON_ARROWR}</a>
        </div>
      </div>

      <div class="service-card">
        {ICON_HOME}
        <h3 class="service-title">Renovace interiérů</h3>
        <p class="service-desc">Škrábání starých nátěrů, penetrace, opravy zdí a štukování. Příprava pro dokonalý výsledek.</p>
        <div class="service-footer">
          <a href="#contact" class="service-link">Zjistit více {ICON_ARROWR}</a>
        </div>
      </div>

      <div class="service-card">
        {ICON_BLDG}
        <h3 class="service-title">Komerční prostory</h3>
        <p class="service-desc">Malování kanceláří, obchodů a firemních prostor. Rychlé termíny, minimální omezení provozu.</p>
        <div class="service-footer">
          <a href="#contact" class="service-link">Zjistit více {ICON_ARROWR}</a>
        </div>
      </div>

      <div class="service-card">
        {ICON_SPARKL}
        <h3 class="service-title">Specializované práce</h3>
        <p class="service-desc">Dekorativní malby, lakování nábytku, míchání barev na míru, tapetování a úklid po malování.</p>
        <div class="service-footer">
          <a href="#contact" class="service-link">Zjistit více {ICON_ARROWR}</a>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════ PROCESS ══════════════════════════════ -->
<section id="process">
  <div class="container">
    <div class="section-head">
      <p class="section-label">Jak to funguje</p>
      <h2 class="section-h2">Od konzultace po předání</h2>
    </div>

    <div class="process-steps">

      <div class="process-step">
        <div class="step-img">
          <img src="./images/img-01.jpg" alt="Bezplatná konzultace" loading="lazy"/>
        </div>
        <div class="step-text">
          <span class="step-num">01</span>
          <h3 class="step-title">Bezplatná konzultace a kalkulace</h3>
          <p class="step-desc">Přijedeme na obhlídku, posoudíme rozsah prací a připravíme nezávaznou cenovou nabídku na míru. Bez skrytých poplatků.</p>
        </div>
      </div>

      <div class="process-step reverse">
        <div class="step-img">
          <img src="./images/img-02.jpg" alt="Profesionální příprava" loading="lazy"/>
        </div>
        <div class="step-text">
          <span class="step-num">02</span>
          <h3 class="step-title">Profesionální příprava</h3>
          <p class="step-desc">Zakryjeme podlahy, odmontujeme zásuvky, opravíme nedokonalosti zdí, provedeme penetraci a štukování.</p>
        </div>
      </div>

      <div class="process-step">
        <div class="step-img">
          <img src="./images/img-03.jpg" alt="Precizní realizace" loading="lazy"/>
        </div>
        <div class="step-text">
          <span class="step-num">03</span>
          <h3 class="step-title">Precizní realizace</h3>
          <p class="step-desc">Nanášíme kvalitní barvy renomovaných značek dvěma vrstvami. Pracujeme čistě, efektivně a s ohledem na váš režim.</p>
        </div>
      </div>

      <div class="process-step reverse">
        <div class="step-img">
          <img src="./images/img-04.jpg" alt="Úklid a předání" loading="lazy"/>
        </div>
        <div class="step-text">
          <span class="step-num">04</span>
          <h3 class="step-title">Úklid a předání</h3>
          <p class="step-desc">Po dokončení uklidíme, namontujeme zpět veškeré kryty a předáme vám dokonale vymalovaný prostor.</p>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════ GALLERY ══════════════════════════════ -->
<section id="gallery">
  <div class="container">
    <div class="section-head">
      <p class="section-label">Realizace</p>
      <h2 class="section-h2">Ukázky naší práce</h2>
    </div>
    <div class="gallery-grid">
{gallery_items}
    </div>
  </div>
</section>

<!-- Lightbox -->
<div id="lightbox">
  <button id="lb-close">{ICON_CLOSE}</button>
  <button id="lb-prev">{ICON_PREV}</button>
  <button id="lb-next">{ICON_NEXT}</button>
  <div id="lb-content">
    <img id="lb-img" src="" alt=""/>
  </div>
</div>

<!-- ═══════════════════════════════ REFERENCES ═══════════════════════════ -->
<section id="references">
  <div class="ref-head">
    <div>
      <p class="section-label">Reference</p>
      <h2 class="section-h2">Co říkají naši zákazníci</h2>
    </div>
    <div class="ref-nav">
      <button id="ref-prev">{ICON_PREVS}</button>
      <button id="ref-next">{ICON_NEXTS}</button>
    </div>
  </div>

  <div class="ref-scroll">

    <div class="ref-card">
      <div class="ref-stars">{STARS5}</div>
      <p class="ref-text">Pan Telvak a jeho tým odvedli skvělou práci. Vymalovali celý náš byt za 2 dny, vše uklidili a výsledek předčil očekávání. Profesionální přístup od začátku do konce.</p>
      <div class="ref-footer">
        <p class="ref-name">Jana K.</p>
        <p class="ref-loc">Praha 2</p>
      </div>
    </div>

    <div class="ref-card">
      <div class="ref-stars">{STARS5}</div>
      <p class="ref-text">Už jsem vyzkoušel několik malířů, ale tihle jsou jiná liga. Precizní práce, čistota, dochvilnost. Cena byla přesně podle dohody. Doporučuji všem.</p>
      <div class="ref-footer">
        <p class="ref-name">Martin P.</p>
        <p class="ref-loc">Praha 6</p>
      </div>
    </div>

    <div class="ref-card">
      <div class="ref-stars">{STARS5}</div>
      <p class="ref-text">Potřebovali jsme rychle vymalovat kancelář před otevřením nové pobočky. Termín dodrželi, cena byla férová a kvalita výborná. Budeme spolupracovat i nadále.</p>
      <div class="ref-footer">
        <p class="ref-name">Lenka S.</p>
        <p class="ref-loc">Praha 10</p>
      </div>
    </div>

    <div class="ref-card">
      <div class="ref-stars">{STARS5}</div>
      <p class="ref-text">Vymalování starého bytu po babičce — škrábání starých maleb, opravy zdí, penetrace. Dnes to vypadá jako nový byt. Obrovské díky za trpělivost a preciznost.</p>
      <div class="ref-footer">
        <p class="ref-name">Petr D.</p>
        <p class="ref-loc">Praha 8</p>
      </div>
    </div>

    <div class="ref-card">
      <div class="ref-stars">{STARS5}</div>
      <p class="ref-text">Neuvěřitelná proměna našeho domu. Exteriér i interiér, všechno dokonale sladěné. Komunikace byla výborná, vždy věděli, co se děje a kdy.</p>
      <div class="ref-footer">
        <p class="ref-name">Kateřina N.</p>
        <p class="ref-loc">Praha 4</p>
      </div>
    </div>

    <div class="ref-card">
      <div class="ref-stars">{STARS5}</div>
      <p class="ref-text">Malování dětského pokoje s dekorativní malbou. Syn je nadšený, výsledek je úžasný. Kreativní přístup a dokonalé provedení.</p>
      <div class="ref-footer">
        <p class="ref-name">Tomáš H.</p>
        <p class="ref-loc">Praha 3</p>
      </div>
    </div>

  </div>
</section>

<!-- ═══════════════════════════════ PRICING ══════════════════════════════ -->
<section id="pricing">
  <div class="container">
    <div class="section-head">
      <p class="section-label">Ceník</p>
      <h2 class="section-h2">Transparentní ceny</h2>
    </div>

    <div class="pricing-grid">

      <div class="price-card">
        {ICON_GRID}
        <h3 class="price-title">Byt do 50 m²</h3>
        <div class="price-amount">
          <span class="price-num">9&nbsp;200</span>
          <span class="price-unit">Kč</span>
        </div>
        <p class="price-note">od</p>
        <div class="price-divider"></div>
        <ul class="price-features">
          <li><span class="price-check">{ICON_CHECK}</span>Příprava povrchu</li>
          <li><span class="price-check">{ICON_CHECK}</span>2 vrstvy barvy</li>
          <li><span class="price-check">{ICON_CHECK}</span>Úklid</li>
          <li><span class="price-check">{ICON_CHECK}</span>Standardní materiál</li>
          <li><span class="price-check">{ICON_CHECK}</span>Doprava zdarma</li>
        </ul>
        <a href="#contact" class="price-btn dark">Nezávazně poptat</a>
      </div>

      <div class="price-card featured">
        <span class="price-badge">Nejoblíbenější</span>
        {ICON_HOME2}
        <h3 class="price-title">Rodinný dům</h3>
        <div class="price-amount">
          <span class="price-num">24&nbsp;900</span>
          <span class="price-unit">Kč</span>
        </div>
        <p class="price-note">od</p>
        <div class="price-divider"></div>
        <ul class="price-features">
          <li><span class="price-check">{ICON_CHECK}</span>Kompletní vymalování</li>
          <li><span class="price-check">{ICON_CHECK}</span>Příprava zdí</li>
          <li><span class="price-check">{ICON_CHECK}</span>Penetrace</li>
          <li><span class="price-check">{ICON_CHECK}</span>2 vrstvy barvy</li>
          <li><span class="price-check">{ICON_CHECK}</span>Úklid a materiál</li>
          <li><span class="price-check">{ICON_CHECK}</span>Doprava zdarma</li>
        </ul>
        <a href="#contact" class="price-btn green">Nezávazně poptat</a>
      </div>

      <div class="price-card">
        {ICON_BLDG2}
        <h3 class="price-title">Komerční prostor</h3>
        <div class="price-amount">
          <span class="price-num">85</span>
          <span class="price-unit">Kč/m²</span>
        </div>
        <p class="price-note">včetně materiálu</p>
        <div class="price-divider"></div>
        <ul class="price-features">
          <li><span class="price-check">{ICON_CHECK}</span>Velké plochy</li>
          <li><span class="price-check">{ICON_CHECK}</span>Rychlé termíny</li>
          <li><span class="price-check">{ICON_CHECK}</span>Kvalitní barvy</li>
          <li><span class="price-check">{ICON_CHECK}</span>Záruka 24 měsíců</li>
          <li><span class="price-check">{ICON_CHECK}</span>Úklid</li>
        </ul>
        <a href="#contact" class="price-btn dark">Nezávazně poptat</a>
      </div>

    </div>
    <p class="pricing-note">Každá zakázka je jedinečná. Cenu upřesníme po bezplatné obhlídce.</p>
  </div>
</section>

<!-- ═══════════════════════════════ FAQ ══════════════════════════════════ -->
<section id="faq">
  <div class="container">
    <div class="section-head">
      <p class="section-label">Časté dotazy</p>
      <h2 class="section-h2">Odpovědi na otázky</h2>
    </div>
    <div class="faq-inner">

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Jak dlouho trvá vymalování standardního bytu 2+1?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Standardní byt 2+1 (cca 55 m²) vymalujeme za 1–2 pracovní dny. Doba závisí na stavu povrchů a rozsahu přípravných prací. Přesný termín sdělíme po obhlídce.</p></div>
      </div>

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Používáte vlastní barvy nebo si máme obstarat vlastní?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Používáme kvalitní barvy renomovaných značek (Primalex, Dulux, Caparol). Cenu barvy zahrnujeme do kalkulace, ale pokud máte vlastní preference, rádi pracujeme s materiály, které si zajistíte sami.</p></div>
      </div>

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Jaký je rozsah vaší působnosti?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Působíme v Praze a okolí do vzdálenosti přibližně 50 km. Nejčastěji realizujeme zakázky v Praze 1–10, Karlštejn, Beroun, Kladno a okolí.</p></div>
      </div>

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Zajišťujete i úklid po malování?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Ano, úklid je standardní součástí našich služeb. Po dokončení práce uklidíme veškeré krytiny, odmontujeme ochranu a zanecháme prostor připravený k okamžitému používání.</p></div>
      </div>

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Jaká je záruka na vaše práce?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Na malířské práce poskytujeme záruku 24 měsíců. V případě jakéhokoli problému nás kontaktujte a obratem se postaráme o nápravu.</p></div>
      </div>

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Potřebuji vymalovat jen jednu místnost — je to možné?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Samozřejmě. Realizujeme zakázky všech rozsahů — od malé koupelny až po velké komerční prostory. Minimální cena za malou zakázku je od 4 500 Kč.</p></div>
      </div>

      <div class="faq-item">
        <button class="faq-btn">
          <span class="faq-q">Jak postupujete, když jsou zdi v špatném stavu?</span>
          <span class="faq-icon">{ICON_PLUS}</span>
        </button>
        <div class="faq-answer"><p>Nejprve provedeme kompletní assessment stavu zdí. Škrábeme staré nátěry, sádrujeme praskliny, provádíme penetraci a štukování. Všechny přípravné práce jsou součástí kalkulace.</p></div>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════ CONTACT ══════════════════════════════ -->
<section id="contact">
  <div class="contact-inner">
    <p class="contact-eyebrow contact-el">Kontakt</p>
    <h2 class="contact-h2 contact-el">Pojďme začít<br/>váš projekt</h2>
    <p class="contact-body contact-el">Zavolejte nebo napište — připravíme vám nezávaznou kalkulaci zdarma. Odpovídáme do 24 hodin.</p>

    <div class="contact-btns contact-el">
      <a href="tel:+420737171208" class="btn-contact-primary">
        {ICON_PHONE}
        <span>+420 737 171 208</span>
        {ICON_ARROW}
      </a>
      <a href="mailto:telvakmal@seznam.cz" class="btn-contact-secondary">
        {ICON_MAIL}
        <span>telvakmal@seznam.cz</span>
        {ICON_ARROW}
      </a>
    </div>

    <div class="contact-divider contact-el"></div>

    <div class="contact-meta contact-el">
      <div class="contact-meta-item">
        <p class="contact-meta-label">Adresa</p>
        <p class="contact-meta-value">Maňákova 753/20, Praha 14</p>
      </div>
      <div class="contact-meta-sep"></div>
      <div class="contact-meta-item">
        <p class="contact-meta-label">IČO</p>
        <p class="contact-meta-value">44292279</p>
      </div>
      <div class="contact-meta-sep"></div>
      <div class="contact-meta-item">
        <p class="contact-meta-label">Provozní doba</p>
        <p class="contact-meta-value">Po–Pá 7:00–18:00</p>
      </div>
    </div>

    <div class="contact-badges contact-el">
      <span class="badge">30+ let na trhu</span>
      <span class="badge">Záruka 24 měsíců</span>
      <span class="badge">IČO ověřeno</span>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ FOOTER ═══════════════════════════════ -->
<footer>
  <div class="footer-grid">
    <div>
      <p class="footer-brand">Malíři Profi</p>
      <p class="footer-sub">David Telvak</p>
      <p class="footer-desc">Profesionální malířské služby v Praze a okolí od roku 1992.</p>
      <div class="footer-contacts">
        <a href="tel:+420737171208">+420 737 171 208</a>
        <a href="mailto:telvakmal@seznam.cz">telvakmal@seznam.cz</a>
      </div>
    </div>
    <div>
      <p class="footer-col-head">Odkazy</p>
      <ul class="footer-col-links">
        <li><a href="#services">Služby</a></li>
        <li><a href="#process">Proces</a></li>
        <li><a href="#gallery">Realizace</a></li>
        <li><a href="#pricing">Ceník</a></li>
        <li><a href="#contact">Kontakt</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-col-head">Služby</p>
      <ul class="footer-col-links">
        <li><a href="#services">Malování bytů</a></li>
        <li><a href="#services">Malování domů</a></li>
        <li><a href="#services">Komerční prostory</a></li>
        <li><a href="#services">Renovace</a></li>
        <li><a href="#services">Lakýrnictví</a></li>
        <li><a href="#services">Úklid</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-col-head">Právní informace</p>
      <ul class="footer-col-links">
        <li><span>Ochrana osobních údajů</span></li>
        <li><span>Obchodní podmínky</span></li>
        <li><span>Cookies</span></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p class="footer-copy">&copy; 2025 Malíři Profi. IČO: 44292279.</p>
    <p class="footer-copy">Všechna práva vyhrazena.</p>
  </div>
</footer>

<!-- ═══════════════════════════════ FLOATING CTA ══════════════════════════ -->
<div id="float-mobile">
  <a href="tel:+420737171208" class="fm-call">
    {ICON_PHONE_S} Zavolat
  </a>
  <a href="#contact" class="fm-cta">Kalkulace zdarma</a>
</div>

<a href="tel:+420737171208" id="float-desktop" aria-label="Zavolat">
  {ICON_PHONE_S}
</a>

<!-- ═══════════════════════════════ SCRIPTS ══════════════════════════════ -->
<script src="./js/gsap.min.js"></script>
<script src="./js/ScrollTrigger.min.js"></script>
<script src="./js/script.js"></script>

</body>
</html>
"""

index_path = f"{BUILD_DIR}/index.html"
with open(index_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Wrote index.html ({len(HTML)//1024}KB)")

# ══════════════════════════════════════════════════════════════════════════
# 404 page
# ══════════════════════════════════════════════════════════════════════════
PAGE404 = """<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>404 – Stránka nenalezena | Malíři Profi Praha</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="./css/style.css"/>
  <style>
    body { display:flex; align-items:center; justify-content:center; min-height:100vh; text-align:center; padding: 40px 20px; }
    .e404-wrap { max-width:560px; }
    .e404-label { font-size:12px; text-transform:uppercase; letter-spacing:.12em; color:#5F6F65; margin-bottom:24px; }
    .e404-h1 { font-family:'Playfair Display',serif; font-size:clamp(48px,8vw,80px); color:#111111; line-height:1; margin-bottom:24px; font-weight:500; }
    .e404-body { font-size:16px; color:#4A4A4A; margin-bottom:40px; line-height:1.6; }
  </style>
</head>
<body>
  <div class="e404-wrap">
    <p class="e404-label">Chyba 404</p>
    <h1 class="e404-h1">Stránka<br/>nenalezena</h1>
    <p class="e404-body">Tato stránka neexistuje nebo byla přesunuta. Vraťte se na hlavní stránku.</p>
    <a href="./index.html" class="btn-primary" style="display:inline-flex;">Zpět na hlavní stránku</a>
  </div>
</body>
</html>
"""
with open(f"{BUILD_DIR}/404.html", "w", encoding="utf-8") as f:
    f.write(PAGE404)
print("Wrote 404.html")

# ── .htaccess ──────────────────────────────────────────────────────────────
HTACCESS = """Options -Indexes
AddDefaultCharset UTF-8
AddType text/css                 .css
AddType application/javascript   .js
AddType image/jpeg               .jpg .jpeg
AddType image/png                .png
AddType image/webp               .webp
AddType image/svg+xml            .svg
ErrorDocument 404 /404.html
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html              "access plus 0 seconds"
  ExpiresByType text/css               "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/jpeg             "access plus 1 month"
  ExpiresByType image/png              "access plus 1 month"
</IfModule>
"""
with open(f"{BUILD_DIR}/.htaccess", "w") as f:
    f.write(HTACCESS)
print("Wrote .htaccess")

# ── ZIP ────────────────────────────────────────────────────────────────────
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(BUILD_DIR):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, BUILD_DIR)
            zf.write(abs_path, rel_path)

print(f"\nZIP: {ZIP_PATH}  ({os.path.getsize(ZIP_PATH)//1024} KB)")
print("\nContents:")
with zipfile.ZipFile(ZIP_PATH) as zf:
    for n in sorted(zf.namelist()):
        print(f"  {n}")
