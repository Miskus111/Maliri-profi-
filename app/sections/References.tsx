"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { Star, ChevronLeft, ChevronRight } from "lucide-react";

gsap.registerPlugin(ScrollTrigger);

const testimonials = [
  {
    name: "Jana K.",
    loc: "Praha 2",
    text: "Pan Telvak a jeho tým odvedli skvělou práci. Vymalovali celý náš byt za 2 dny, vše uklidili a výsledek předčil očekávání. Profesionální přístup od začátku do konce.",
  },
  {
    name: "Martin P.",
    loc: "Praha 6",
    text: "Už jsem vyzkoušel několik malířů, ale tihle jsou jiná liga. Precizní práce, čistota, dochvilnost. Cena byla přesně podle dohody. Doporučuji všem.",
  },
  {
    name: "Lenka S.",
    loc: "Praha 10",
    text: "Potřebovali jsme rychle vymalovat kancelář před otevřením nové pobočky. Termín dodrželi, cena byla férová a kvalita výborná. Budeme spolupracovat i nadále.",
  },
  {
    name: "Petr D.",
    loc: "Praha 8",
    text: "Vymalování starého bytu po babičce — škrábání starých maleb, opravy zdí, penetrace. Dnes to vypadá jako nový byt. Obrovské díky za trpělivost a preciznost.",
  },
  {
    name: "Kateřina N.",
    loc: "Praha 4",
    text: "Neuvěřitelná proměna našeho domu. Exteriér i interiér, všechno dokonale sladěné. Komunikace byla výborná, vždy věděli, co se děje a kdy.",
  },
  {
    name: "Tomáš H.",
    loc: "Praha 3",
    text: "Malování dětského pokoje s dekorativní malbou. Syn je nadšený, výsledek je úžasný. Kreativní přístup a dokonalé provedení.",
  },
];

export default function References() {
  const sectionRef = useRef<HTMLElement>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    const ctx = gsap.context(() => {
      gsap.fromTo(
        sectionRef.current!.querySelectorAll(".ref-card"),
        { opacity: 0, x: 40 },
        {
          opacity: 1,
          x: 0,
          duration: 0.8,
          stagger: 0.08,
          ease: "power3.out",
          scrollTrigger: { trigger: sectionRef.current, start: "top 75%" },
        }
      );
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  const scroll = (dir: "left" | "right") => {
    scrollRef.current?.scrollBy({
      left: dir === "left" ? -460 : 460,
      behavior: "smooth",
    });
  };

  return (
    <section
      id="references"
      ref={sectionRef}
      className="w-full py-24 lg:py-36 bg-[#F6F5F1]"
    >
      <div className="max-w-[1280px] mx-auto px-5 lg:px-10">
        <div className="flex items-end justify-between mb-12 lg:mb-16">
          <div className="max-w-[500px]">
            <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-4">
              Reference
            </p>
            <h2 className="font-display text-[32px] sm:text-[44px] lg:text-[60px] leading-[1.0] tracking-[-0.02em] text-[#111111]">
              Co říkají naši zákazníci
            </h2>
          </div>
          <div className="hidden lg:flex gap-2">
            <button
              onClick={() => scroll("left")}
              className="w-10 h-10 rounded-full border border-[#E3E1DC] flex items-center justify-center text-[#4A4A4A] hover:border-[#5F6F65] hover:text-[#5F6F65] transition-colors"
            >
              <ChevronLeft size={18} />
            </button>
            <button
              onClick={() => scroll("right")}
              className="w-10 h-10 rounded-full border border-[#E3E1DC] flex items-center justify-center text-[#4A4A4A] hover:border-[#5F6F65] hover:text-[#5F6F65] transition-colors"
            >
              <ChevronRight size={18} />
            </button>
          </div>
        </div>
      </div>

      <div
        ref={scrollRef}
        className="flex gap-4 lg:gap-5 overflow-x-auto scrollbar-hide scroll-snap-x pl-5 lg:pl-10 pr-5"
      >
        {testimonials.map((t, i) => (
          <div
            key={i}
            className="ref-card scroll-snap-start flex-shrink-0 w-[320px] lg:w-[420px] bg-[#FFFFFF] rounded-2xl p-7 lg:p-9 shadow-[0_1px_3px_rgba(0,0,0,0.04)] border border-[#E3E1DC]/60"
          >
            <div className="flex gap-0.5">
              {[...Array(5)].map((_, j) => (
                <Star
                  key={j}
                  size={15}
                  className="fill-amber-500 text-amber-500"
                />
              ))}
            </div>
            <p className="font-body text-[15px] lg:text-[16px] text-[#242424] leading-[1.7] mt-6">
              {t.text}
            </p>
            <div className="mt-8 pt-5 border-t border-[#E3E1DC]/60">
              <p className="font-body font-semibold text-[14px] text-[#111111]">
                {t.name}
              </p>
              <p className="font-body text-[13px] text-[#5A5A5A]">
                {t.loc}
              </p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
