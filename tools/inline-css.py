#!/usr/bin/env python3
"""Copy style.css into the <style> block of every page.

style.css is the single source of truth for the site's CSS, but pages carry
it inlined so the first paint needs no second request; that is worth about
half a second on a phone with weak signal. After editing style.css, run:

    python3 tools/inline-css.py

and commit both the stylesheet and the pages it touched.
"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
css = (root / "style.css").read_text().strip()
pages = list(root.glob("*.html")) + list(root.glob("*/index.html"))
changed = 0
for f in pages:
    s = f.read_text()
    new = re.sub(
        r'(<link rel="stylesheet" href="/style\.css">|<style>.*?</style>)',
        lambda m: "<style>\n" + css + "\n</style>",
        s, count=1, flags=re.S)
    if new != s:
        f.write_text(new)
        changed += 1
print(f"{changed} pages updated")
