"use client";

const quickLinks = [
  { label: "Služby", href: "#services" },
  { label: "Proces", href: "#process" },
  { label: "Realizace", href: "#gallery" },
  { label: "Ceník", href: "#pricing" },
  { label: "Kontakt", href: "#contact" },
];

const services = [
  "Malování bytů",
  "Malování domů",
  "Komerční prostory",
  "Renovace",
  "Lakýrnictví",
  "Úklid",
];
const legal = ["Ochrana osobních údajů", "Obchodní podmínky", "Cookies"];

export default function Footer() {
  const scrollTo = (href: string) =>
    document.querySelector(href)?.scrollIntoView({ behavior: "smooth" });

  return (
    <footer className="w-full py-14 lg:py-20 px-5 lg:px-10 bg-[#1F1F1F]">
      <div className="max-w-[1280px] mx-auto">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 lg:gap-8">
          <div>
            <p className="font-body font-medium text-[17px] text-white">
              Malíři Profi
            </p>
            <p className="font-body text-[13px] text-white/60 mt-0.5">
              David Telvak
            </p>
            <p className="font-body text-[13px] text-white/55 mt-3 max-w-[220px] leading-relaxed">
              Profesionální malířské služby v Praze a okolí od roku 1992.
            </p>
            <div className="mt-5 space-y-2">
              <a
                href="tel:+420737171208"
                className="block font-body text-[13px] text-white/70 hover:text-white transition-colors"
              >
                +420 737 171 208
              </a>
              <a
                href="mailto:telvakmal@seznam.cz"
                className="block font-body text-[13px] text-white/70 hover:text-white transition-colors"
              >
                telvakmal@seznam.cz
              </a>
            </div>
          </div>

          <div>
            <p className="font-body text-[11px] uppercase tracking-[0.1em] text-white/50 mb-4">
              Odkazy
            </p>
            <ul className="space-y-2.5">
              {quickLinks.map((l) => (
                <li key={l.label}>
                  <a
                    href={l.href}
                    onClick={(e) => {
                      e.preventDefault();
                      scrollTo(l.href);
                    }}
                    className="font-body text-[14px] text-white/75 hover:text-white transition-colors"
                  >
                    {l.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <p className="font-body text-[11px] uppercase tracking-[0.1em] text-white/50 mb-4">
              Služby
            </p>
            <ul className="space-y-2.5">
              {services.map((s) => (
                <li key={s}>
                  <a
                    href="#services"
                    onClick={(e) => {
                      e.preventDefault();
                      scrollTo("#services");
                    }}
                    className="font-body text-[14px] text-white/75 hover:text-white transition-colors"
                  >
                    {s}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <p className="font-body text-[11px] uppercase tracking-[0.1em] text-white/50 mb-4">
              Právní informace
            </p>
            <ul className="space-y-2.5">
              {legal.map((l) => (
                <li key={l}>
                  <span className="font-body text-[14px] text-white/75 hover:text-white transition-colors cursor-pointer">
                    {l}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="border-t border-white/[0.08] mt-12 pt-6 flex flex-col sm:flex-row justify-between items-center gap-3">
          <p className="font-body text-[12px] text-white/45">
            &copy; 2025 Malíři Profi. IČO: 44292279.
          </p>
          <p className="font-body text-[12px] text-white/45">
            Všechna práva vyhrazena.
          </p>
        </div>
      </div>
    </footer>
  );
}
