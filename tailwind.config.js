/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "**/templates/**/*.html",

    "**/*.py",
  ],
  safelist: ["bg-green-800"],
  theme: {
    fontFamily: {
      sans: ["Roboto"],
    },
    extend: {
      fontFamily: {
        roboto: ["Roboto", "sans-serif"],
        "dancing-script": ["Dancing Script", "cursive"],
      },
      colors: {
        "custom-powder-light": "#eee2dc",
        "custom-powder": "#edc7b7",
        "custom-blue": "#123c69",
        "custom-blue-light": "#3a6aa4",
        "custom-red": "#ac3b61",
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
