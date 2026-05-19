import Navigation from "./sections/Navigation";
import Hero from "./sections/Hero";
import Services from "./sections/Services";
import Process from "./sections/Process";
import Gallery from "./sections/Gallery";
import References from "./sections/References";
import Pricing from "./sections/Pricing";
import FAQ from "./sections/FAQ";
import Contact from "./sections/Contact";
import Footer from "./sections/Footer";
import FloatingCTA from "./sections/FloatingCTA";

export default function Home() {
  return (
    <div className="relative">
      <Navigation />

      <main>
        <Hero />

        <div className="w-full h-20 bg-gradient-to-b from-[#F2F1ED] to-[#FAFAF7]" />

        <Services />

        <div className="w-full h-20 bg-gradient-to-b from-[#FAFAF7] to-[#F2F1ED]" />

        <Process />

        <div className="w-full h-20 bg-gradient-to-b from-[#F2F1ED] to-[#FAFAF7]" />

        <Gallery />

        <div className="w-full h-20 bg-gradient-to-b from-[#FAFAF7] to-[#F2F1ED]" />

        <References />

        <div className="w-full h-20 bg-gradient-to-b from-[#F2F1ED] to-[#FAFAF7]" />

        <Pricing />

        <div className="w-full h-20 bg-gradient-to-b from-[#FAFAF7] to-[#F2F1ED]" />

        <FAQ />

        <div className="w-full h-20 bg-gradient-to-b from-[#F2F1ED] to-[#FAFAF7]" />

        <Contact />
      </main>

      <Footer />
      <FloatingCTA />
    </div>
  );
}
