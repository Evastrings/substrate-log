# Chapter 16 — Abstract vector spaces

## Geometric intuition (3Blue1Brown)

Everything in the course generalizes beyond arrows-in-space. **Functions** can be
"vectors" too, once you notice they can be added and scaled just like arrows:

```
(f + g)(x) = f(x) + g(x)
(c·f)(x) = c·f(x)
```

### The derivative as a linear transformation

The derivative operator `d/dx` takes in a function (a "vector" in this space) and spits
out another function. It's **linear** because it obeys the same two properties from
Ch. 3:

```
d/dx(f + g) = d/dx(f) + d/dx(g)      → additivity
d/dx(c·f) = c · d/dx(f)              → homogeneity (scaling)
```

Example worked in notes: `d/dx(x³ + x² + x + 1) = 3x² + 2x + 1`.

### Polynomials as coordinate vectors

Using the basis functions `b₀(x) = 1, b₁(x) = x, b₂(x) = x², b₃(x) = x³, ...`, any
polynomial can be written as a coordinate vector of its coefficients:
```
2x² + 3x + 7  →  [7, 3, 2, 0, 0, ...]
```
Taking the derivative in this coordinate system becomes literal **matrix
multiplication** by a specific (infinite, mostly-zero) matrix — e.g. the notes work out
that differentiating in coefficient-space corresponds to a matrix whose structure shifts
each coefficient down and multiplies by its original exponent.

The space of all polynomials is infinite-dimensional (there's no bound on `n`, the
highest degree of term you could need).

## Formal treatment — the vector space axioms

A **vector space** is any set equipped with addition and scalar multiplication
satisfying these 8 axioms, for all vectors `u, v, w` and scalars `a, b`:

1. `u + (v + w) = (u + v) + w`
2. `v + w = w + v`
3. There exists a zero vector `0` such that `v + 0 = v` for all `v`
4. For every `v`, there exists `-v` such that `v + (-v) = 0`
5. `a(bv) = (ab)v`
6. `1v = v`
7. `a(v + w) = av + aw`
8. `(a+b)v = av + bv`

These axioms are **an interface, not an implementation** — much like an abstract class
in software. Whatever the underlying "vector" actually is (arrow, tuple, function,
matrix, polynomial), as long as it satisfies these 8 rules, every theorem proven using
only the axioms (spans, linear independence, eigenvectors, determinants, etc.)
automatically applies to it, without re-deriving anything from scratch.

## Key takeaway

This is the payoff of the entire course: linear algebra isn't fundamentally about arrows
in 2D/3D space — it's about any system obeying these 8 rules of "add and scale." That's
precisely why the same machinery (spans, eigenvectors, transformations) shows up
everywhere in ML — weight matrices, function spaces, and probability distributions can
all be treated as vectors once you notice they satisfy these axioms.
