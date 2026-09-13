# Chapter 5 — Three-dimensional linear transformations

## Geometric intuition (3Blue1Brown)

Everything from Ch. 3–4 extends directly to 3D — important for robotics and computer
graphics. Now there are **three** basis vectors: î, ĵ, k̂, each a 3D column, and a 3×3
matrix's three columns tell you where each one lands.

A 3D vector transforms as a linear combination of the transformed basis vectors, exactly
like the 2D case, just with one more term:

```
[x]
[y]  →  x·(where î lands) + y·(where ĵ lands) + z·(where k̂ lands)
[z]
```

Composing two 3D linear transformations (applying one 3×3 matrix, then another) works by
the identical logic as 2D matrix multiplication — track where each column of the second
matrix ends up after being hit by the first.

## Worked arithmetic (own notes, verified)

Given:

```
A = [ 0  -2   2]      B = [1]
    [ 3   1   5]          [4]
    [ 1   4  -1]          [7]
```

`Av` for `v = [1, 4, 7]`:

- Row 1: `0(1) + (-2)(4) + 2(7) = 0 - 8 + 14 = 6`
- Row 2: `3(1) + 1(4) + 5(7) = 3 + 4 + 35 = 42`
- Row 3: `1(1) + 4(4) + (-1)(7) = 1 + 16 - 7 = 10`

So `Av = [6, 42, 10]` — worth double-checking against the notebook version, which had a
transcription slip (`10` vs `4` in one draft); redo this by hand once more as a sanity
check before trusting it in code.

Multiplying `A` (above) by a second 3×3 matrix `C = [[0,1,2],[3,4,5],[6,7,8]]` column by
column, using the same matrix-vector logic on each column of `C`, gives the columns of
the product `AC` — this is the "3D composition" mechanic in action, just applied three
times (once per column of `C`).

## Key takeaway

3D linear transformations aren't a separate topic from 2D ones — they're the same idea
(basis vectors define everything) with one more coordinate to track. The arithmetic gets
heavier, but the *why* doesn't change.
