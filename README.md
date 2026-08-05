# meishi

Static site for meishi.shop. NFC business cards in six materials and small
business websites, Markham, Ontario.

Plain HTML and CSS. No build step, no npm. The only JavaScript on the
site is one small inline script on `/write` that talks to the phone's NFC
radio through Web NFC; every other page ships none. `style.css` is
the single source of truth for styles, and every page carries a copy
inlined in a `<style>` block so the first paint needs no second request;
after editing `style.css`, run `python3 tools/inline-css.py` and commit
both. Header and footer markup is duplicated across pages on purpose; the
duplication costs less than a toolchain here.

## Card URLs

These six paths are encoded onto physical cards and can never change, not
even to a redirect:

```
/metal  /wood  /plastic  /paper  /fabric  /selvedge
```

Each is a directory with an `index.html`, so `/metal` and `/metal/` both
resolve with no `.html` extension.

## Deploy, step by step

Cloudflare Pages, connected to this repo.

1. Cloudflare dashboard, Workers and Pages, Create, Pages, Connect to Git.
   Pick this repo, production branch `main`.
2. Build settings: framework preset None, build command empty, build output
   directory `/`. Save and deploy.
3. Custom domains tab: add `meishi.shop`. If the domain's DNS is already on
   Cloudflare, Pages adds the record itself; otherwise it will ask to create
   a `CNAME` for `meishi.shop` pointing at `<project>.pages.dev` (Cloudflare
   flattens the CNAME at the apex automatically). Add `www.meishi.shop` as a
   second custom domain the same way.
4. SSL/TLS settings for the zone: set mode to Full (strict). Pages serves a
   real certificate, so strict costs nothing and stops anyone downgrading
   the hop between Cloudflare and the origin.
5. Redirect `www` to the apex: Rules, Redirect Rules, create one rule,
   when hostname equals `www.meishi.shop`, 301 to
   `https://meishi.shop$1` with the path preserved. One hop, no chain.
6. Cache headers ship in the `_headers` file in this repo; nothing to
   configure in the dashboard.

Trailing slashes: Pages serves `dir/index.html` at `/dir` and 308-redirects
`/dir/` to `/dir`. The six card URLs are therefore encoded on the physical
cards WITHOUT the trailing slash (`meishi.shop/metal`), which always
returns 200 with no redirect. Verify all six after the first deploy:

```
for p in metal wood plastic paper fabric selvedge; do
  curl -s -o /dev/null -w "%{http_code} /$p\n" https://meishi.shop/$p
done
```

Every line must read 200. The 404 page (`404.html`) is picked up by Pages
automatically and lists the six card URLs, since the most likely 404 is a
mistyped card link.

## Before launch

- Replace the placeholder phone number `(905) 000-0000` in every footer and
  on `/order` (search for `19050000000`).
- Real photos: search the pages for `TODO` to find each shot.
- `/story` is placeholder text until Katsuma writes it.
- `/work` ships honestly empty until real client jobs exist.

## Rules

Never commit to main; every change is a branch and a PR. No em dashes in
copy. No JS unless a feature genuinely needs it. Every page under 100KB.
