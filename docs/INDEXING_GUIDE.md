# Notation and subject indexing: first pass

## Contents
A grouped Index of Notation in the front matter (45 entries) and an alphabetical Subject Index in the back matter (90 index commands including cross-references). The book class is unchanged. Definitions and substantial discussions are indexed, not every occurrence. This is a first pass, not exhaustive coverage.

The notation list includes automatic page references, dimensions where useful, local hypotheses, historical aliases, and overloaded-symbol warnings. It distinguishes rho(k) from rho_j, kernel rank from matrix rank, M from partial-circulant M_i, and trace tau from interpolation tau. It is not a new global definition overriding local conventions.

## Base and compatibility
Prepared against GitHub main commit d1532329f99bd81e0ef10cd8ca76d7d7443e872b. The Chapters 7--8 revision was not on main when this was prepared. The installer inserts at stable labels and headings instead of replacing mathematical source files. Apply mathematical updates first, then run this installer. If a later source update overwrites index entries, rerun the installer. Missing or ambiguous anchors stop installation before manuscript files are written. Always inspect the Git diff.

## Install
Create a new branch from your up-to-date local main, for example:

    git switch main
    git pull origin main
    git switch -c book-indices

Copy the CONTENTS of apply-to-repository-root/ into the repository root. This supplies new indexing files; it does not replace your mathematical source files. Then run:

    python3 scripts/add_book_indices.py --check
    python3 scripts/add_book_indices.py
    python3 scripts/check_book_indices.py
    make

The installer changes main.tex and inserts subject entries at definitions/discussions in the existing source. It is idempotent: rerunning it without intervening changes makes no edits. The installer and static checker require only Python's standard library.

The manuscript already loads makeidx and calls makeindex. The installer adds printindex and the Subject Index title. The supplied svmono class adds the subject index to the table of contents. No additional TeX packages or second MakeIndex stream are required: the notation list is a curated page-reference list rather than a symbol-sorting stream.

A full TeX installation supporting the existing EPS/PSTricks workflow is needed. latexmk should detect main.idx and run MakeIndex automatically; if necessary run makeindex main.idx and then make again. Let reference reruns finish. Review the compiled notation list and subject index, especially entry placement near page breaks, before committing and pushing.

## Checks and limits
The installed local source has 83 master-reachable TeX files. All inputs and reference/notation targets resolve; active labels are unique. Index and notation arguments pass static brace checks. Installer idempotence is verified. No LaTeX or MakeIndex executable is available here, so compilation, pagination, index sorting and visual layout have not been verified. Some notation references intentionally identify the principal discussion rather than the exact formula line.

Continue expanding the index as chapters stabilize. This indexing pass does not certify historical proofs or research-status claims, and does not normalize remaining mathematical aliases.

## Archive layout
- apply-to-repository-root/: new files to copy, then run the installer.
- review/INDEX_SOURCE_CHANGES.patch: source diff for review against the base commit. Do not apply it as well as running the installer.
- README-FIRST.md: this guide.

No changes have been pushed to GitHub.
