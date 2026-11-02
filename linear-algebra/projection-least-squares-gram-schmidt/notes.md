# Projection, Least Squares & the Motivation for Gram-Schmidt

## Big Picture

These topics are not independent. They form one continuous chain of ideas:

```text
Projection
        ↓
Closest Point
        ↓
Error is Orthogonal
        ↓
Least Squares
        ↓
Normal Equations
        ↓
AᵀA measures overlap
        ↓
Overlap complicates coefficient recovery
        ↓
Gram-Schmidt removes overlap
        ↓
Orthonormal Basis
        ↓
QR Decomposition
```

---

## 1. Projection

A projection is the **closest point** in a subspace to a given vector.

If

- $`b`$ is the original vector,
- $`p`$ is its projection,

then

```math
e = b - p
```

is called the **error vector**.

The defining property of a projection is

```math
e \perp \text{Subspace}.
```

If the error were not perpendicular, we could move within the subspace and reduce its length, contradicting the definition of the closest point.

---

## 2. Projection onto a Line

Suppose a line is spanned by vector $`w`$.

The projection must be some multiple of $`w`$:

```math
cw.
```

Since the error is perpendicular to $`w`$,

```math
(v - cw)\cdot w = 0.
```

Expanding,

```math
v\cdot w - c\,(w\cdot w) = 0.
```

Therefore,

```math
c = \frac{v\cdot w}{w\cdot w}.
```

Thus,

**Projection onto a line:**

```math
\text{proj}_w(v) = \frac{w^T v}{w^T w}\, w
```

### Important intuition

The dot product is **not** the projection vector.

It measures **how much of one vector points in another direction**.

If $`w`$ is a unit vector, then $`w^T v`$ equals the shadow length.

Otherwise, dividing by $`w^T w`$ removes the scaling caused by the length of $`w`$, producing the correct coefficient in the linear combination.

---

## 3. Least Squares

Every vector in the column space can be written as

```math
Ax.
```

The projection is therefore

```math
p = Ax.
```

The error becomes

```math
e = b - Ax.
```

Since the error is orthogonal to every column,

```math
A^T e = 0.
```

Substituting,

```math
A^T (b - Ax) = 0.
```

Rearranging,

**Normal Equations:**

```math
A^T A x = A^T b
```

---

## 4. Understanding $`A^T`$

If

```math
A = \begin{bmatrix} a_1 & a_2 & \cdots & a_n \end{bmatrix},
```

then

```math
A^T =
\begin{bmatrix}
a_1^T \\
a_2^T \\
\vdots \\
a_n^T
\end{bmatrix}.
```

Therefore, for any vector $`y`$,

```math
A^T y =
\begin{bmatrix}
a_1^T y \\
a_2^T y \\
\vdots \\
a_n^T y
\end{bmatrix}.
```

Each row computes a dot product with one column of $`A`$.

**Interpretation:** every column asks

> "How much of this vector points in my direction?"

Thus,

```math
A^T e = 0
```

means the error has zero component in every basis direction of the column space.

---

## 5. Understanding $`A^T A`$

Expanding,

```math
A^T A =
\begin{bmatrix}
a_1^T a_1 & a_1^T a_2 \\
a_2^T a_1 & a_2^T a_2
\end{bmatrix}.
```

**Interpretation:**

- Diagonal entries = squared lengths.
- Off-diagonal entries = overlap between basis vectors.

Thus, $`A^T A`$ encodes the geometry of the basis.

---

## 6. Why Gram-Schmidt?

Suppose

```math
b = x_1 a_1 + x_2 a_2.
```

If the basis is not orthogonal, $`a_1^T b`$ does **not** equal $`x_1`$, because $`a_2`$ also contributes in the direction of $`a_1`$.

The dot product is working correctly — it measures directional components — but multiple basis vectors share those directions.

Gram-Schmidt removes this overlap by constructing an orthonormal basis spanning the same subspace.

---

## 7. First Step of Gram-Schmidt

Normalize the first basis vector:

```math
q_1 = \frac{a_1}{\| a_1 \|}.
```

Project $`a_2`$ onto $`q_1`$:

```math
(q_1^T a_2)\, q_1.
```

Subtract this projection:

```math
u_2 = a_2 - (q_1^T a_2)\, q_1.
```

Normalize:

```math
q_2 = \frac{u_2}{\| u_2 \|}.
```

**Verification:**

```math
q_1^T u_2 = 0.
```

Subtracting the projection removes everything already explained by previous basis vectors, leaving only a new orthogonal direction.

---

## Key Takeaways

- Projection = closest point.
- Error vector is always perpendicular to the subspace.
- Least squares is projection onto the column space.
- $`A^T`$ computes dot products with every column.
- $`A^T A`$ measures relationships between basis vectors.
- Non-orthogonal bases couple the coefficients.
- Gram-Schmidt removes that coupling by building an orthonormal basis.
- QR decomposition is Gram-Schmidt expressed in matrix form (next topic).
