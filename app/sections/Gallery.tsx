"use client";

import { useEffect, useRef, useState } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { REAL_IMAGES } from "./Hero";
import { X, ChevronLeft, ChevronRight } from "lucide-react";

gsap.registerPlugin(ScrollTrigger);

const galleryImages = REAL_IMAGES.slice(5);

export default function Gallery() {
  const sectionRef = useRef<HTMLElement>(null);
  const gridRef = useRef<HTMLDivElement>(null);
  const [openIdx, setOpenIdx] = useState<number | null>(null);

  useEffect(() => {
    if (!sectionRef.current || !gridRef.current) return;
    const ctx = gsap.context(() => {
      gsap.fromTo(
        gridRef.current!.children,
        { opacity: 0, y: 30, scale: 0.97 },
        {
          opacity: 1,
          y: 0,
          scale: 1,
          duration: 0.7,
          stagger: 0.06,
          ease: "power3.out",
          scrollTrigger: { trigger: gridRef.current, start: "top 80%" },
        }
      );
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  useEffect(() => {
    if (openIdx !== null) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [openIdx]);

  const prev = () =>
    setOpenIdx((p) =>
      p === null || p === 0 ? galleryImages.length - 1 : p - 1
    );
  const next = () =>
    setOpenIdx((p) =>
      p === null || p === galleryImages.length - 1 ? 0 : p + 1
    );

  return (
    <>
      <section
        id="gallery"
        ref={sectionRef}
        className="w-full py-24 lg:py-36 px-5 lg:px-10 bg-[#FAFAF7]"
      >
        <div className="max-w-[1280px] mx-auto">
          <div className="max-w-[600px] mb-16 lg:mb-24">
            <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-4">
              Realizace
            </p>
            <h2 className="font-display text-[32px] sm:text-[44px] lg:text-[60px] leading-[1.0] tracking-[-0.02em] text-[#1F1F1F]">
              Ukázky naší práce
            </h2>
          </div>

          <div ref={gridRef} className="columns-2 md:columns-3 gap-3 lg:gap-4">
            {galleryImages.map((src, i) => (
              <div
                key={src}
                className="break-inside-avoid mb-3 lg:mb-4 rounded-xl overflow-hidden cursor-pointer group"
                onClick={() => setOpenIdx(i)}
              >
                <img
                  src={src}
                  alt=""
                  className="w-full object-cover group-hover:scale-[1.04] transition-transform duration-700 ease-out"
                  loading="lazy"
                />
              </div>
            ))}
          </div>
        </div>
      </section>

      {openIdx !== null && (
        <div
          className="fixed inset-0 z-50 bg-black/95 flex items-center justify-center"
          onClick={() => setOpenIdx(null)}
        >
          <button
            className="absolute top-5 right-5 text-white/60 hover:text-white z-10"
            onClick={() => setOpenIdx(null)}
          >
            <X size={28} />
          </button>
          <button
            className="absolute left-4 top-1/2 -translate-y-1/2 text-white/40 hover:text-white z-10 hidden sm:block"
            onClick={(e) => {
              e.stopPropagation();
              prev();
            }}
          >
            <ChevronLeft size={36} />
          </button>
          <button
            className="absolute right-4 top-1/2 -translate-y-1/2 text-white/40 hover:text-white z-10 hidden sm:block"
            onClick={(e) => {
              e.stopPropagation();
              next();
            }}
          >
            <ChevronRight size={36} />
          </button>
          <div
            className="max-w-[90vw] max-h-[88vh]"
            onClick={(e) => e.stopPropagation()}
          >
            <img
              src={galleryImages[openIdx]}
              alt=""
              className="max-w-full max-h-[88vh] object-contain rounded-sm"
            />
          </div>
        </div>
      )}
    </>
  );
}
