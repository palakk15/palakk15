# Profile maintenance

Regenerate local graphics with `python scripts/build_assets.py` (Python 3, standard library only). The script preserves `assets/ascii-portrait.txt` and validates SVG XML and the 150 KB size limit. The original portrait was recovered from the embedded JPEG in this account's existing portfolio repository; it matches the supplied photograph.

The terminal, headings, project visualizations and flow diagram are local assets. Badge, skill-icon and capsule services are decorative dependencies. Each custom SVG has a dark background, accessible title and reduced-motion support.

## Contribution animation

Pushing to `main` starts **Generate Snake** automatically. It also runs daily at 00:00 UTC (05:30 IST). For a manual refresh: **Actions → Generate Snake → Run workflow → main → Run workflow**. The workflow publishes light/dark SVGs to the `output` branch. Public contributions supply the calendar data; an empty calendar will have little for the snake to traverse.

## Content follow-ups

- Confirm the deployed portfolio URL before adding a portfolio badge.
- Confirm project-specific language/framework stacks. Cards currently use only supplied technologies or capability labels.
- Add concrete Unicode and DJS Express responsibilities/results.
- Add a real agent project once available.
- Confirm the assumed sentence: “Open to software engineering and AI internships, and to collaborating on agent projects.”
- ReserveX was found, but is private. Its link is labeled accordingly; a public demo or case study would help visitors without access. All four exact repository links were found.

Project figures come from the supplied brief and are not independent benchmarks. Different projects' units are not plotted on a shared axis. Agentic AI is presented as a focus/exploration rather than an unprovided completed project.

## Files

```text
README.md
MAINTENANCE.md
assets/
  ascii-portrait.txt
  palak.jpg
  hero.svg
  divider-matrix.svg
  section-*.svg
  project-*.svg
  agent-flow.svg
scripts/build_assets.py
.github/workflows/snake.yml
```

To publish future edits:

```sh
python scripts/build_assets.py
git add README.md MAINTENANCE.md assets scripts .github .gitignore
git diff --cached --check
git commit -m "Update profile content and visuals"
git push origin main
```
