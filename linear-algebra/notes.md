# Interactive Linear Algebra — Chapter 1: Systems of Linear Equations & Vectors

*Source: Interactive Linear Algebra (Margalit/Herman, Georgia Tech, Ximera)*

## 1.1 What is linear algebra?

- **Linear** → anything to do with lines.
- **Algebra** → anything to do with solving for unknowns in equations.

## 1.2 Systems of linear equations

A **linear equation** in unknowns `x, y, z, ...` is a sum of constant multiples of those unknowns plus an optional constant, e.g.:

```
2x + 4y - z = 2
-x - z = 100
```

A **system of linear equations** is a collection of several linear equations considered together.

- **Solution** — values of the unknowns that make *every* equation in the system true simultaneously.
- **Solution set** — the collection of all solutions.
- **Solving** — finding the solution set, usually expressed with some number of parameters.

A system does not need to have a solution. Example:

```
x + 2y = 3
x + 2y = -3
```

Here the solution set is empty.

- **Inconsistent system** — no solutions.
- **Consistent system** — at least one solution.

A solution to a system in *n* variables is a list of *n* numbers. E.g. `(x, y, z) = (1, 2, 3)` is a candidate solution to a 3-variable system.

## 1.3 Rⁿ: points, lines, planes, space

- **ℝ** — the set of all real numbers (π, 3/4, -2.74, ...).
- **ℝⁿ** — the set of all ordered n-tuples of real numbers `(x₁, x₂, ..., xₙ)`. Such a tuple is called a **point** of ℝⁿ.

| Space | Interpretation |
|---|---|
| ℝ¹ | the number line |
| ℝ² | the xy-plane (Euclidean plane) |
| ℝ³ | 3D space |

When a system has *n* unknowns, it's psychologically useful to view a solution as a single point in ℝⁿ.

## 1.4 Picturing solution sets

- **Line** — a ray that is straight and infinite in both directions.
- **Plane** — a flat sheet, infinite in all directions.

A single linear equation in *n* variables defines an **(n − 1)-dimensional "plane"** in n-space. E.g. `x + y + z + w = 1` defines a 3-plane inside 4-space.

### Two equations, two unknowns — three cases

1. **Lines intersect at one point** → unique solution (the intersection point makes both equations true at once).
2. **Lines are parallel** → no solution. E.g. `x + 2y = 5` and `x + 2y = -5`.
3. **Lines coincide** (one equation is a scalar multiple of the other) → infinitely many solutions. E.g. `x + 2y = 5` and `2x + 10y = 10` — both true at `(0, 5)`, `(1, 2)`, `(5, 0)`, etc.

### Free variables

For a system with more unknowns than independent equations:

```
number of unknowns − number of independent equations = number of free variables
```

## 1.5 Parametric description of solution sets

Solving "with parameters" means expressing the solution set using free parameters rather than a single fixed answer.

Example: `x + y = 1` is the **implicit** equation of a line. Rewritten in **parametric form**:

```
(x, y) = (t, 1 - t),  for any t ∈ ℝ
```

Here `t` is a parameter — it parameterizes each point on the line.

## 1.6 Row reduction

Two standard approaches to solving systems:

- The elimination method
- Augmented matrices + row operations

**Three legal row operations:**
1. Swap two rows
2. Scale a row
3. Row replacement (add a multiple of one row to another)

### Row echelon form (REF)

A matrix is in row echelon form if:
- All zero rows are pushed to the bottom.
- The first nonzero entry in each row is strictly to the right of the first nonzero entry in the row above.
- Every entry below a pivot is zero.

**Theorem:** every matrix is row-equivalent to exactly one matrix in **reduced** row echelon form (RREF) — provided the three legal row operations are used correctly.

### RREF algorithm

```
1a. Swap row 1 with a lower row so the leftmost nonzero entry is in row 1 (if needed).
1b. Scale row 1 so its leading entry is 1.
1c. Use row replacement to zero out every entry below this 1.
2a. Repeat for row 2, using the leftmost nonzero entry in row 2 or below.
2b. Scale row 2 so its leading entry is 1.
2c. Zero out every entry below this 1.
... continue for each row ...
Last step: Use row replacement to clear every entry ABOVE each pivot,
           working from the last pivot backward.
```

