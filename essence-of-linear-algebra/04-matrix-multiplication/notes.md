# Chapter 4 — Matrix multiplication as composition

## Geometric intuition (3Blue1Brown)

> "It is my experience that proofs involving matrices can be shortened by 50% if one
> throws the matrices out." — Emil Artin

**Composition:** applying one transformation, then another. Reading `f(g(x))` right to
left tells you the *order of operations* — apply `g` first, then `f`. The same logic
governs matrix products: `AB` applied to a vector means "apply `B` first, then `A`."

- The product matrix `AB`'s columns are found by tracking where `B`'s columns land after
  also being hit by `A` — i.e., transform the basis vectors of `B`'s output space by `A`.
- **Order matters.** Rotation-then-shear gives a different result than shear-then-rotation
  in general — matrix multiplication is **not commutative**: `AB ≠ BA` in general.
- **Associativity holds:** `(AB)C = A(BC)`. Geometrically this is obvious — applying three
  transformations in sequence doesn't care how you group the pairwise compositions,
  because "apply C, then B, then A" is the same physical action either way. This is a case
  where the algebraic fact is *easier* to see geometrically than to verify by grinding
  through the arithmetic.

## Multiplying two matrices — mechanics

For 2×2 matrices `A` and `B`:

```
[a b][e f]   [ae+bg  af+bh]
[c d][g h] = [ce+dg  cf+dh]
```

Interpreted geometrically: take `A`'s column vectors, and use them to figure out where
`B`'s basis vectors (its own columns) land — sum and scale `A`'s columns according to
`B`'s column entries.

## Formal notes

- Matrix-vector product is a linear combination of the matrix's columns, weighted by the
  vector's entries. This is the same operation, scaled up, whether multiplying a matrix
  by a vector or by another matrix (a matrix's columns are themselves just vectors).
- Composition of linear transformations is itself linear (additivity and homogeneity are
  preserved through composition) — which is *why* the composite can always be represented
  as a single matrix product.

## Key takeaway

Don't memorize the row-times-column arithmetic in isolation — that's the *symptom*.
The *cause* is: "where does each basis vector end up after both transformations,
applied in this specific order?"
