"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { Paintbrush, Home, Building2, Sparkles, ArrowUpRight } from "lucide-react";

gsap.registerPlugin(ScrollTrigger);

const services = [
  {
    icon: Paintbrush,
    title: "Malování bytů a domů",
    description:
      "Kompletní vymalování bytů všech velikostí i rodinných domů. Od přípravy povrchu až po finální úklid.",
  },
  {
    icon: Home,
    title: "Renovace interiérů",
    description:
      "Škrábání starých nátěrů, penetrace, opravy zdí a štukování. Příprava pro dokonalý výsledek.",
  },
  {
    icon: Building2,
    title: "Komerční prostory",
    description:
      "Malování kanceláří, obchodů a firemních prostor. Rychlé termíny, minimální omezení provozu.",
  },
  {
    icon: Sparkles,
    title: "Specializované práce",
    description:
      "Dekorativní malby, lakování nábytku, míchání barev na míru, tapetování a úklid po malování.",
  },
];

export default function Services() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    const ctx = gsap.context(() => {
      gsap.fromTo(
        sectionRef.current!.querySelectorAll(".service-card"),
        { opacity: 0, y: 50 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          stagger: 0.1,
          ease: "power3.out",
          scrollTrigger: { trigger: sectionRef.current, start: "top 78%" },
        }
      );
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  return (
    <section
      id="services"
      ref={sectionRef}
      className="w-full py-24 lg:py-36 px-5 lg:px-10 bg-[#FAFAF7]"
    >
      <div className="max-w-[1280px] mx-auto">
        <div className="max-w-[600px] mb-16 lg:mb-24">
          <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-4">
            Naše služby
          </p>
          <h2 className="font-display text-[32px] sm:text-[44px] lg:text-[60px] leading-[1.0] tracking-[-0.02em] text-[#111111]">
            Kompletní malířské řešení
          </h2>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6">
          {services.map((s) => (
            <div
              key={s.title}
              className="service-card group bg-[#FFFFFF] rounded-2xl p-7 lg:p-8 shadow-[0_1px_3px_rgba(0,0,0,0.04)] hover:bg-[#5F6F65] hover:shadow-lg transition-all duration-400 cursor-default"
            >
              <s.icon
                size={36}
                className="text-[#5F6F65] group-hover:text-white transition-colors duration-400"
                strokeWidth={1.5}
              />
              <h3 className="font-body font-semibold text-[17px] text-[#111111] group-hover:text-white mt-6 mb-2 transition-colors duration-400">
                {s.title}
              </h3>
              <p className="font-body text-[14px] text-[#242424] group-hover:text-white/85 leading-[1.6] transition-colors duration-400">
                {s.description}
              </p>
              <div className="mt-6 pt-5 border-t border-[#E3E1DC] group-hover:border-white/20 transition-colors duration-400">
                <a
                  href="#contact"
                  onClick={(e) => {
                    e.preventDefault();
                    document
                      .querySelector("#contact")
                      ?.scrollIntoView({ behavior: "smooth" });
                  }}
                  className="inline-flex items-center gap-1.5 font-body font-medium text-[13px] text-[#5F6F65] group-hover:text-white transition-colors duration-400"
                >
                  Zjistit více{" "}
                  <ArrowUpRight
                    size={14}
                    className="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-200"
                  />
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
