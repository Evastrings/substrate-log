# The Chain Rule

## Statement

```
d/dx [f(g(x))] = f'(g(x)) · g'(x)
```

For nested (triple) compositions:

```
d/dx [f(g(h(x)))] = f'(g(h(x))) · g'(h(x)) · h'(x)
```

## Mechanics

- Differentiate the **outer** function first, leaving the inner function(s)
  untouched inside it.
- Multiply by the derivative of the inner function.
- Repeat once per extra layer of nesting — each layer contributes one more
  factor.

## Worked examples

**Basic:** `h(x) = (sin x)² = sin²x`
`h'(x) = 2 sin x · cos x`

**Triple composition:** `f(x) = cos³(x)`
`f'(x) = 3cos²(x) · (−sin x) = −3 sin x cos²x`

**Square root of trig:** `h(x) = √(sin x)`
`h'(x) = cos x / (2√(sin x))`

**tan of a power:** `y = tan(x²)`
`dy/dx = 2x · sec²(x²)`

**tan of a square root:** `y = tan(√x)`
`dy/dx = sec²(√x) / (2√x)`

**tan²:** `y = tan²x`
`dy/dx = 2 tan x · sec²x`

**Nested radical (generalized power rule):**
`d/dx[ ⁴√(x³ + 4x² + 7) ] = (3x² + 8x) / (4 · ⁴√((x³+4x²+7)³))`

Worked via substitution `u = x³ + 4x² + 7`, `y = u^(1/4)`, then
`dy/dx = (1/4)u^(−3/4) · du/dx`.

**Three-layer nested trig:** `sec(3π / (2 − x))`

Let `u = 3π(2−x)⁻¹` and `v = 2−x`.
`du/dv = −3π·v⁻²`, `dv/dx = −1`

```
dy/dx = sec(u)tan(u) · (−3π v⁻²) · (−1) = sec(u)tan(u) · 3π(2−x)⁻²
```

Evaluated at `x = π/4`, this reduces (via the unit circle at `5π/4`) to `−√2`.

## Evaluating chain-rule derivatives from given data points

Recurring pattern: given `h(2) = −1`, `h'(2) = 6`, `f'(−1) = −5`, and
`G(x) = f(h(x))`:

```
G'(2) = f'(h(2)) · h'(2) = f'(−1) · 6 = (−5)(6) = −30
```

Rule of thumb: **outer derivative evaluated at the inner function's value,
times the inner derivative** — same pattern regardless of what the functions
are named (`f∘g`, `g∘h`, `H = g(h(x))`, etc.).

## Identifying the components of a composite function

Given a target like `cos(sin(x) + 1)`, decompose into:
- outer: `g(x) = cos(x)`
- inner: `h(x) = sin(x) + 1`

Given `f(x) = 1 + x`, `g(x) = cos(x)`: `f(g(x)) = 1 + cos(x)`.

## Flag for review

One notebook line simplifies `cos(x)/sin(x)` as `tan(x)` inside a
`ln(sin x)` derivative (see the exponential/log notes). `cos(x)/sin(x)`
is actually `cot(x)`, not `tan(x)` — worth re-deriving that step to check
whether it's a transcription slip or an actual reasoning error.
