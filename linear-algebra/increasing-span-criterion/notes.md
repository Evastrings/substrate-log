# The Increasing Span Criterion — Theorem & Proof

## The statement
A set of vectors {v₁, v₂, ..., vₖ} is **linearly independent** if and only if every vector you add is *not* already in the span of the ones before it:

    vⱼ ∉ Span{v₁, ..., vⱼ₋₁}  for every j

Plain English: **every new vector must increase the size of the span.**

## Geometric intuition (build the set one vector at a time)
- Add v₁ = (1,0) → span = a line.
- Add v₂ = (0,1) → not in Span(v₁) → span grows to the whole plane. ✅ independent so far.
- Add v₃ = (1,1) → but (1,1) = 1·(1,0) + 1·(0,1), already in the span → span stays the plane. ❌ dependent.

So checking independence geometrically means: **did each new vector introduce a genuinely new direction?** — much easier to visualize than solving c₁v₁+...+cₖvₖ=0 directly.

## Why the proof goes the "opposite" direction
Proving *dependent ⇒ some vector was already redundant* is easier than proving *independent ⇒ every vector is new*, so the proof works with the contrapositive-style structure.

## The proof, step by step

**1. Assume dependent.** At least one vector can be written as a combination of the others:

    vⱼ = x₁v₁ + ... + xⱼ₋₁vⱼ₋₁ + xⱼ₊₁vⱼ₊₁ + ... + xₖvₖ

**2. Choose j = the *largest* index for which this is possible.** Not a guess — check every index, collect all indices where the vector is expressible via the others, and take the max of that list. (E.g., in v₁=(1,0), v₂=(0,1), v₃=(1,1): all three qualify, so j=3.)

**3. Suppose (for contradiction) vⱼ actually needs a *later* vector** — i.e., some coefficient xₖ ≠ 0 for k > j in that expression.

**4. Solve for vₖ instead** by rearranging:

    vₖ = -(1/xₖ)(x₁v₁ + ... - vⱼ + ...)

This shows vₖ is expressible using only vectors before it — so **k also qualifies** as a redundant index.

**5. Contradiction.** k > j, but j was supposed to be the *largest* qualifying index. Impossible.

**6. Conclusion.** The assumption in step 3 is false. vⱼ cannot depend on any later vector — it depends only on earlier ones:

    vⱼ ∈ Span{v₁, ..., vⱼ₋₁}

## Why "choose the largest j" is the whole trick
This is a proof by contradiction, not a proof that "banks on someone making an error." The logic:
- We *assume* vⱼ needs a later vector — a temporary hypothetical, like assuming "Alice isn't the tallest" to see what nonsense follows.
- If that hypothetical were true, algebra forces a later index (k) to also be redundant.
- That directly contradicts how j was defined (the *last* redundant one).
- So the hypothetical never held in the first place — not because of a computational slip, but because it's logically incompatible with j's definition.

If you ever *can* solve for a later vector, that's not "vⱼ made an error" — it means you picked the wrong j to begin with; the true largest redundant index is actually that later one.

## Detective-story version
"I'll choose the last person in line wearing a red hat — say, person 7." If someone then shows person 10 also wears a red hat, person 7 was never really the last one. Same structure: pick the last redundant vector, and any later "redundant" vector you find is a contradiction of that choice.

## Connecting the proof to the span-growth conclusion
The proof itself only establishes:

    dependent ⇒ vⱼ ∈ Span{v₁, ..., vⱼ₋₁}   (some vector already in the previous span)

The "span got bigger / didn't get bigger" language is a **translation**, not a new theorem:
- "vⱼ already in previous span" = "adding vⱼ doesn't change the span" (this is just what span means).
- So: dependent ⇒ some addition failed to enlarge the span.
- Take the contrapositive: if *every* addition enlarged the span ⇒ not dependent ⇒ independent.

That contrapositive step is exactly the blue-box statement. The theorem and its "geometric" restatement are two descriptions of the same fact, not two separate ideas.

