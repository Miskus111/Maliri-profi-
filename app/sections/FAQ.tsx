"use client";

import { useEffect, useRef, useState } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { Plus } from "lucide-react";

gsap.registerPlugin(ScrollTrigger);

const items = [
  {
    q: "Jak dlouho trvá vymalování standardního bytu 2+1?",
    a: "Standardní byt 2+1 (cca 55 m²) vymalujeme za 1–2 pracovní dny. Doba závisí na stavu povrchů a rozsahu přípravných prací. Přesný termín sdělíme po obhlídce.",
  },
  {
    q: "Používáte vlastní barvy nebo si máme obstarat vlastní?",
    a: "Používáme kvalitní barvy renomovaných značek (Primalex, Dulux, Caparol). Cenu barvy zahrnujeme do kalkulace, ale pokud máte vlastní preference, rádi pracujeme s materiály, které si zajistíte sami.",
  },
  {
    q: "Jaký je rozsah vaší působnosti?",
    a: "Působíme v Praze a okolí do vzdálenosti přibližně 50 km. Nejčastěji realizujeme zakázky v Praze 1–10, Karlštejn, Beroun, Kladno a okolí.",
  },
  {
    q: "Zajišťujete i úklid po malování?",
    a: "Ano, úklid je standardní součástí našich služeb. Po dokončení práce uklidíme veškeré krytiny, odmontujeme ochranu a zanecháme prostor připravený k okamžitému používání.",
  },
  {
    q: "Jaká je záruka na vaše práce?",
    a: "Na malířské práce poskytujeme záruku 24 měsíců. V případě jakéhokoli problému nás kontaktujte a obratem se postaráme o nápravu.",
  },
  {
    q: "Potřebuji vymalovat jen jednu místnost — je to možné?",
    a: "Samozřejmě. Realizujeme zakázky všech rozsahů — od malé koupelny až po velké komerční prostory. Minimální cena za malou zakázku je od 4 500 Kč.",
  },
  {
    q: "Jak postupujete, když jsou zdi v špatném stavu?",
    a: "Nejprve provedeme kompletní assessment stavu zdí. Škrábeme staré nátěry, sádrujeme praskliny, provádíme penetraci a štukování. Všechny přípravné práce jsou součástí kalkulace.",
  },
];

export default function FAQ() {
  const sectionRef = useRef<HTMLElement>(null);
  const [open, setOpen] = useState<number | null>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    const ctx = gsap.context(() => {
      gsap.fromTo(
        sectionRef.current!.querySelectorAll(".faq-item"),
        { opacity: 0, y: 20 },
        {
          opacity: 1,
          y: 0,
          duration: 0.6,
          stagger: 0.05,
          ease: "power3.out",
          scrollTrigger: { trigger: sectionRef.current, start: "top 80%" },
        }
      );
    }, sectionRef);
    return () => ctx.revert();
  }, []);

  return (
    <section
      id="faq"
      ref={sectionRef}
      className="w-full py-24 lg:py-36 px-5 lg:px-10 bg-[#F6F5F1]"
    >
      <div className="max-w-[720px] mx-auto">
        <div className="text-center mb-12 lg:mb-20">
          <p className="font-body text-[12px] uppercase tracking-[0.12em] text-[#5F6F65] mb-4">
            Časté dotazy
          </p>
          <h2 className="font-display text-[32px] sm:text-[44px] lg:text-[60px] leading-[1.0] tracking-[-0.02em] text-[#111111]">
            Odpovědi na otázky
          </h2>
        </div>

        <div>
          {items.map((item, i) => (
            <div key={i} className="faq-item border-b border-[#E3E1DC]">
              <button
                onClick={() => setOpen(open === i ? null : i)}
                className="w-full flex items-center justify-between py-6 text-left group"
              >
                <span className="font-body font-semibold text-[16px] lg:text-[18px] text-[#111111] pr-6 group-hover:text-[#5F6F65] transition-colors">
                  {item.q}
                </span>
                <span
                  className={`flex-shrink-0 w-7 h-7 rounded-full border flex items-center justify-center transition-all duration-300 ${
                    open === i
                      ? "border-[#5F6F65] bg-[#5F6F65] text-white rotate-45"
                      : "border-[#E3E1DC] text-[#5F6F65]"
                  }`}
                >
                  <Plus size={14} />
                </span>
              </button>
              <div
                className={`overflow-hidden transition-all duration-400 ${
                  open === i ? "max-h-48 pb-6" : "max-h-0"
                }`}
              >
                <p className="font-body text-[15px] text-[#242424] leading-[1.7]">
                  {item.a}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