This is the **forward pass** (clear below pivots) followed by the **backward pass** (clear above pivots) — RREF requires both.

### Pivot positions and pivot columns

- A **pivot position** is an entry that is a pivot in *some* row echelon form of the matrix.
- A **pivot column** is a column that contains a pivot position.

An augmented matrix corresponds to an **inconsistent** system if and only if the last column is a pivot column.

**Two illustrative cases:**
1. Pivot in every non-augmented column → unique solution.
2. Pivot in the last (augmented) column → no solution.

## 1.7 Parametric form — the recipe

For a consistent system in variables `x₁, ..., xₙ`:

> `xᵢ` is a **free variable** if its column in the row-echelon form is *not* a pivot column.

**Recipe:**
1. Write the system's augmented matrix.
2. Row reduce to RREF.
3. Write out the corresponding solved system of equations.
4. Move all free variables to the right-hand side.

## 1.8 Implicit vs. parametric equations

Given the implicit system:

```
2x + y + 12z = 1
x + 2y + 9z = -1
```

The parametric form is:

```
x = 1 - 5z
y = -1 - 2z

(x, y, z) = (1 - 5z, -1 - 2z, z),  z ∈ ℝ
```

This expresses every point on the line in terms of a single parameter `z`.

## 1.9 Number of solutions — three possibilities

For the RREF of an augmented matrix:

1. Last column is a pivot column → **inconsistent** (no solution).
2. Every column except the last is a pivot column → **unique solution**.
3. Last column is not a pivot column, and at least one other column also isn't → **infinitely many solutions** (free variable(s) present).

## 1.10 Matrix equation form: Ax = b

A system of linear equations can be written compactly as:

```
Ax = b
```

- `A` — an `m × n` matrix (coefficients)
- `x` — the unknown vector, in ℝⁿ
- `b` — a vector in ℝᵐ

Two central questions this framing sets up:
- What is the solution set of `Ax = b`?
- What is the set of *all* `b` for which the system is consistent?

## 1.11 Vectors in ℝⁿ

A vector is determined by its **length and direction**, not its location — it doesn't need to start at the origin. Unless stated otherwise, assume vectors start at the origin. A vector can also be thought of as the difference between two points.

### Vector algebra

**Addition:**
```
(a, b, c)ᵀ + (x, y, z)ᵀ = (a+x, b+y, c+z)ᵀ
```

**Scalar multiplication:**
```
c(x, y, z)ᵀ = (cx, cy, cz)ᵀ
```
`cv` is called a *scalar multiple* of `v`.

### Geometric interpretation

- **Parallelogram law (addition):** place the tail of `w` at the head of `v`. The sum `v + w` runs from the tail of `v` to the head of `w`. Doing this both ways (v then w, w then v) traces out a parallelogram.
- **Subtraction:** place the tails of `v` and `w` at the same point. Then `v - w` is the vector from the head of `w` to the head of `v`. (Check: `w + (v - w) = v`.)
- **Scalar multiplication:** scales the length of `v`, and flips direction if the scalar is negative. The set of all scalar multiples of a nonzero vector `v` is a **line**. The set of all scalar multiples of the zero vector is a single **point**.

## 1.12 Linear combinations

We can add and scale vectors within a single equation — a **linear combination**.

- The linear combination of a single vector traces out a line.
- Linear combinations of collinear vectors still span only that same line.

## 1.13 Vector equations

A **vector equation** — an equation involving a linear combination of vectors with unknown coefficients — is really an *n*-coordinate vector equation packaged as a single equation, equivalent to *n* ordinary numerical equations.

A linear system can be viewed three equivalent ways:
1. A system of linear equations
2. An augmented matrix
3. A vector equation

Vector equations are a means to an end — they give a more geometric lens on the same systems of equations we're ultimately trying to solve.

## 1.14 Span

The **span** of a set of vectors is the set of *all* linear combinations of those vectors — the subset "spanned" or "generated" by them.

Set-builder notation:

```
{ x₁v₁ + x₂v₂ + ... + xₖvₖ | x₁, x₂, ..., xₖ ∈ ℝ }
```

Read as: "the set of all things of the form `x₁v₁ + x₂v₂ + ... + xₖvₖ` such that `x₁, ..., xₖ` are real numbers."

---
