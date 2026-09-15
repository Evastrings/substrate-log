# Solution Sets vs. Column Space — Where the Domain/Range Analogy Breaks

## The hypothesis I tested
Treat `Ax = b` like a function `T(x) = Ax`, `T: Rⁿ → Rᵿ`, and map:
- solution set ("all x for a given b") → domain
- column span ("all b reachable from Ax") → range

## What's exactly right (not just analogous — definitional)
Col(A) **is** the range of T:

    Col(A) = { Ax : x ∈ Rⁿ } = Range(T)

This isn't a loose comparison. Range is *defined* as the set of outputs a function actually hits, and that's exactly what Col(A) is.

## Where it breaks
Domain has no "for a given b" attached to it — it's fixed:

    Domain(T) = Rⁿ

...independent of which b you're asking about. What I was actually describing — "all x's for a given b" — is the **preimage/fiber** of b, not the domain:

    T⁻¹(b) = { x ∈ Rⁿ : Ax = b }

That's the solution set. It's a *subset* of the domain, and it changes shape with b:
- if b ∉ Col(A): T⁻¹(b) = ∅
- if b ∈ Col(A): T⁻¹(b) = x_p + Null(A) (a particular solution + the null space — a coset)

So the solution set is never equal to the domain (a preimage of one point can't be the whole domain unless T is constant, and linear maps are only constant when A = 0).

## Corrected pairing

| My original term | What it actually is |
|---|---|
| Domain | Rⁿ — fixed, has nothing to do with b |
| "Solution set for given b" | Preimage/fiber T⁻¹(b) — a subset of the domain, depends on b |
| Column span | Range = Col(A) — this part was correct |

## Why this matters — the tie to Rank-Nullity
The domain is really the disjoint union of every fiber: for each b ∈ Col(A), its fiber is a nonempty coset of Null(A), and these cosets partition Rⁿ. (For b ∉ Col(A) the fiber is empty and contributes nothing.)

This is exactly why Rank-Nullity stitches the picture together:

    dim(domain) = dim(Null(A)) + dim(Col(A))

Null(A)'s dimension governs how "fat" each nonempty fiber is; the rank governs how much of Rᵐ those fibers collectively land on.

## Here's where I was wrong
I conflated "the set of x's I care about right now" with "the domain," when really the domain is the whole space Rⁿ and my solution set was just one slice of it (a fiber/coset). The fix: domain = fixed input space; solution set = preimage of a specific b, living inside that space.
