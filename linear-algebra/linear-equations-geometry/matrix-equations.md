# When Solutions Always Exist

## The Theorem

Let $A$ be an $m \times n$ (non-augmented) matrix. The following are equivalent:

1. $Ax = b$ has a solution for all $b \in \mathbb{R}^m$.
2. The span of the columns of $A$ is all of $\mathbb{R}^m$ (i.e., $\text{Col}(A) = \mathbb{R}^m$).
3. $A$ has a pivot position in every row.

## Why they're equivalent

**1 ⟺ 2** is close to definitional once you know $Ax$ ranges over exactly $\text{Col}(A)$ as $x$ varies. "A solution exists for every $b$" *is* "every $b$ is hit by $Ax$" *is* "$\text{Col}(A) = \mathbb{R}^m$."

**2 ⟺ 3**: pivot-in-every-row is a structural check on $A$ alone (never look at $b$). Row reduce $[A \mid b]$ for arbitrary $b$ — if every row has a pivot in the coefficient part, no row can ever become $[0 \, 0 \, \cdots \, 0 \mid c]$ with $c \neq 0$, because that would require a pivot-free row. No pivot-free row → no possible contradiction, for *any* $b$.

## Necessary conditions (and why they're only necessary, not sufficient)

- **$m \le n$ is necessary.** You need at least as many columns as rows, since $m$ pivots need $m$ distinct columns to live in. If $n < m$, it's structurally impossible — no examination of entries needed.
- **$m \le n$ is *not* sufficient.** Counterexample: $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$. Here $m=2 \le n=3$, but row 2 is a multiple of row 1, so it row-reduces to only one pivot. The columns are all parallel — they span a line, not $\mathbb{R}^2$.
- **The real requirement:** rank $m$ — i.e., $m$ of the columns must be linearly independent. Independent vectors span a subspace whose dimension equals *how many* of them you have; spanning all of $\mathbb{R}^m$ requires that count to hit exactly $m$.

## Misconceptions I corrected along the way

**"The columns must be standard basis vectors."** Wrong — they only need to *span* $\mathbb{R}^m$, which is much weaker than containing $e_1, \dots, e_m$ literally. Counterexample: $A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$ satisfies the theorem (pivot in every row after $R_2 \to R_2 - R_1$) with no standard basis vector among its columns. What *is* true: if $A$ is square and satisfies the theorem, its RREF equals the identity — but that's a fact about the row-reduced matrix, not the original columns.

**Row independence ≠ column independence.** When asked to justify that a square matrix with a pivot in every row has independent columns, my first instinct was to reason about rows ("no row is a combination of the others"). That's true but is a separate fact — it doesn't establish column independence. The actual chain:

1. $n$ rows, pivot in each → $n$ pivots total.
2. Pivots occupy distinct columns → with $n$ pivots and $n$ columns, every column has one.
3. No pivot-free columns → no free variables in $Ax=0$.
4. No free variables → $Ax=0$ has only the trivial solution.
5. That's the definition of column independence.

This only works *because* $A$ is square — for non-square matrices, pivot-in-every-row and column-independence come apart completely (e.g., a $2\times 3$ matrix can have a pivot in every row while its 3 columns in $\mathbb{R}^2$ can't possibly all be independent).

## Key takeaway

For a **square** matrix, "pivot in every row" and "pivot in every column" are equivalent — pivots never share a row or column, so hitting $n$ pivots via full row coverage automatically means full column coverage too. This is the seed of the Rank-Nullity Theorem, which is next.

## Worked examples

**Satisfies the theorem:** $A = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \end{bmatrix}$ — already RREF, pivot in every row (2×3, non-square, so RREF ≠ identity but theorem still holds).

**Fails the theorem:** $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ — reduces to one pivot; $b=(0,1)$ produces a contradiction row $[0\,0\mid 1]$.

**Square, satisfies the theorem:** $A = \begin{bmatrix} 1&1&1\\1&1&2\\1&2&1\end{bmatrix}$ — reduces (with a row swap) to a pivot in every row, and full RREF gives the $3\times 3$ identity.
