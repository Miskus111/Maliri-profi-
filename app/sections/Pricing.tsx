"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { LayoutGrid, Home, Building2, Check } from "lucide-react";

gsap.registerPlugin(ScrollTrigger);

const plans = [
  {
    icon: LayoutGrid,
    title: "Byt do 50 m²",
    price: "9 200",
    unit: "Kč",
    note: "od",
    features: [
      "Příprava povrchu",
      "2 vrstvy barvy",
      "Úklid",
      "Standardní materiál",
      "Doprava zdarma",
    ],
    featured: false,
  },
  {
    icon: Home,
    title: "Rodinný dům",
    price: "24 900",
    unit: "Kč",
    note: "od",
    features: [
      "Kompletní vymalování",
      "Příprava zdí",
      "Penetrace",
      "2 vrstvy barvy",
      "Úklid a materiál",
      "Doprava zdarma",
    ],
    featured: true,
  },
  {
    icon: Building2,
    title: "Komerční prostor",
    price: "85",
    unit: "Kč/m²",
    note: "včetně materiálu",
    features: [
      "Velké plochy",
      "Rychlé termíny",
      "Kvalitní barvy",
      "Záruka 24 měsíců",
      "Úklid",
    ],
    featured: false,
  },
];

export default function Pricing() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    const ctx = gsap.context(() => {
      gsap.fromTo(
        sectionRef.current!.querySelectorAll(".price-card"),
        { opacity: 0, y: 50 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          stagger: 0.12,
          ease: "power3.out",
          scrollTrigger: { trigger: sectionRef.current, start: "top 75%" },
        }
      );
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  return (
    <section
      id="pricing"
      ref={sectionRef}
      className="w-full py-24 lg:py-36 px-5 lg:px-10 bg-[#FAFAF7]"
    >
      <div className="max-w-[1280px] mx-auto">
        <div className="text-center max-w-[520px] mx-auto mb-16 lg:mb-24">
          <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-4">
            Ceník
          </p>
          <h2 className="font-display text-[32px] sm:text-[44px] lg:text-[60px] leading-[1.0] tracking-[-0.02em] text-[#1F1F1F]">
            Transparentní ceny
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-5 lg:gap-6">
          {plans.map((p) => (
            <div
              key={p.title}
              className={`price-card relative bg-[#FFFFFF] rounded-3xl p-8 lg:p-10 text-center shadow-[0_1px_3px_rgba(0,0,0,0.04)] ${
                p.featured ? "ring-2 ring-[#5F6F65]" : ""
              }`}
            >
              {p.featured && (
                <span className="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#5F6F65] text-white font-body font-medium text-[11px] uppercase tracking-wider px-4 py-1 rounded-full">
                  Nejoblíbenější
                </span>
              )}

              <p.icon
                size={44}
                className="text-[#5F6F65] mx-auto"
                strokeWidth={1.5}
              />
              <h3 className="font-body font-medium text-[18px] text-[#1F1F1F] mt-5">
                {p.title}
              </h3>

              <div className="mt-4">
                <span className="font-display text-[52px] lg:text-[56px] text-[#1F1F1F] leading-none">
                  {p.price}
                </span>
                <span className="font-body text-[16px] text-[#6B6B6B] ml-1">
                  {p.unit}
                </span>
              </div>
              <p className="font-body font-light text-[13px] text-[#6B6B6B] mt-1">
                {p.note}
              </p>

              <div className="w-full h-px bg-[#E1E0DC] my-7" />

              <ul className="space-y-3 text-left max-w-[240px] mx-auto">
                {p.features.map((f) => (
                  <li key={f} className="flex items-start gap-3">
                    <Check
                      size={15}
                      className="text-[#5F6F65] mt-0.5 flex-shrink-0"
                    />
                    <span className="font-body font-light text-[14px] text-[#6B6B6B]">
                      {f}
                    </span>
                  </li>
                ))}
              </ul>

              <a
                href="#contact"
                onClick={(e) => {
                  e.preventDefault();
                  document
                    .querySelector("#contact")
                    ?.scrollIntoView({ behavior: "smooth" });
                }}
                className={`block mt-8 w-full font-body font-medium text-[14px] py-3.5 rounded-full transition-colors duration-200 ${
                  p.featured
                    ? "bg-[#5F6F65] text-white hover:bg-[#4A5A50]"
                    : "bg-[#1F1F1F] text-white hover:bg-black"
                }`}
              >
                Nezávazně poptat
              </a>
            </div>
          ))}
        </div>

        <p className="font-body font-light text-[14px] text-[#6B6B6B] text-center mt-10">
          Každá zakázka je jedinečná. Cenu upřesníme po bezplatné obhlídce.
        </p>
      </div>
    </section>
  );
}
