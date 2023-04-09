const env = process.env.SVELTE_APP_ENV;

let envApiUrl = "";

if (env === "production") {
  envApiUrl = `https://${process.env.SVELTE_APP_DOMAIN_PROD}`;
} else if (env === "staging") {
  envApiUrl = `https://${process.env.SVELTE_APP_DOMAIN_STAG}`;
} else {
  envApiUrl = `http://${process.env.SVELTE_APP_DOMAIN_DEV}`;
}

export const apiUrl = envApiUrl;
export const appName = process.env.SVELTE_APP_NAME;
