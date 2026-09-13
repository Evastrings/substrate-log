# Chapter 1 — Vectors, what even are they?

## Geometric intuition (3Blue1Brown)

Three legitimate ways to think about a vector, and linear algebra lives in the overlap:

- **Physics student:** a vector is an arrow with a *magnitude* and a *direction*. It can sit
  anywhere in space — what matters is length and orientation, not position.
- **CS student:** a vector is an ordered list of numbers. A list of house attributes
  (square footage, price) is "a vector" in this sense, even though it has nothing to do
  with arrows.
- **Mathematician:** a vector can be anything where there's a sensible notion of adding
  two of them and scaling them. The arrow and the list are both special cases of this
  more general object.

For linear algebra specifically: a vector is anchored with its tail at the **origin**.
Its coordinates then tell you how far to walk along each basis direction to reach the
tip.

- `[3, -2]` means: start at the origin, move 3 units along the unit vector **î** (x-axis),
  then -2 units along the unit vector **ĵ** (y-axis).
- î and ĵ are called the **basis vectors** of the coordinate system.

**Vector addition** — tip-to-tail: move along the first vector from the origin, then
from that new point move along the second vector. The coordinates of where you land are
the sum of the two vectors' coordinates. This is "moving in a series of steps."

**Scalar multiplication** — stretching or squishing a vector by a number (the *scalar*).
A positive scalar > 1 stretches it, a scalar between 0 and 1 squishes it, and a
**negative** scalar flips the direction before scaling the magnitude.

> "The introduction of numbers as coordinates is an act of violence." — Hermann Weyl

This is the tension the whole course sits inside: numbers are a *convenient* description
of a vector, not what the vector fundamentally *is*. Change the basis vectors and the same
arrow gets different numbers.

## Formal treatment (ILA style)

- A vector in ℝⁿ is an ordered n-tuple of real numbers, `v = (v₁, v₂, ..., vₙ)`, which can
  equivalently be represented as a column.
- Addition is componentwise: `(u₁+v₁, u₂+v₂, ...)`.
- Scalar multiplication is componentwise: `c·(v₁, v₂, ...) = (cv₁, cv₂, ...)`.
- These two operations, plus the origin acting as the additive identity, are what let you
  eventually define a **vector space** abstractly (see Ch. 16) — vectors don't have to be
  arrows or tuples at all, they just have to obey these rules.

## Key takeaway

Don't over-index on "vector = arrow." The arrow is the training-wheels picture. What
actually matters for everything downstream (spans, transformations, eigenvectors) is that
vectors can be **added** and **scaled**, and every other idea in the course is built out
of just those two operations.
