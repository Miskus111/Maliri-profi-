"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { REAL_IMAGES } from "./Hero";

gsap.registerPlugin(ScrollTrigger);

const steps = [
  {
    num: "01",
    title: "Bezplatná konzultace a kalkulace",
    desc: "Přijedeme na obhlídku, posoudíme rozsah prací a připravíme nezávaznou cenovou nabídku na míru. Bez skrytých poplatků.",
    img: REAL_IMAGES[1],
  },
  {
    num: "02",
    title: "Profesionální příprava",
    desc: "Zakryjeme podlahy, odmontujeme zásuvky, opravíme nedokonalosti zdí, provedeme penetraci a štukování.",
    img: REAL_IMAGES[2],
  },
  {
    num: "03",
    title: "Precizní realizace",
    desc: "Nanášíme kvalitní barvy renomovaných značek dvěma vrstvami. Pracujeme čistě, efektivně a s ohledem na váš režim.",
    img: REAL_IMAGES[3],
  },
  {
    num: "04",
    title: "Úklid a předání",
    desc: "Po dokončení uklidíme, namontujeme zpět veškeré kryty a předáme vám dokonale vymalovaný prostor.",
    img: REAL_IMAGES[4],
  },
];

export default function Process() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    const ctx = gsap.context(() => {
      sectionRef.current!.querySelectorAll(".process-step").forEach((el, i) => {
        const isEven = i % 2 === 0;
        gsap.fromTo(
          el,
          { opacity: 0, x: isEven ? -40 : 40 },
          {
            opacity: 1,
            x: 0,
            duration: 0.9,
            ease: "power3.out",
            scrollTrigger: { trigger: el, start: "top 80%" },
          }
        );
      });
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  return (
    <section
      id="process"
      ref={sectionRef}
      className="w-full py-24 lg:py-36 px-5 lg:px-10 bg-[#F2F1ED]"
    >
      <div className="max-w-[1280px] mx-auto">
        <div className="max-w-[600px] mb-16 lg:mb-24">
          <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-4">
            Jak to funguje
          </p>
          <h2 className="font-display text-[32px] sm:text-[44px] lg:text-[60px] leading-[1.0] tracking-[-0.02em] text-[#1F1F1F]">
            Od konzultace po předání
          </h2>
        </div>

        <div className="flex flex-col gap-16 lg:gap-24">
          {steps.map((step, i) => (
            <div
              key={step.num}
              className="process-step grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 items-center"
            >
              <div className={i % 2 === 1 ? "lg:order-2" : ""}>
                <div className="rounded-2xl overflow-hidden">
                  <img
                    src={step.img}
                    alt={step.title}
                    className="w-full aspect-[4/5] object-cover hover:scale-[1.03] transition-transform duration-700"
                    loading="lazy"
                  />
                </div>
              </div>
              <div
                className={`flex flex-col justify-center ${
                  i % 2 === 1 ? "lg:order-1 lg:pr-10" : "lg:pl-10"
                }`}
              >
                <span className="font-display text-[72px] lg:text-[96px] leading-none text-[#D8CEC2]">
                  {step.num}
                </span>
                <h3 className="font-display text-[24px] lg:text-[32px] leading-[1.15] text-[#1F1F1F] mt-2 mb-4">
                  {step.title}
                </h3>
                <p className="font-body font-light text-[15px] text-[#6B6B6B] leading-[1.7] max-w-[400px]">
                  {step.desc}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
