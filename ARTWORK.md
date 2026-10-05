# A very small workshop

Original SVG artwork for the [ydot20 profile](https://github.com/ydot20), built around a friendly robot and its yellow rubber duck.

## Files

- `assets/workshop.svg`: wide hero with a gently floating head and blinking eyes.
- `assets/duck-route.svg`: a looping, decorative duck-and-circuit illustration.
- `assets/signoff.svg`: the closing note.
- Each has a separately composed `-mobile.svg` version, selected below a 600 px viewport.

All artwork is self-contained. There are no downloaded fonts, external image services, scripts, counters, contribution data, secrets, or GitHub Actions workflows. Animations stop when the viewer prefers reduced motion; the circuit retains a static golden trail.

## Rebuild

Python 3, standard library only:

```sh
python tools/build_assets.py
python tools/check_assets.py
```

The committed SVG files are the production assets. The builder is deterministic and makes no network requests. The duck animation is intentionally an illustration, not a visualization of GitHub contributions.

## Design

- Dark olive `#20251f`
- Warm cream `#f4efdf`
- Duck yellow `#ffcf42`
- Muted sage `#a7aa9b`

The wide and narrow layouts are drawn separately to keep the headline, character, and essential labels legible. The README also contains plain-text identification and descriptive image alternatives.
