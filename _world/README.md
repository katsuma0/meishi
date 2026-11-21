# meishi.world

Link pages. One tap opens a page that holds every link a shop has:
reviews, Instagram, menu, website, maps. Sold through
[meishi.shop](https://meishi.shop); each page lives here at
`meishi.world/<name>`.

Plain HTML, one file per page, no build step, no JavaScript. Each page
carries its own CSS inline so the first paint needs no second request.

## Making a page

1. Copy `template/` to `<name>/`, lowercase, no spaces. That folder name
   is the URL, and it is encoded onto a physical card, so it can never
   change afterwards.
2. In `<name>/index.html` change the `<title>`, the `<meta
   name="description">`, the `<h1>`, and every button label and href.
   Add or remove buttons freely; four or five is the sweet spot.
3. Commit and push. GitHub Pages deploys in about a minute.
4. Encode the card or sticker to `https://meishi.world/<name>`.

Link pages are noindexed on purpose: they are for taps, not for search.
The root page is the only indexable one.

## Rules

- Every visible word renders lowercase; that is the house quirk.
- No em dashes. Plain declarative voice.
- Five colours only: indigo `#22304a`, cotton `#f2eee4`, selvedge red
  `#a13d36`, steel `#878c91`, birch `#cbaf82`.
- Never commit to main directly on meishi.shop; here, small pages can go
  straight in.

## Deploy

GitHub Pages from `main`, root folder. `CNAME` holds `meishi.world`.
DNS at the registrar: four `A` records on `@` pointing at
`185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
`185.199.111.153`, and a `CNAME` on `www` pointing at
`katsuma0.github.io`. Then tick Enforce HTTPS in the repo's Pages
settings once the DNS check goes green.
