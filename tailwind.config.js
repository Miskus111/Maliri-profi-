/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ["'Playfair Display'", "Georgia", "serif"],
        body: ["'Inter'", "-apple-system", "BlinkMacSystemFont", "sans-serif"],
      },
      colors: {
        sage: {
          DEFAULT: "#5F6F65",
          50: "#F4F6F4",
          100: "#E3E8E5",
          200: "#C7D1CB",
          300: "#A5B5AC",
          400: "#7D9186",
          500: "#5F6F65",
          600: "#4A5A50",
          700: "#3A473E",
          800: "#2D3831",
          900: "#1F2622",
        },
        beige: {
          DEFAULT: "#D8CEC2",
          50: "#FAF8F6",
          100: "#F3F0EC",
          200: "#E8E2D9",
          300: "#D8CEC2",
          400: "#C4B6A6",
          500: "#A89884",
        },
        stone: {
          50: "#F2F1ED",
          100: "#E1E0DC",
          200: "#D4D4D4",
          300: "#A3A3A3",
          400: "#6B6B6B",
          500: "#525252",
          600: "#404040",
          700: "#1F1F1F",
          800: "#171717",
          900: "#0A0A0A",
        },
      },
    },
  },
  plugins: [],
};
