# Chapter 3 — Linear transformations and matrices

## Geometric intuition (3Blue1Brown)

A **linear transformation** is a function: it takes in a vector and spits out a vector.
"Unfortunately, no one can be told what the matrix is — you have to see it for
yourself." (Morpheus reference; the point being matrices only click once you've watched
them act on space.)

A transformation is **linear** iff it satisfies two properties:

1. **Lines remain lines** — gridlines stay parallel and evenly spaced (no curving).
2. **The origin remains fixed** in place.

Because a transformation is fully determined by where the *basis vectors* land, and any
vector is a linear combination of the basis vectors, you can compute where **any** vector
lands just by knowing where î and ĵ land:

```
[x]           [a]      [b]     [ax + by]
[y]  →  x·[c] + y·[d]  =  [cx + dy]
```

The matrix's **columns literally are** the new coordinates of the transformed basis
vectors. E.g. if `î → [1,-2]` and `ĵ → [3,0]`, the matrix is:

```
[1  3]
[-2 0]
```

and any input `[x,y]` transforms to `[x + 3y, -2x + 0y]`.

## Formal definition (ILA style)

A transformation `L` is linear iff, for all vectors `u, v` and scalar `c`:

- **Additivity:** `L(u + v) = L(u) + L(v)`
- **Homogeneity (scaling):** `L(cv) = c·L(v)`

These two properties are exactly what let you represent `L` as multiplication by a
matrix — the matrix encodes the transformation completely because of linearity.

## Key takeaway

A matrix is not a grid of numbers to memorize operations on — it's a compact recipe for
"where do the basis vectors go," and that recipe alone determines the fate of every other
vector in the space.
