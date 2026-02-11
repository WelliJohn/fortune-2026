/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'fortune-red': '#DC143C',
        'fortune-gold': '#FFD700',
      },
    },
  },
  plugins: [],
}
