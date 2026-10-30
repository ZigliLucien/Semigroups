# Algebraic Methods in Automata Theory

Conservatively reorganized source copy of ZigliLucien/Semigroups. Mathematical content and chapter order are preserved; this copy has not been compilation-tested.

## Start here
- `main.tex`: master document.
- `docs/REVIEW.md`: findings, scope and priorities.
- `docs/CHAPTER_MAP.md`: chapters, inputs and section headings.
- `docs/PATH_MAP.json`: old-to-new file paths.
- `docs/previous/`: inherited editorial records (historical, not regenerated).

## Layout
`chapters/`, `appendices/`, `blocks/`, `sections/`, `frontmatter/`, `preamble/`, `bibliography/`, `figures/`.

## Build
Run from the repository root with a full TeX installation supporting PSTricks, EPS, dvips and ps2pdf:

```sh
make
# equivalent: latexmk -pdfps main.tex
python3 scripts/check_inputs.py
```

The supplied svmono book class is retained. Migration to amsart requires a separate chapter/environment conversion. No remote repository changes were made by this review.
