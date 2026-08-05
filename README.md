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

## Link pages

One tap can open a whole page of links: reviews, Instagram, menu, maps.
These are sold as a product ("link pages" on /products) and are built to
live at meishi.world under the customer's name once that domain is wired
up (separate repo, CNAME meishi.world, same GitHub Pages setup as this
one). Until then they live here:

- `/katsuma` is the official example, Katsuma's own page.
- `t/demo/` is the template. To make a customer's page, copy `t/demo/`
  to `t/<shopname>/` (or a top-level `/<name>/` for the meishi.world
  style), change the title, the h1, the logo if they have one, and the
  button links, then commit and push. Encode the card to that URL.
- These pages are noindexed on purpose; they are for taps, not search.

## Prices

Canonical, bare numbers, singles only: metal 40, wood 35, fabric 20,
embossed 20, cardstock 3, selvedge unpriced (stitched to order).
Stickers 5 to 8 (chip-size 5, bigger pieces and counter tags 8, matte).
Wholesale: half of retail, $200 opening order, Ontario and other
provinces by Canada Post.

## House rules for copy and design

- Every visible word renders lowercase (CSS transform, the house quirk).
- Never "NFC" or "free" in visible copy; the chip is "a microchip with
  an antenna". Titles and meta may say nfc for search.
- No em dashes. Plain declarative voice. Buttons say what happens.
- The product is called meishi, not cards, in nav and product context.
- The red selvedge line and denim twill texture appear only on
  /selvedge/. Everywhere else is flat matte.
- Light and dark mode both work; dark follows the device setting.

## Before launch

- Real photos: search the pages for `TODO` to find each shot.
- `/samples` ships honestly empty until real photos and jobs exist.

## Rules

Never commit to main; every change is a branch and a PR. No em dashes in
copy. No JS unless a feature genuinely needs it. Every page under 100KB.
