# Chapter 6 — The determinant

## Geometric intuition (3Blue1Brown)

> "The purpose of computation is insight, not numbers." — Richard Hamming

The determinant answers: **how much does a linear transformation scale areas (2D) or
volumes (3D)?**

- `det(A)` is the factor by which any region's area (2D) or volume (3D) gets scaled after
  applying the transformation `A`. This holds for *any* region, not just the unit
  square/cube — because linear transformations scale all regions by the same factor
  uniformly (a consequence of grid lines staying parallel and evenly spaced).
- **Negative determinant** = the transformation flips the orientation of space (like
  flipping a sheet of paper over) in addition to scaling area. In 2D, ĵ is usually to the
  left of î; if after the transformation ĵ ends up to the *right* of î, orientation has
  flipped, signaled by a negative determinant.
- **`det = 0`** means the transformation squashes space into something of a lower
  dimension — a line, or even a single point. Since a squashed region has zero area
  (or volume), the determinant faithfully reports this as zero.
- In 3D, the sign convention is governed by the **right-hand rule**: if flipping the hand
  orientation of the basis vectors would be needed to reproduce the transformed
  configuration, the determinant is negative.

## Determinant of a composition

```
det(M₁M₂) = det(M₁) · det(M₂)
```

Geometrically: if the first transformation scales area by a factor of `det(M₂)`, and the
second scales whatever it's given by `det(M₁)`, then applying both in sequence scales
area by the product of the two factors. This is a case where the geometric argument for a
seemingly-algebraic identity is more convincing than grinding through the formula.

## Formal 2×2 / 3×3 formulas

For 2×2:
```
det([a b; c d]) = ad - bc
```

For 3×3, expand along a row/column via cofactors (Laplace expansion) — e.g., worked in
notes as:
```
det([1 0 6; 1 2 3; 1 0 -1])
= 1(2·(-1) - 3·0) - 0(...) + 6(1·0 - 2·1)
= 1(-2) - 0 + 6(-2) = -2 - 12 = -14   ← re-verify this by hand, it was worked slightly
                                        differently across two notebook passes
```

## Key takeaway

The determinant is not an arbitrary formula to memorize — it's "how much area/volume
scaling does this matrix do, and does it flip orientation while doing it." Zero
determinant is the single most important diagnostic value in the whole course: it's the
dividing line between "this system of equations has a unique solution" and "it doesn't."