## Here's where I was wrong (build-in-public note)
I initially conflated the proof's algebraic conclusion (vⱼ ∈ span of earlier vectors) with the span-growth language, treating them as if the growth language were an extra assumption. It isn't — "already in the span" and "doesn't enlarge the span" are the same statement, just worded differently. The contrapositive is what flips "dependent → some vector redundant" into "always-growing span → independent."

## Why this matters going forward
This theorem underpins bases, rank, column space, QR factorization, and why Gaussian elimination identifies pivot columns — the "new direction vs. redundant information" idea shows up constantly in ML linear algebra.

---

## Addendum: j and k are computed, not guessed (worked examples)

### What "index" means
Index = position label. In {v₁, v₂, v₃, v₄}, the index of v₃ is just 3 — no geometric meaning, purely "where in the list."

### What j and k actually are
- **j** — the *largest* index such that vⱼ can be written as a combination of the other vectors in the set. Defined by an actual check, not a guess.
- **k** — whatever later index (k > j) turns out to have a nonzero coefficient, *if* you mistakenly try to write vⱼ using a vector after it. Discovered while inspecting the equation, not chosen up front.

So j is fixed first by a real maximization; k only shows up inside the (doomed) hypothetical of step 3 of the proof.

### How to actually find j: check every index
Given a dependent set, test each vector: "can this one be written using the others?" Collect every index where the answer is yes, then j = the largest number in that list.

**Worked example 1** — v₁=(1,0), v₂=(0,1), v₃=(1,1), where v₃=v₁+v₂:
- v₁ = v₃ − v₂ → qualifies
- v₂ = v₃ − v₁ → qualifies
- v₃ = v₁ + v₂ → qualifies
- Qualifying list {1,2,3} → **j = 3**. No index above 3 exists, so there's no room to demonstrate the contradiction step here — j is already the last vector.

### Building a case where the contradiction step actually does work
Need a set where the redundant vector is *not* the last one, so there's a real later index to play k.

**Worked example 2** — v₁=(1,0), v₂=(0,1), v₃=(1,1), v₄=(2,2), where v₃=v₁+v₂ and v₄=2v₃=2v₁+2v₂:

Checking all four: every one qualifies (v₁=v₃−v₂, v₂=v₃−v₁, v₃=v₁+v₂, v₄=2v₁+2v₂). True **j = 4**.

Now deliberately test the *wrong* claim "j = 3" (as if v₄ had been missed):
1. Under this wrong claim, "the others" for v₃ includes v₄. Is v₃ expressible using v₄? Yes: v₃ = ½v₄.
2. This means x₄ = ½ ≠ 0 — a later index (4 > 3) has a nonzero coefficient. This is exactly the proof's "suppose vⱼ needs a later vector" setup.
3. Solve for v₄ instead: v₄ = (1/x₄)v₃ = 2v₃. So v₄ is expressible using only v₃ (index 3 < 4).
4. **Contradiction**: index 4 now also qualifies as "expressible via earlier vectors," but 4 > 3, and the wrong claim said 3 was the largest. The claim collapses.
5. This agrees with reality: the true j is 4, and indeed v₄ = 2v₃ uses only an earlier vector — consistent with the theorem's conclusion vⱼ ∈ Span{v₁,...,vⱼ₋₁}.

### The mechanism in one sentence
Any time you try to express the supposedly-largest vⱼ using a later vector, that same equation flips around to show the later vector is expressible via earlier ones — meaning *it* should have been picked as j instead. You can never legitimately need a later vector when defining vⱼ, because the attempt always hands you a bigger candidate for j.

### Here's where I was wrong (build-in-public note)
I initially treated j and k as things you could "claim" or freely pick to illustrate the proof (e.g., saying "let's say j=2"). They're not free choices — j is the output of an actual maximization over which indices qualify as redundant, and k only appears as a byproduct of a hypothetical that the proof goes on to destroy. Constructing an example where the contradiction step has real work to do required deliberately building a set where the redundant vector wasn't already the last one in the list.
