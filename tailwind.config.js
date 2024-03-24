/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      fontFamily:{
        'RobotoBold':['robotoBold','ui-sans-serif'],
        'RobotoItalic':['robotoItalic','ui-sans-serif'],
        'RobotoRegular':['robotoRegular','ui-sans-serif'],
        'Saiba':['saibaRegular', 'ui-sans-serif'],
        'SaibaOutline':['saibaOutlineRegular','ui-sans-serif']
      }
    },
  },
  plugins: [],
}

