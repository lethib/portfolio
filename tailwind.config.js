module.exports = {
  content: ['./templates/*.html'],
  theme: {
    extend: {
      colors: {
        'fond-bleu' : '#012b70',
      },
    },
  },
  plugins: [require('@tailwindcss/forms')],
}
