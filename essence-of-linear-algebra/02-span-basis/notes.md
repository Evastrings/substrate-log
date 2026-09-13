# Chapter 2 — Linear combinations, span, and basis vectors

## Geometric intuition (3Blue1Brown)

"Mathematics requires a small dose, not of genius, but of an imaginative freedom which,
in a larger dose, would be insanity." — Vector coordinates are scalars that scale the
**basis vectors** î and ĵ. `[3, -2]` really means `3î + (-2)ĵ`.

- Anytime you scale two vectors and add them, that's a **linear combination** of them.
- The **span** of two vectors = the set of *all* possible linear combinations of them —
  every vector you can reach by adding and scaling those two vectors.
  - If the two vectors point in different directions, their span is the entire 2D plane.
  - If one vector is just a scaled version of the other, the span collapses to a single
    line (one vector is *redundant* — it adds no new reachable territory).
  - If both vectors are the zero vector, the span is just the origin.
- Vectors are more useful to think of as **points** (the tip) rather than arrows once
  you're juggling a whole span or collection of them — arrows clutter the picture fast.
- In 3D: the span of two vectors (generically) is a flat 2D plane through the origin. The
  span of three vectors, if the third isn't already in the span of the first two, fills
  all of 3D space.

## Linear dependence / independence

- **Linearly dependent vectors:** one of the vectors can be removed without shrinking the
  span of the whole set — i.e., that vector is already expressible as a linear
  combination of the others. It "adds no new dimension."
- **Linearly independent vectors:** each vector adds a new dimension to the span; none
  can be built from the others.

## Basis — technical definition

> The **basis** of a vector space is a set of linearly independent vectors that span the
> full space.

Every vector in the space can be written as *some* linear combination of the basis
vectors, and no basis vector is redundant.

## Formal treatment (ILA style)

- Given vectors `v₁, ..., vₖ` in ℝⁿ, their span is `{c₁v₁ + c₂v₂ + ... + cₖvₖ : cᵢ ∈ ℝ}`.
- A set is linearly independent iff the only solution to `c₁v₁ + ... + cₖvₖ = 0` is
  `c₁ = c₂ = ... = cₖ = 0`.
- Connects directly to the **null space** (Ch. 7/8): if the only vector that solves
  `Ax = 0` is `x = 0`, the columns of `A` are linearly independent.

## Key takeaway

Span answers "what can I reach?" Linear independence answers "is anyone on my team dead
weight?" Basis is the sweet spot: the minimal, non-redundant team that can still reach
everywhere.
