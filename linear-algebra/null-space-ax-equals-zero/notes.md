# Ax = 0, the Null Space, and Row vs. Column Dependence

## Starting question
For a "matrix" built from three triples — [1,-1,2], [-2,2,-4], [1,2,3] — where one row/column is clearly a multiple of another, what does the solution x to Ax=0 actually represent geometrically?

## First fix: columns vs. rows are different matrices
The same three triples can be read two ways, and they give *different* matrices with *different* null spaces:
- **As columns**: a₁=(1,-1,2), a₂=(-2,2,-4), a₃=(1,2,3). Here a₂ = -2·a₁.
- **As rows**: the standard convention for "Ax=0", solving
  ```
  [ 1  -1   2]       [0]
  [-2   2  -4] x  =  [0]
  [ 1   2   3]       [0]
  ```

These are not the same matrix, so don't expect the same null space from both readings.

## What x represents geometrically
**x is not a linear combination of A's columns — it's the recipe for one.**

    Ax = x₁a₁ + x₂a₂ + x₃a₃

x's entries are the coefficients applied to A's columns. Ax=0 asks: *is there a nonzero set of coefficients that cancels the columns down to nothing?* x lives in **coefficient space**, not in the space the columns themselves occupy. They coincide (both Rⁿ) only because A happened to be square here — that's a coincidence, not a rule. If A were 3×5, x would live in R⁵ while the columns live in R³ — completely different spaces.

## Case 1: reading as columns
a₂ = -2a₁ is the whole story: 2 parts a₁ + 1 part a₂ cancel exactly (they're opposite directions, one twice as long), while a₃ isn't a multiple of either, so any nonzero coefficient on it leaves a residual — forcing x₃=0.

Null space direction: **(2, 1, 0)** — check: 2·(1,-1,2) + 1·(-2,2,-4) + 0·(1,2,3) = (0,0,0). ✓

Since a₂ is redundant, Col(A) collapses to a plane (rank 2), and nullity = 1 — matching **free parameters = unknowns − rank**. Every point on the line through (2,1,0) is a valid null-space vector (all scalar multiples) — the geometric content of a dependency is a whole *direction* of coefficients, not one special vector.

## Case 2: reading as rows (the actual worked computation)
Row reduction:
```
R1=[1,-1,2]  R2=[-2,2,-4]  R3=[1,2,3]

R2 + 2R1 = [0,0,0]   → row 2 is redundant (= -2·row 1), drop it, reorder:
[1,-1,2]
[1, 2,3]
[0, 0,0]

R1 - R3 → new row2 = [0,-3,-1]:
[1,-1, 2]
[0,-3,-1]
[0, 0, 0]

÷(-3) row2 → [0,1,1/3]:
[1,-1, 2 ]
[0, 1,1/3]
[0, 0, 0 ]

R1 + R2 → [1,0,7/3]:
[1,0,7/3]
[0,1,1/3]
[0,0, 0 ]
```

Pivots in columns 1,2 → x₃ is free. Reading off the RREF:

    x₁ = -(7/3)x₃
    x₂ = -(1/3)x₃
    x₃ = x₃  (free)

Let x₃ = t: **x = t·(-7/3, -1/3, 1)**, for any t ∈ ℝ — a full line through the origin, infinitely many solutions.

**Where I was wrong:** my first candidate answer was (-7/3, -1/3, 0) — off by one digit. The free variable itself must be set to 1 to generate the line (t=1 case); setting it to 0 only ever gives the trivial solution (0,0,0), which is why that candidate failed the Ax=0 check (plugging it in gave (-5/3, 5/3, -10/3), not zero).

Geometrically here the redundancy is row 2 = -2·row 1 — the second equation carries no independent information, leaving two independent constraints on three unknowns, hence one degree of freedom (a line) survives.

## The row/column duality — precise version
This is where an earlier looser claim ("Ax=0 relates to independence, roughly") needed tightening:

**For columns, Ax=0 doesn't just relate to independence — it *is* the definition of it.** The columns of A are linearly independent iff Ax=0 has only the trivial solution x=0. Finding a nontrivial solution to Ax=0 (Case 1's x=t(2,1,0)) *is* checking independence — not a separate computation that happens to be related.

**For rows, it's the same question on a different matrix.** A dependence relation among the rows of A is exactly a dependence relation among the columns of Aᵀ. When elimination produced R2+2R1=0, giving scalars (2,1,0), that *is* the null-space computation for Aᵀ — discovered as a byproduct of eliminating A, not a fundamentally different operation.

**Summary: row reduction is the single tool that exposes dependence relations either way** — for columns, the free-variable parametrization of Ax=0 gives the relation directly; for rows, a row collapsing to zero during elimination gives the relation as the trail of scalars used to get there.

## Ax = b vs. Ax = 0 — these are genuinely different ideas
Easy trap: conflating "Ax=b gives coefficients that reduce A to zero (for columns)" with "Ax=0 gives the solution set when b=0" as if they're two versions of the same operation via transposition. They're not — that's mixing up two independent distinctions.

- **Ax = b** (general): "which combination of A's columns builds the target vector b?" For a generic b, the combination lands on b — a nonzero vector, not zero. "Reducing to zero" only happens in the special case b=0.
- **Ax = 0** (homogeneous, the special case): which combinations of the columns cancel completely — the dependence relation, whose full solution set is the null space.

**The real relationship:** if x_p is any one particular solution to Ax=b, the complete solution set is

    x_p + Null(A)

Every solution to Ax=b looks like (one specific answer) + (any null-space vector). The null space is the "free slack" — directions you can nudge x in without moving Ax off of b, because those directions collapse to zero anyway.

**Note:** the row/column transpose duality is a *separate* idea from the Ax=b vs Ax=0 distinction. Transpose duality is about row-dependence vs. column-dependence being the same question asked of A vs. Aᵀ. Ax=b vs Ax=0 is about whether the target is a specific vector or the zero vector. Don't merge the two.

## Here's where I was wrong (build-in-public note)
1. Misread a triple of vectors as columns when the row-reduction convention (and the standard Ax=0 setup) called for rows — got a different, incorrect null space direction as a result.
2. Dropped a digit turning the RREF into a parametric solution — set the free variable to 0 instead of 1, which silently collapsed an infinite line of solutions into just the trivial one.
3. Initially undersold the row/column-independence connection as "just related," when for columns it's literally the definition, not a related fact.
4. Conflated the transpose duality (rows of A vs columns of Aᵀ) with the Ax=b vs Ax=0 distinction — they're answering different questions and shouldn't be merged.
