# humanweek.org

The Human Week site, rebuilt from Wix as plain HTML and CSS. There's no build step and nothing to install.

## Pages

| URL | File |
|---|---|
| / | `index.html` |
| /about/ | `about/index.html` |
| /schedule/ | `schedule/index.html` (the 2026 schedule as a static list, pulled from Luma) |
| /host/ | `host/index.html` |
| /attend/ | `attend/index.html` |
| /thanks/ | `thanks/index.html` (where forms land after you submit) |

The header and footer are repeated on every page, so a change to the nav or footer needs to be made in all six files.

## Styles and assets

- `assets/css/site.css`: colors, type and layout. The colors at the top come from the Wix site.
- `assets/css/fonts.css` + `assets/fonts/`: Rubik, Sora, Instrument Serif, Space Mono and Silkscreen, hosted in this repo (open-source licensed).
- `assets/img/`: headshots, favicon, the blob shape and the pixel dividers.
- `assets/js/site.js`: the mobile menu, the gathering-type tabs on the Host page, and the looping tickers.

## Forms

The newsletter and host-interest forms are Netlify Forms (`data-netlify="true"`). Once the site is deployed on Netlify, submissions show up under Forms in the Netlify dashboard. The newsletter form will be replaced with beehiiv later.

## Preview locally

```
python3 -m http.server 8000
```
Then open http://localhost:8000
