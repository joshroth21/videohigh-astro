import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

import vercel from "@astrojs/vercel/serverless";

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  output: "server",
  adapter: vercel({
    functionPerRoute: false,
    imageService: true,
    imagesConfig: {
      sizes: [320, 640, 1280],
    },
  }),
});
