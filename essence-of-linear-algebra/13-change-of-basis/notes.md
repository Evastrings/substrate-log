# Chapter 13 — Change of basis

## Geometric intuition (3Blue1Brown)

> "Mathematics is the art of giving the same name to different things." — a paraphrase
> used to frame this chapter.

Everyone's numeric coordinates depend on an implicit choice of basis vectors. Two people
using *different* basis vectors for the same coordinate system will describe the exact
same physical vector using different numbers.

### Translating a vector between two people's bases ("Jennifer's basis")

If Jennifer's basis vectors, expressed in *your* coordinates, form a matrix `A`, then:

- `A` translates a vector described in **Jennifer's coordinates** into **your**
  coordinates.
- `A⁻¹` does the reverse — translates a vector from your coordinates into Jennifer's.

### Translating a *transformation* between bases

To apply a transformation `M` (defined in your coordinate system) to a vector that's
currently described in Jennifer's coordinates, and get the result back in Jennifer's
coordinates:

```
A⁻¹ M A
```

Read right to left: `A` converts Jennifer's vector into your coordinates, `M` applies the
transformation in your coordinates, and `A⁻¹` converts the result back into Jennifer's
coordinates. This composite matrix `A⁻¹MA` represents "the same transformation `M`, but
described entirely from Jennifer's point of view."

### Worked numeric example (own notes)

```
[2 -1]⁻¹ [0 -1] [2 -1] [-1]
[1  1]   [1  0] [1  1] [ 2]
```
is exactly this "translate in, transform, translate back" sandwich applied to a specific
vector — the general pattern behind every basis-change computation.

## Eigenbasis preview

`A⁻¹MA` is described as "some sort of mathematical eigenkin" in the notes — this hints at
Ch. 14: when the columns of `A` are chosen to be **eigenvectors** of `M`, the sandwiched
matrix `A⁻¹MA` becomes diagonal, dramatically simplifying computation (this is called an
**eigenbasis**).

## Key takeaway

A change of basis is a *translation problem*, not a fundamentally new kind of math — the
same vector or transformation can be described in infinitely many equivalent numeric
languages, and `A` / `A⁻¹` are literally translation dictionaries between two of them.
