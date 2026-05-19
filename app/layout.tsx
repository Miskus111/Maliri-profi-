import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Malíři Profi Praha | Profesionální malířské služby od roku 1992",
  description:
    "Profesionální malířské služby v Praze — malování bytů, domů a kanceláří. 30 let zkušeností, čistá práce, férové ceny. Nezávazná kalkulace zdarma.",
  keywords: [
    "malíř pokojů Praha",
    "malování bytů Praha",
    "malířské práce Praha",
    "malování kanceláří Praha",
    "malíři Praha",
  ],
  authors: [{ name: "David Telvak - Malíři Profi" }],
  robots: "index, follow",
  openGraph: {
    title: "Malíři Profi Praha | Profesionální malířské služby",
    description:
      "Malování bytů, domů a kanceláří po celé Praze a okolí. 30 let zkušeností, čistá práce, férové ceny.",
    type: "website",
    images: ["/images/img-21.jpg"],
    locale: "cs_CZ",
  },
  twitter: {
    card: "summary_large_image",
    title: "Malíři Profi Praha | Profesionální malířské služby",
    description: "Malování bytů, domů a kanceláří po celé Praze. 30 let zkušeností.",
    images: ["/images/img-21.jpg"],
  },
  icons: {
    icon: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 24 24' fill='none' stroke='%235F6F65' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M18 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3H6a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3V6a3 3 0 0 0-3-3 3 3 0 0 0-3 3 3 3 0 0 0 3 3h12a3 3 0 0 0 3-3 3 3 0 0 0-3-3z'/%3E%3C/svg%3E",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="cs">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:wght@400;500;600&display=swap"
          rel="stylesheet"
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "LocalBusiness",
              name: "Malíři Profi - David Telvak",
              description:
                "Profesionální malířské služby v Praze a okolí. Malování bytů, domů a komerčních prostor.",
              url: "https://www.maliriprofi.cz",
              telephone: "+420737171208",
              email: "telvakmal@seznam.cz",
              founder: { "@type": "Person", name: "David Telvak" },
              address: {
                "@type": "PostalAddress",
                streetAddress: "Maňákova 753/20",
                addressLocality: "Praha 14",
                addressRegion: "Praha",
                postalCode: "198 00",
                addressCountry: "CZ",
              },
              areaServed: { "@type": "City", name: "Praha", containedIn: "CZ" },
              serviceType: [
                "Malování bytů",
                "Malování domů",
                "Malování kanceláří",
                "Renovace interiérů",
                "Lakýrnictví",
              ],
              priceRange: "$$",
              openingHours: "Mo-Fr 07:00-18:00",
              foundingDate: "1992",
              image: "/images/img-21.jpg",
            }),
          }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
