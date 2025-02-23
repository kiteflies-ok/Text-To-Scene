module.exports = {
    content: [
      './src/**/*.{html,js,jsx,ts,tsx}',
      './public/index.html'
    ],
    theme: {
      extend: {
        colors: {
          'primary': '#2563eb',
          'secondary': '#1e40af',
          'accent': '#7c3aed',
        },
        animation: {
          'fade-in': 'fadeIn 0.5s ease-out',
          'pulse': 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite'
        },
        keyframes: {
          fadeIn: {
            '0%': { opacity: 0, transform: 'translateY(20px)' },
            '100%': { opacity: 1, transform: 'translateY(0)' }
          }
        }
      },
    },
    plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
    ],
  }