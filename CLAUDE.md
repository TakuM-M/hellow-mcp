# CLAUDE.md

## Language

- Write in English.

## Design document

- `architecture/index.html` is a visual overview of the system design.
- When making a design decision or change, update this HTML in the same change.
  - When an open question in section 6 is decided, remove it from section 6.
  - Bump the version and the updated date in the header, and add one line to the changelog in section 7.
- Draw diagrams as inline SVG, using CSS variables for colors (supporting both light and dark themes). Do not use external images.

## Principles

- KISS: Prefer the simplest code that works. 
- YAGNI: Implement only what the current task requires. No speculative options or extension points.
- SOLID: Apply only where it reduces real complexity — mainly single responsibility per module/function.
- When these conflict, KISS and YAGNI win.
