# meishi

Static site for meishi.shop. NFC business cards in six materials and small
business websites, Markham, Ontario.

Plain HTML and CSS. No build step, no npm, no JavaScript. One shared
stylesheet at `style.css`. Header and footer markup is duplicated across
pages on purpose; the duplication costs less than a toolchain here.

## Card URLs

These six paths are encoded onto physical cards and can never change, not
even to a redirect:

```
/metal  /wood  /plastic  /paper  /fabric  /selvedge
```

Each is a directory with an `index.html`, so `/metal` and `/metal/` both
resolve with no `.html` extension.

## Deploy

Cloudflare Pages, connected to this repo.

- Build command: none
- Build output directory: `/`
- Custom domain: `meishi.shop`

Cloudflare Pages serves `dir/index.html` for both `/dir` and `/dir/` out of
the box, which is exactly what the card URLs need.

## Before launch

- Replace the placeholder phone number `(905) 000-0000` in every footer and
  on `/order` (search for `19050000000`).
- Real photos: search the pages for `TODO` to find each shot.
- `/story` is placeholder text until Katsuma writes it.
- `/work` ships honestly empty until real client jobs exist.

## Rules

Never commit to main; every change is a branch and a PR. No em dashes in
copy. No JS unless a feature genuinely needs it. Every page under 100KB.
