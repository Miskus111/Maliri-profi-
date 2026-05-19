"use client";

import { Phone } from "lucide-react";

export default function FloatingCTA() {
  return (
    <>
      <div className="fixed bottom-0 left-0 right-0 z-40 bg-[#FAFAF7]/95 backdrop-blur-md border-t border-[#E1E0DC]/60 p-3 flex gap-2.5 lg:hidden">
        <a
          href="tel:+420737171208"
          className="flex-1 flex items-center justify-center gap-2 bg-[#5F6F65] text-white font-body font-medium text-[13px] py-3 rounded-full"
        >
          <Phone size={15} />
          Zavolat
        </a>
        <a
          href="#contact"
          onClick={(e) => {
            e.preventDefault();
            document
              .querySelector("#contact")
              ?.scrollIntoView({ behavior: "smooth" });
          }}
          className="flex-1 flex items-center justify-center bg-[#1F1F1F] text-white font-body font-medium text-[13px] py-3 rounded-full"
        >
          Kalkulace zdarma
        </a>
      </div>

      <a
        href="tel:+420737171208"
        className="fixed bottom-6 right-6 z-40 w-12 h-12 bg-[#5F6F65] text-white rounded-full flex items-center justify-center shadow-lg hover:bg-[#4A5A50] hover:scale-105 transition-all duration-200 hidden lg:flex"
        aria-label="Zavolat"
      >
        <Phone size={20} />
      </a>
    </>
  );
}
