# Chapter 11 — Cross products in the light of linear transformations

## Geometric intuition (3Blue1Brown)

This chapter explains *why* the cross product formula from Ch. 10 works, by connecting it
to duality (Ch. 9).

Define a linear transformation from 3D vectors down to a number, parameterized by two
fixed vectors `v` and `w`:

```
f([x,y,z]) = det([x v₁ w₁; y v₂ w₂; z v₃ w₃])
```

This is linear in `[x,y,z]`, so by **duality** (Ch. 9), it corresponds to some vector `p`
such that `f(u) = p · u` for every input `u`. That vector `p` turns out to be exactly
`v × w`.

Why this makes geometric sense: `det([u v w])` computes the (signed) volume of the
parallelepiped spanned by `u`, `v`, `w`. That volume equals (area of the `v`,`w`
parallelogram) × (component of `u` perpendicular to that parallelogram). Since
`p · u = |p||u|cos(θ)`, matching this to the volume expression forces `|p|` to equal the
area of the `v`,`w` parallelogram, and `p`'s direction to be perpendicular to that
parallelogram (obeying the right-hand rule) — which is precisely the geometric
definition of `v × w` from Ch. 10.

## Worked component derivation

Expanding the determinant along the first column gives:

```
p₁ = v₂w₃ - v₃w₂
p₂ = v₃w₁ - v₁w₃
p₃ = v₁w₂ - v₂w₁
```

matching the Ch. 10 formula exactly.

## Key takeaway

The cross product formula isn't an arbitrary pattern to memorize — it *falls out* of
combining "determinant = volume" with "duality = every linear-to-a-number transformation
is secretly a dot product with some vector." This is one of the cleanest examples in the
whole course of how the earlier chapters compound into later ones (Ch. 6 determinant +
Ch. 9 duality → Ch. 11 cross product).
