"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";

export const REAL_IMAGES = [
  "/images/img-00.jpg",
  "/images/img-01.jpg",
  "/images/img-02.jpg",
  "/images/img-03.jpg",
  "/images/img-04.jpg",
  "/images/img-05.jpg",
  "/images/img-06.jpg",
  "/images/img-07.jpg",
  "/images/img-08.jpg",
  "/images/img-09.jpg",
  "/images/img-10.jpg",
  "/images/img-11.jpg",
  "/images/img-12.jpg",
  "/images/img-13.jpg",
  "/images/img-14.jpg",
  "/images/img-15.jpg",
  "/images/img-16.jpg",
  "/images/img-17.jpg",
  "/images/img-18.jpg",
  "/images/img-19.jpg",
  "/images/img-20.jpg",
  "/images/img-21.jpg",
  "/images/img-22.jpg",
  "/images/img-23.jpg",
  "/images/img-24.jpg",
];

export default function Hero() {
  const contentRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!contentRef.current) return;
    const els = contentRef.current.children;
    gsap.fromTo(
      els,
      { opacity: 0, y: 30 },
      {
        opacity: 1,
        y: 0,
        duration: 0.9,
        stagger: 0.12,
        ease: "power3.out",
        delay: 0.3,
      }
    );
  }, []);

  return (
    <section
      id="hero"
      className="relative w-full min-h-[100dvh] flex items-end lg:items-center overflow-hidden"
    >
      <div className="absolute inset-0">
        <img
          src="/images/img-21.jpg"
          alt="Malířské práce Praha"
          className="w-full h-full object-cover object-center"
        />
        <div
          className="absolute inset-0"
          style={{
            background:
              "linear-gradient(180deg, rgba(242,241,237,0.82) 0%, rgba(242,241,237,0.60) 35%, rgba(242,241,237,0.38) 65%, rgba(242,241,237,0.88) 100%)",
          }}
        />
      </div>

      <div className="relative z-10 w-full max-w-[1280px] mx-auto px-5 lg:px-10 pb-16 pt-32 lg:py-0">
        <div ref={contentRef} className="max-w-[640px]">
          <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-5">
            Profesionální malířské služby v Praze od roku 1992
          </p>

          <h1 className="font-display text-[42px] sm:text-[56px] lg:text-[80px] leading-[0.95] tracking-[-0.025em] text-[#111111]">
            Precizní malířské práce, na které se můžete spolehnout
          </h1>

          <p className="font-body text-base lg:text-lg text-[#242424] leading-[1.65] max-w-[420px] mt-6">
            Malování bytů, domů a kanceláří v Praze a okolí. Třicet let
            zkušeností, čistá práce, férové ceny.
          </p>

          <div className="flex flex-col sm:flex-row gap-3 mt-10">
            <a
              href="#contact"
              onClick={(e) => {
                e.preventDefault();
                document
                  .querySelector("#contact")
                  ?.scrollIntoView({ behavior: "smooth" });
              }}
              className="font-body font-medium text-[14px] bg-[#5F6F65] text-white px-7 py-3.5 rounded-full hover:bg-[#4A5A50] transition-colors duration-200 text-center"
            >
              Nezávazná kalkulace zdarma
            </a>
            <a
              href="tel:+420737171208"
              className="font-body font-medium text-[14px] border border-[#111111] text-[#111111] px-7 py-3.5 rounded-full hover:bg-[#111111] hover:text-white transition-all duration-200 text-center"
            >
              Zavolat nyní
            </a>
          </div>

          <div className="flex flex-wrap gap-8 mt-14">
            {[
              { num: "30+", label: "let zkušeností" },
              { num: "500+", label: "realizací" },
              { num: "50 km", label: "okolí Prahy" },
            ].map((s) => (
              <div key={s.label}>
                <p className="font-display text-[28px] lg:text-[32px] leading-none text-[#111111]">
                  {s.num}
                </p>
                <p className="font-body text-[13px] text-[#4A4A4A] mt-1">
                  {s.label}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
