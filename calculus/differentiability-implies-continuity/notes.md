# Differentiability Implies Continuity

## Theorem

If a function `f` is differentiable at some point `c`, then `f` is also
continuous at `c`.

The converse is **false** — continuity does not imply differentiability.
(Classic counterexample: `f(x) = |x|` is continuous but not differentiable
at `x = 0`.)

## Definitions recap

- **Differentiable at c:** `lim(x→c) [f(x) − f(c)] / (x − c) = f'(c)` exists.
- **Continuous at c:** `lim(x→c) f(x) = f(c)`.

## Proof

Assume `f` is differentiable at `c`. Goal: show `lim(x→c) f(x) = f(c)`,
equivalently `lim(x→c) [f(x) − f(c)] = 0`.

```
lim(x→c) [f(x) − f(c)] = lim(x→c) [ (x − c) · (f(x) − f(c))/(x − c) ]
```

By the product rule for limits, this splits into two independent limits:

```
= [ lim(x→c) (x − c) ] · [ lim(x→c) (f(x) − f(c))/(x − c) ]
= 0 · f'(c)
= 0
```

The second factor is exactly the definition of `f'(c)`, which exists by
assumption (this is where differentiability is actually used). Since the
product is `0`, we get `lim(x→c) f(x) = f(c)`, so `f` is continuous at `c`. ∎

## Worked example using this machinery

`f(x) = log₃(x − 4x²)`

Using `y = log_a(x) → y' = 1/(x ln a)` combined with the chain rule:

```
f'(x) = (1 − 8x) / [(x − 4x²) ln 3]
```

## Note on terminology

A claim used as a stepping stone inside a larger proof — like the limit
splitting step above — is called a **lemma**.
