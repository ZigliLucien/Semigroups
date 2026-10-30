# Repository review and organization

## Scope
Reviewed the public main-branch source structure, master, chapter wrappers, editorial notes, selected mathematical source and existing build log. This is an editorial/build review, not a proof-by-proof mathematical certification. No changes have been pushed to GitHub.

## Findings and priorities
1. **High: normalize Chapter 5 notation semantically.** Its explicit crosswalk maps old N0 to current N, old N to J-N, old M0 to current M, and old M to M-tau omega. The inherited blocks still print old symbols. Do not apply blind global replacements; audit each definition, formula and subsequent use.
2. **High: distinguish build provenance.** The README and master disclaim compilation, but the repository contains a log ending with a successful 166-page main.pdf build. That proves a recorded build occurred, not that this log and PDF match the current source. Rebuild cleanly and record the commit and toolchain. No TeX engine is installed in this review environment, so the reorganized copy has not been compiled.
3. **High: maintain local hypotheses.** Audit each theorem for finiteness, irreducibility, aperiodicity, letter weights and rank assumptions. Preserve the existing separation between general semigroup theory and road-coloring applications.
4. **Medium: improve topic visibility.** Numbered legacy blocks hide their subjects. A generated chapter map now lists section headings and input paths; retain legacy names until stable semantic names can be chosen without breaking the historical crosswalks.
5. **Medium: separate core narrative from specialty material.** Keep Chapters 1-8 as the main dependency spine, Chapters 9-12 as extensions, and Chapter 13 as synthesis. This is an editorial recommendation, not a newly verified theorem-dependency graph.
6. **Medium: label completion status.** Existing front matter identifies Appendices B/C as scope notes and D as historical; preserve that distinction. Keep unproved converses and research questions visibly separate from established results.
7. **Low: repository hygiene.** Generated auxiliaries and PDFs were mixed with source. This source package excludes build artifacts, retains figure conversions, and adds a Makefile and .gitignore.

## Changes made
- Grouped chapters, appendices, front matter, shared sections, preamble, bibliography and figures.
- Rewrote input/include paths and added the graphics search path.
- Preserved mathematical source text, chapter order, authorship and the supplied svmono class.
- Archived earlier organizational metadata under docs/previous; that metadata describes the previous layout and is not a new validation result.
- Added a chapter map, path migration map and reproducible static input check.

## Class choice
The author's preference for amsart is noted. The current manuscript uses book-only structures (parts, chapters and front/main/back matter) and class-specific theorem environments. An amsart migration is a separate structural conversion, not a safe one-line class replacement. The current book class is retained in this conservative organization pass.

## Next mathematical editing pass
For each numbered statement, record: label, hypotheses, prerequisites, notation convention, proof status and examples. Start with Chapter 5, then audit the tensor/symmetric/zeon transition for common-letter versus independent-particle dynamics. Verify research-status claims and bibliography separately before publication.
