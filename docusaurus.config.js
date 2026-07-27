// @ts-check
// SETUP - replace YOUR-GITHUB-USERNAME in 3 spots below.

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Ridgeline Documentation',
  tagline: 'Customer documentation for Ridgeline, built as code',
  favicon: 'img/favicon.svg',

  organizationName: 'YOUR-GITHUB-USERNAME', // (1)
  projectName: 'ridgeline-docs',

  url: 'https://YOUR-GITHUB-USERNAME.github.io', // (2)
  baseUrl: '/ridgeline-docs/',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: { defaultLocale: 'en', locales: ['en'] },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/YOUR-GITHUB-USERNAME/ridgeline-docs/edit/main/', // (3)
          routeBasePath: '/',
        },
        blog: false,
        theme: { customCss: './src/css/custom.css' },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Ridgeline Docs',
        items: [
          { type: 'docSidebar', sidebarId: 'docsSidebar', position: 'left', label: 'Documentation' },
        ],
      },
      footer: {
        style: 'dark',
        copyright: 'Ridgeline is a fictional product. This site is a documentation portfolio artifact.',
      },
      colorMode: { defaultMode: 'dark', respectPrefersColorScheme: true },
    }),
};

export default config;
