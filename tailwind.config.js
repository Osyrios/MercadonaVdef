/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      fontFamily:{
        'RobotoBold':['robotoBold'],
        'RobotoItalic':['robotoItalic'],
        'RobotoRegular':['robotoRegular']
      }
    },
  },
  plugins: [],
}

