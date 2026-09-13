# Chapter 7 — Inverse matrices, column space, and null space

## Geometric intuition (3Blue1Brown)

> "To ask the right question is harder than to answer it." — Georg Cantor

Solving `Ax = v` means: which vector `x`, after being transformed by `A`, lands on `v`?

### Inverse matrix, `A⁻¹`

`A⁻¹` is the matrix representing the **reverse transformation** — the one that undoes
whatever `A` did.

```
A⁻¹Ax = A⁻¹v  ⟹  x = A⁻¹v      (since A⁻¹A = I, the identity)
```

- If `det(A) ≠ 0`, `A⁻¹` exists and there's exactly one solution `x` for every `v`.
- If `det(A) = 0`, the transformation squashes space into a lower dimension, and there is
  no way to "unsquash" it back out — so `A⁻¹` does **not** exist in that case (you'd need
  to map a single point/line back out into a full plane, which no function can do).

### Rank

**Rank** = the number of dimensions in the output of a transformation. A 2×2 matrix that
squashes the plane onto a line has rank 1; one that keeps the full plane has "full rank"
(rank 2).

### Column space

The set of *all* possible outputs `Ax` (as `x` ranges over every input vector) is called
the **column space** of `A` — literally the span of the matrix's columns. When the number
of dimensions in the column space equals the number of columns, `A` is **full rank**.

The zero vector `0` is always in the column space (since `A·0 = 0` for any `A`).

### Null space (kernel)

If `A` reduces dimensions (rank < number of columns), some nonzero set of input vectors
gets squashed to the origin. That set of vectors is the **null space** (or **kernel**) of
`A` — the set of solutions to `Ax = 0`.

## Formal worked example

Solve `2x + 5y + 3z = -3`, `4x + 0y + 8z = 0`, `1x + 3y + 0z = 2`:

```
A = [2 5 3]     x = [x]     v = [-3]
    [4 0 8]         [y]         [ 0]
    [1 3 0]         [z]         [ 2]
```

Because `det(A) ≠ 0` here, `A⁻¹` exists, and `x = A⁻¹v` gives the unique solution.

## Key takeaway

"Inverse, column space, rank, null space" are four faces of the same underlying
question: *does this transformation lose information, and if so, how much and which
inputs get lost?* Column space asks "what can I reach," rank asks "how many dimensions is
that," and null space asks "what collapses to nothing."
