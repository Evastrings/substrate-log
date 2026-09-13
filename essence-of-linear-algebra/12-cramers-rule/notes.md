# Chapter 12 — Cramer's rule, explained geometrically

## Geometric intuition (3Blue1Brown)

Cramer's rule is a formula for solving `Ax = v` using determinants, and 3Blue1Brown's
point is that it's **not** the most efficient method computationally (Gaussian
elimination usually wins) — its real value is geometric insight.

### Setup: transformations that preserve dot products

An **orthonormal transformation** (rotation, reflection — one whose columns are unit
vectors, all mutually perpendicular) preserves dot products: applying the same
transformation to two vectors doesn't change their dot product. This matters because
Cramer's rule leans on measuring *areas*, and orthonormal transformations don't distort
area/angle relationships.

### The 2D case

For `Ax = v` where `A = [a b; c d]`:

```
x = Area(before scaling by det, using v in place of A's first column) / det(A)
y = Area(before scaling by det, using v in place of A's second column) / det(A)
```

Concretely:
```
x = det([v₁ b; v₂ d]) / det(A)
y = det([a v₁; c v₂]) / det(A)
```

**Why this works geometrically:** replacing a column of `A` with `v` and taking the
determinant computes the *area* of a parallelogram related to how `v` sits relative to
the untouched basis vector. Dividing by `det(A)` (the area-scaling factor of the whole
transformation) "undoes" that scaling, recovering the original coordinate.

### 3D generalizes the same way

For a 3×3 system, each unknown is the determinant of `A` with the corresponding column
swapped for `v`, divided by `det(A)`.

## Worked example (from notes)

```
3x + 2y = -4
-x + 2y = -2
```
```
A = [3  2]      v = [-4]
    [-1 2]          [-2]

y = det([3 -4; -1 -2]) / det(A)
x = det([-4 2; -2 2]) / det(A)
```

## Key takeaway

Cramer's rule is a beautiful *illustration* of why determinants and area-scaling matter,
more than a practical algorithm — it's worth knowing for the geometric "aha," not as a
go-to solving method.
