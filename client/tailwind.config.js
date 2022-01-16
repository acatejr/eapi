// module.exports = {
//   content: ['./src/**/*{html, js, svelte, ts}'],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

const production = !process.env.ROLLUP_WATCH;
module.exports = {
  future: {
    purgeLayersByDefault: true,
    removeDeprecatedGapUtilities: true,
  },
  plugins: [
  ],
  purge: {
    content: [
     "./src/**/*{svelte, html, js, ts}",
    ],
    enabled: production // disable purge in dev
  },
};