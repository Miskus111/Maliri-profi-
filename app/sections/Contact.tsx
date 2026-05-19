"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { Phone, Mail, ArrowRight } from "lucide-react";

gsap.registerPlugin(ScrollTrigger);

export default function Contact() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    const ctx = gsap.context(() => {
      gsap.fromTo(
        sectionRef.current!.querySelectorAll(".contact-el"),
        { opacity: 0, y: 30 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          stagger: 0.1,
          ease: "power3.out",
          scrollTrigger: {
            trigger: sectionRef.current,
            start: "top 75%",
          },
        }
      );
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  return (
    <section
      id="contact"
      ref={sectionRef}
      className="w-full py-28 lg:py-44 px-5 lg:px-10 bg-[#FAFAF7]"
    >
      <div className="max-w-[680px] mx-auto text-center">
        <p className="contact-el font-body text-[12px] uppercase tracking-[0.14em] text-[#5F6F65] mb-5">
          Kontakt
        </p>

        <h2 className="contact-el font-display text-[40px] sm:text-[52px] lg:text-[68px] leading-[0.98] tracking-[-0.025em] text-[#1F1F1F]">
          Pojďme začít
          <br />
          váš projekt
        </h2>

        <p className="contact-el font-body font-light text-[16px] lg:text-[18px] text-[#6B6B6B] leading-[1.65] mt-6 max-w-[460px] mx-auto">
          Zavolejte nebo napište — připravíme vám nezávaznou kalkulaci zdarma.
          Odpovídáme do 24 hodin.
        </p>

        <div className="contact-el flex flex-col sm:flex-row items-center justify-center gap-3 mt-10">
          <a
            href="tel:+420737171208"
            className="group w-full sm:w-auto inline-flex items-center justify-center gap-2.5 bg-[#5F6F65] text-white font-body font-medium text-[14px] px-8 py-4 rounded-full hover:bg-[#4A5A50] hover:shadow-lg hover:shadow-[#5F6F65]/15 hover:-translate-y-0.5 transition-all duration-300"
          >
            <Phone size={17} />
            <span>+420 737 171 208</span>
            <ArrowRight
              size={15}
              className="text-white/50 group-hover:text-white group-hover:translate-x-0.5 transition-all duration-200"
            />
          </a>
          <a
            href="mailto:telvakmal@seznam.cz"
            className="group w-full sm:w-auto inline-flex items-center justify-center gap-2.5 border border-[#1F1F1F] text-[#1F1F1F] font-body font-medium text-[14px] px-8 py-4 rounded-full hover:bg-[#1F1F1F] hover:text-white hover:-translate-y-0.5 transition-all duration-300"
          >
            <Mail size={17} />
            <span>telvakmal@seznam.cz</span>
            <ArrowRight
              size={15}
              className="text-[#6B6B6B] group-hover:text-white group-hover:translate-x-0.5 transition-all duration-200"
            />
          </a>
        </div>

        <div className="contact-el w-12 h-px bg-[#E1E0DC] mx-auto mt-14" />

        <div className="contact-el flex flex-wrap items-center justify-center gap-x-8 gap-y-3 mt-10">
          <div className="text-center">
            <p className="font-body text-[10px] uppercase tracking-[0.1em] text-[#6B6B6B] mb-0.5">
              Adresa
            </p>
            <p className="font-body font-light text-[13px] text-[#1F1F1F]">
              Maňákova 753/20, Praha 14
            </p>
          </div>
          <div className="w-px h-6 bg-[#E1E0DC] hidden sm:block" />
          <div className="text-center">
            <p className="font-body text-[10px] uppercase tracking-[0.1em] text-[#6B6B6B] mb-0.5">
              IČO
            </p>
            <p className="font-body font-light text-[13px] text-[#1F1F1F]">
              44292279
            </p>
          </div>
          <div className="w-px h-6 bg-[#E1E0DC] hidden sm:block" />
          <div className="text-center">
            <p className="font-body text-[10px] uppercase tracking-[0.1em] text-[#6B6B6B] mb-0.5">
              Provozní doba
            </p>
            <p className="font-body font-light text-[13px] text-[#1F1F1F]">
              Po–Pá 7:00–18:00
            </p>
          </div>
        </div>

        <div className="contact-el flex flex-wrap items-center justify-center gap-2.5 mt-10">
          {["30+ let na trhu", "Záruka 24 měsíců", "IČO ověřeno"].map(
            (badge) => (
              <span
                key={badge}
                className="font-body text-[12px] bg-[#F2F1ED] text-[#6B6B6B] px-3.5 py-1.5 rounded-full"
              >
                {badge}
              </span>
            )
          )}
        </div>
      </div>
    </section>
  );
}
