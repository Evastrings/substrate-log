# Chapter 9 — Dot products and duality

## Geometric intuition (3Blue1Brown)

The role the dot product plays can be understood through the lens of linear
transformations.

**Numeric definition:** multiply corresponding components and add:
```
[a,b] · [c,d] = ac + bd
```

**Geometric meaning:** project the second vector onto the line through the first vector
(through the origin and the first vector's tip), then multiply the length of that
projection by the length of the first vector.

- When vectors point in the **same general direction**, the dot product is **positive**.
- When they're **perpendicular**, the dot product is **zero**.
- When they point in **roughly opposite directions**, the dot product is **negative**.
- The order doesn't matter (dot product is symmetric): `v·w = w·v`, and this symmetry is
  itself a reflection of the fact you could project either vector onto the other and
  scale by the other's length — both computations agree.

## Duality

A 1×2 matrix `[a, b]` acting on a 2D vector via matrix-vector multiplication looks
*identical*, arithmetically, to taking the dot product of `[a,b]` with that vector. This
is not a coincidence:

> **The dual of a vector is the linear transformation it encodes.** Every linear
> transformation from some vector space down to one dimension (the number line)
> corresponds to a unique vector in that space, such that applying the transformation is
> the same as dot-producting with that vector.

Concretely: a 1×2 matrix transforming 2D vectors down to numbers is fully described by
where î and ĵ land (two numbers) — and those two numbers are exactly the coordinates of
the vector you'd dot-product with to get the same result. The vector and the linear
functional are two views of the same object.

## Formal / worked note

For standard basis vectors, `î · ĵ = [1,0]·[0,1] = 0` (confirms perpendicularity, as
expected). For `[2,1]·[3,4]`, the projection interpretation and the componentwise
`ac + bd` computation agree, since `2·3 + 1·4 = 10`.

## Key takeaway

Dot product isn't a separate, disconnected operation from matrices — it's what a
1×n matrix multiplication *is*, and duality is the deep reason "vector" and "linear
functional to a number line" turn out to be the same kind of object in disguise.
