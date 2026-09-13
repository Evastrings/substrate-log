# Derivatives of Exponential and Logarithmic Functions

## Deriving d/dx[aˣ] for any base a > 0

The trick: rewrite `aˣ` in terms of base `e`, using `a = e^(ln a)`:

```
aˣ = e^((ln a)·x)
```

Let `u = (ln a)x`, so `y = e^u`.

```
dy/du = e^u
du/dx = ln a
dy/dx = e^u · ln a = e^((ln a)x) · ln a = aˣ · ln a
```

**Result:** `d/dx[aˣ] = aˣ · ln a`

## Deriving d/dx[log_a(x)]

Change of base: `log_a(x) = ln(x) / ln(a)`

```
d/dx[ln(x)/ln(a)] = (1/ln a) · d/dx[ln x] = (1/ln a) · (1/x)
```

**Result:** `d/dx[log_a(x)] = 1 / (x ln a)`

## Worked examples

| Function | Derivative |
|---|---|
| `g(x) = 15·4ˣ` | `g'(x) = 15 ln(4)·4ˣ` |
| `p(x) = 5 log₉(x)` | `p'(x) = 5 / (x ln 9)` |
| `y = 7^(x²−x)` | `dy/dx = ln7 · (2x−1) · 7^(x²−x)` |
| `y = log₄(x²+x)` | `dy/dx = (2x+1) / ((x²+x) ln 4)` |
| `y = 5^(6x²−x+2)` | `dy/dx = 5^(6x²−x+2) · ln5 · (12x−1)` |
| `log₁₀(x²−1)` | `2x / ((x²−1) ln 10)` |

## Composed with the chain rule

**`y = ln(sin x)`:**
```
dy/dx = (1/sin x) · cos x = cot x
```
*(Notebook wrote this last step as `tan x` — see the flag in the chain rule
notes; `cos x / sin x` simplifies to `cot x`, not `tan x`.)*

**`y = ln(√x)`**, two ways:

1. Directly: `d/dx[ln(√x)] = (1/√x) · (1/(2√x)) = 1/(2x)`
2. Via substitution `u = √x`: `dy/du = 1/u`, `du/dx = 1/(2√x)`,
   so `dy/dx = (1/u)(1/(2√x)) = 1/(2x)`

Both methods agree — good consistency check for log-of-radical derivatives.

## Inverse relationship (graphical)

`y = 2ˣ` and `y = log₂(x)` are inverses of each other. Table of values for
`y = 2ˣ`:

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|----|
| y | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |

Reflecting this graph across `y = x` gives `log₂(x)`. This inverse
relationship is exactly why the two derivative formulas are structural
mirrors of each other — `ln a` appears as a **multiplier** for `aˣ` and as a
**divisor** for `log_a(x)`.
