# meishi

Static site for meishi.shop. NFC business cards in six materials and small
business websites, Markham, Ontario.

Plain HTML and CSS. No build step, no npm, no JavaScript. `style.css` is
the single source of truth for styles, and every page carries a copy
inlined in a `<style>` block so the first paint needs no second request;
after editing `style.css`, run `python3 tools/inline-css.py` and commit
both. Header and footer markup is duplicated across pages on purpose; the
duplication costs less than a toolchain here.

## Card URLs

These six paths are encoded onto physical cards and can never change, not
even to a redirect:

```
/metal  /wood  /paper  /fabric  /selvedge  /embossed
```

Each is a directory with an `index.html`, so `/metal` and `/metal/` both
resolve with no `.html` extension.

## Deploy, step by step

GitHub Pages, straight from this repo. This is what is live now.

1. Repo Settings, Pages: build from the `main` branch, root folder. The
   `CNAME` file in the repo root holds the custom domain (`meishi.shop`).
2. DNS at the registrar (GoDaddy): four `A` records on `@` pointing at
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
   `185.199.111.153`, and a `CNAME` record on `www` pointing at
   `katsuma0.github.io`.
3. Once the Pages settings page shows the DNS check green, tick
   Enforce HTTPS.
4. Every merge to `main` deploys itself; the pages build runs in about a
   minute.

The `_headers` file is inert on GitHub Pages; it is kept in case the site
ever moves to a host that reads it (Cloudflare Pages does).

Trailing slashes: GitHub Pages serves `dir/index.html` at `/dir/` and
301-redirects `/dir` to `/dir/`. Phones follow that redirect instantly
when a card is tapped, so cards are encoded `meishi.shop/metal` and work
either way. Verify all six after a deploy:

```
for p in metal wood paper fabric selvedge embossed; do
  curl -sL -o /dev/null -w "%{http_code} /$p\n" https://meishi.shop/$p
done
```

Every line must read 200. The 404 page (`404.html`) is picked up by Pages
automatically and lists the six card URLs, since the most likely 404 is a
mistyped card link.

## Tap pages

Some customers want one tap to offer several links: reviews, Instagram,
menu, website. Those get a small page under `/t/`, a link tree with
nothing on it but their buttons and the meishi mark. `t/demo/` is
meishi's own hub (instagram, website, google); to make one for a shop,
copy `t/demo/` to `t/<shopname>/`, swap the logo for their name, change
the title and the button links, commit, and push. The card then gets
encoded to `meishi.shop/t/<shopname>`. These pages are noindexed on
purpose; they are for taps, not for search.

## Before launch

- Real photos: search the pages for `TODO` to find each shot.
- `/samples` ships honestly empty until real photos and jobs exist.

## Rules

Never commit to main; every change is a branch and a PR. No em dashes in
copy. No JS unless a feature genuinely needs it. Every page under 100KB.
