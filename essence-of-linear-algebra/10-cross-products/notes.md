# Chapter 10 — Cross products

## Geometric intuition (3Blue1Brown)

The "standard" introduction to cross products, before reframing them via linear
transformations in Ch. 11.

- `î × ĵ = +1` (in the 2D sense) — a right-handed convention.
- For 2D vectors `v` and `w`, `v × w` computed as `det([v w])` gives a **signed area**:
  the area of the parallelogram formed by `v` and `w`.
  - If `w` is counterclockwise from `v` (roughly, "`v` is to the right of `w`"), the cross
    product is **positive**.
  - If `w` is clockwise from `v` (to the left), the cross product is **negative**.
- **Anticommutative:** `v × w = -(w × v)` — swapping the order flips the sign, since it
  reverses which vector is "the reference" for orientation.

## 3D cross product

For 3D vectors `v` and `w`, the cross product produces a **new 3D vector** `p = v × w`
such that:

- `|p|` = the area of the parallelogram that `v` and `w` span.
- The direction of `p` is **perpendicular** to both `v` and `w`, with orientation given by
  the **right-hand rule**.

Formula:
```
v × w = [v₂w₃ - v₃w₂]
        [v₃w₁ - v₁w₃]
        [v₁w₂ - v₂w₁]
```

This can be remembered via the symbolic determinant:
```
v × w = det([ î   v₁  w₁ ])
            ([ ĵ   v₂  w₂ ])
            ([ k̂   v₃  w₃ ])
```
expanding along the first column and treating î, ĵ, k̂ as placeholders for the resulting
vector's components.

## Key takeaway

The 2D cross product is really "signed area, dressed up as a scalar." The 3D cross
product is "a whole new vector, perpendicular to both inputs, whose length is that same
signed area." Chapter 11 explains *why* the determinant formula falls out so naturally —
it's not a coincidence.
