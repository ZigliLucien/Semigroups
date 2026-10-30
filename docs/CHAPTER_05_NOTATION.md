# Chapter 5 notation pass

The book class is retained. Changes apply to the local organized copy only; no GitHub push was made.

## Convention
N = E[KK^T]; M = E[K^T J K]; tau = tr(M).
The historical complementary N is written J-N. The historical centered M is written M-tau omega. No N0/M0 operator definitions remain in Chapter 5.

## Mathematical and editorial changes
- Rewrote the operator-definition section and fixed-point equations with a dummy matrix X/Y and explicit lists of applicable operators. Existing equation labels eq:N and eq:M are retained for downstream references.
- Distinguished uM=n^2 pi from u(M-tau omega)=(n^2-tau)pi.
- Wrote all trace and equipartition identities in the same convention.
- Corrected the corollary's reference to the Delta proposition instead of the norms proposition; corrected the local-group identity ek=ke=k; repaired the induction's reference to the kernel Delta corollary.
- Corrected a scalar/row/column dimensional mismatch in the transposed pair-survival identity.
- Replaced the doubly stochastic commutativity proof by a direct proof of MN=(n/r)J. Kept the original historical statement as an explicit statement about the centered/complementary operators, and also proved commutativity of the uncentered operators.
- Replaced an unfinished 'etc.' calculation with an explicitly marked further question.
- Called the stationary limit a Cesaro limit, avoiding an unnecessary aperiodicity assumption.
- Clarified that averaging distinguished idempotents does not assert an idempotent result.
- Removed fully commented historical duplicate material from two active chapter blocks; originals are preserved in the before/ patch review archive.

## Validation and limits
All input targets and reference-label names resolve in static checks. Exact rational tests on three explicit irreducible transformation examples (kernel ranks 1, 2 and 3) check fixed-point, equipartition, trace, centered-row and limit-commutation identities. These examples are sanity checks, not substitutes for proofs or a full hypothesis audit. No TeX engine is installed; no successful compilation is claimed.

## Remaining scope
Later inherited chapters still announce historical notation locally. This is not a book-wide notation migration. A full proof/hypothesis audit and a clean typesetting build remain necessary. The chapter-map inventory from the organization pass has not been regenerated and may retain older section titles.
