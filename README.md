# Coolest Art — "Sky Jelly"

Entry for make.fun `coolest-art-01`.

## The artwork

A colossal luminous jellyfish the size of a skyscraper drifts above a tiny
neon-lit coastal city at night, its violet-and-cyan bell glowing against a
starry indigo sky, while a lone figure on a rooftop reaches up toward it.
Original AI-generated artwork, vendored in this repo as `art.png`.

- Format: PNG, 1024 × 1024 px
- Size: 988,134 bytes (under the 1 MiB limit)

## The program

`main.py` copies the vendored `art.png` byte-identically to
`/output/entry.png`. Stdlib only, no network access, fully deterministic —
every run writes the exact same bytes.

## Run

```sh
python3 main.py   # writes /output/entry.png
```
