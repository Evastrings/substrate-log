# Chapter 15 — A quick trick for computing eigenvalues (2×2 case)

## Geometric intuition (3Blue1Brown)

For a 2×2 matrix, there's a shortcut that skips fully expanding the characteristic
polynomial, using two facts:

- **Mean of eigenvalues = mean of diagonal entries** (half the trace):
  ```
  (λ₁ + λ₂) / 2 = (a + d) / 2
  ```
- **Product of eigenvalues = determinant:**
  ```
  λ₁ · λ₂ = det(A) = ad - bc
  ```

Let `m = (a+d)/2` (the mean) and `p = ad - bc` (the product, i.e. the determinant). Then
the two eigenvalues are:

```
λ = m ± √(m² - p)
```

This comes directly from treating `λ₁, λ₂` as the two roots of a quadratic with known
sum (`2m`) and product (`p`) — same logic as "sum and product of roots" from basic
algebra, just applied to eigenvalues instead of an arbitrary quadratic's roots.

## Worked template

For `A = [a b; c d]`:

1. Compute `m = (a+d)/2`.
2. Compute `p = ad - bc`.
3. `λ = m ± √(m² - p)`.

Sanity-check against Ch. 14's example, `A = [2 2; 1 3]`:
- `m = (2+3)/2 = 2.5`
- `p = 2·3 - 2·1 = 4`
- `λ = 2.5 ± √(6.25 - 4) = 2.5 ± √2.25 = 2.5 ± 1.5` → `λ = 4` or `λ = 1` ✓ (matches the
  full characteristic-polynomial method from Ch. 14 exactly).

## Key takeaway

This trick is only a shortcut for 2×2 matrices — it doesn't generalize cleanly to larger
matrices, where you're stuck factoring the actual characteristic polynomial. Still useful
as a fast mental-math sanity check.
