"use client";

import { useEffect, useState } from "react";
import { Phone, Menu, X } from "lucide-react";

const navLinks = [
  { label: "Služby", href: "#services" },
  { label: "Proces", href: "#process" },
  { label: "Realizace", href: "#gallery" },
  { label: "Ceník", href: "#pricing" },
  { label: "Kontakt", href: "#contact" },
];

export default function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [hidden, setHidden] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [lastScrollY, setLastScrollY] = useState(0);

  useEffect(() => {
    const onScroll = () => {
      const y = window.scrollY;
      setScrolled(y > 80);
      if (y > lastScrollY && y > 200) setHidden(true);
      else setHidden(false);
      setLastScrollY(y);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, [lastScrollY]);

  const scrollTo = (href: string) => {
    setMobileOpen(false);
    document.querySelector(href)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <>
      <nav
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          hidden ? "-translate-y-full" : "translate-y-0"
        } ${
          scrolled
            ? "bg-[#F6F5F1]/90 backdrop-blur-xl shadow-[0_1px_0_rgba(0,0,0,0.04)]"
            : "bg-transparent"
        }`}
      >
        <div className="max-w-[1280px] mx-auto h-16 lg:h-20 flex items-center justify-between px-5 lg:px-10">
          <a
            href="#"
            onClick={(e) => {
              e.preventDefault();
              window.scrollTo({ top: 0, behavior: "smooth" });
            }}
            className="font-body font-medium text-[15px] tracking-tight text-[#111111]"
          >
            Malíři Profi
          </a>

          <div className="hidden lg:flex items-center gap-9">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                onClick={(e) => {
                  e.preventDefault();
                  scrollTo(link.href);
                }}
                className="font-body text-[13px] tracking-[0.06em] text-[#4A4A4A] hover:text-[#111111] transition-colors duration-200"
              >
                {link.label}
              </a>
            ))}
          </div>

          <div className="flex items-center gap-3">
            <a
              href="#contact"
              onClick={(e) => {
                e.preventDefault();
                scrollTo("#contact");
              }}
              className="hidden sm:inline-flex font-body font-medium text-[13px] bg-[#5F6F65] text-white px-5 py-2.5 rounded-full hover:bg-[#4A5A50] transition-colors duration-200"
            >
              Kalkulace zdarma
            </a>
            <a
              href="tel:+420737171208"
              className="hidden md:flex w-9 h-9 rounded-full border border-[#E3E1DC] items-center justify-center text-[#4A4A4A] hover:border-[#5F6F65] hover:text-[#5F6F65] transition-colors"
            >
              <Phone size={15} />
            </a>
            <button
              className="lg:hidden w-9 h-9 flex items-center justify-center text-[#111111]"
              onClick={() => setMobileOpen(!mobileOpen)}
            >
              {mobileOpen ? <X size={22} /> : <Menu size={22} />}
            </button>
          </div>
        </div>
      </nav>

      {mobileOpen && (
        <div className="fixed inset-0 z-40 lg:hidden">
          <div
            className="absolute inset-0 bg-black/20 backdrop-blur-sm"
            onClick={() => setMobileOpen(false)}
          />
          <div className="absolute top-16 left-0 right-0 bg-[#F6F5F1]/95 backdrop-blur-xl border-b border-[#E3E1DC]/60 p-6 flex flex-col gap-1">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                onClick={(e) => {
                  e.preventDefault();
                  scrollTo(link.href);
                }}
                className="font-body text-[15px] text-[#111111] py-3 px-2 hover:text-[#5F6F65] transition-colors"
              >
                {link.label}
              </a>
            ))}
            <a
              href="tel:+420737171208"
              className="mt-3 font-body font-medium text-[13px] bg-[#5F6F65] text-white px-5 py-3 rounded-full text-center"
            >
              Zavolat: +420 737 171 208
            </a>
          </div>
        </div>
      )}
    </>
  );
}
