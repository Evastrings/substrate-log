# Chapter 14 — Eigenvectors and eigenvalues

## Geometric intuition (3Blue1Brown)

**Eigenvectors** are vectors that *don't get knocked off their own span* by a
transformation — they only get **scaled**, never rotated to point somewhere new. The
scaling factor is the corresponding **eigenvalue**.

Symbolically:
```
Av = λv
```
`A` is the matrix, `v` is the eigenvector, `λ` (lambda) is the eigenvalue — the amount by
which `v` is scaled.

This is enormously useful in 3D for describing **rotations**: the eigenvector of a 3D
rotation matrix (with eigenvalue 1) points along the **axis of rotation** — the one
direction that doesn't move at all.

## Deriving eigenvalues

Rewrite `Av = λv` as `Av - λv = 0`, i.e. `(A - λI)v = 0` (subtracting `λ` times the
identity matrix, since `λv` alone isn't valid matrix subtraction).

For this equation to have a **nonzero** solution `v` (the zero vector trivially always
"works" but isn't interesting), the transformation `(A - λI)` must squash space into a
lower dimension — meaning its determinant must be zero:

```
det(A - λI) = 0
```

This is the **characteristic polynomial**; its roots are the eigenvalues.

## Worked example (verified)

```
A = [2 2]
    [1 3]
```

```
det(A - λI) = det([2-λ  2   ]) = (2-λ)(3-λ) - 2
                  [1    3-λ ]
            = 6 - 5λ + λ² - 2 = λ² - 5λ + 4 = 0
            = (λ - 1)(λ - 4) = 0
        ⟹  λ = 1  or  λ = 4
```

**Eigenvector for λ = 1:** solve `(A - I)v = 0`:
```
[1 2][x]   [0]        x + 2y = 0  ⟹  x = -2y
[1 2][y] = [0]                       eigenvector ∝ [-2, 1]
```

**Eigenvector for λ = 4:** solve `(A - 4I)v = 0`:
```
[-2  2][x]   [0]      -2x + 2y = 0  ⟹  x = y
[ 1 -1][y] = [0]                        eigenvector ∝ [1, 1]
```

## Eigenbasis

If a matrix's eigenvectors span the full space, using them **as a basis** (see Ch. 13)
turns the matrix into a **diagonal matrix** — the eigenvalues sitting on the diagonal,
zeros everywhere else. Diagonal matrices are trivial to raise to powers (`Dⁿ` just raises
each diagonal entry to the n-th power), which is the whole reason eigenbases matter
computationally — e.g. for computing `Aⁿ` efficiently via `A = PDP⁻¹` ⟹ `Aⁿ = PDⁿP⁻¹`.

## Key takeaway

Eigenvectors/eigenvalues answer: "is there a direction this transformation respects,
rather than scrambles?" That question turns out to be central to diagonalization,
understanding rotations, and — down the line — the math behind PCA and stability
analysis in ML.
