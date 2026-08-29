# substrate-log

A public log of the math, CS, and algorithms foundations I'm building on the way to AI/ML engineering — specifically toward **[Amadeus](#north-star)**, a memory-enabled character AI, and toward roles at studios doing real generative-character work (Spellbrush, Shizuku AI).

Background: B.Eng Petroleum Engineering → AI/ML engineer, focused on anime AI, VTubers, and interactive narrative. This repo is the "substrate" layer — everything underneath the projects, made visible.

## Why this exists

Two reasons:

1. **Forced retrieval.** Writing a concept down and implementing it from scratch is real practice, not the illusion of comprehension you get from re-reading or watching. If I can't code it, I don't actually know it yet.
2. **Honest signal.** No one commits to a repo or stars it out of politeness. This is a build-in-public record — dated, unpolished, and real — that anyone (a hiring manager, a collaborator, future me) can check against the roadmap.

## Structure

Organized by **topic**, not by date, so it mirrors a knowledge graph rather than a diary:

```
substrate-log/
├── README.md
├── LEARNING_LOG.md          # running one-line-per-session log
├── linear-algebra/
│   ├── 01-row-reduction/
│   ├── 02-pivots-free-vars/
│   ├── 03-span-independence/
│   └── 04-column-null-space/
├── calculus/                # added when Phase 0 moves there
├── probability-statistics/  # added when Phase 0 moves there
├── algorithms/              # sorting, searching, data structures
└── ml-from-scratch/         # gradient descent, linear/logistic regression, etc.
```

Each concept folder contains:
- `notes.md` — the definition, the derivation, and the "aha" in my own words
- a small script implementing the concept from scratch (no libraries doing the actual work — that's the point)

## Principles this follows

Borrowed from Justin Skycak's writing on efficient learning (Math Academy):

- **Diagnostic first** — don't study what I already know; find the actual knowledge frontier.
- **Mastery before advancing** — if I can't consistently solve it correctly, I don't move on. I park it and come back.
- **Minimum effective dose + active practice** — every concept gets the least instruction needed, then immediate problem-solving / implementation.
- **Spaced review via new material** — advanced topics implicitly re-exercise earlier ones (e.g. implementing eigendecomposition re-exercises matrix multiplication and row reduction), so review is compressed into new building, not separate flashcard sessions.

## Current status

**Phase:** 0 — Foundations
**Focus:** Linear algebra (Interactive Linear Algebra, Margalit/Herman — Georgia Tech/Ximera), Python fundamentals (Khan Academy)
**Gate ahead:** Derive gradient descent by hand; implement linear regression from scratch, no libraries.

See [`LEARNING_LOG.md`](./LEARNING_LOG.md) for the running session-by-session record.

## North Star

**Amadeus** — a fine-tuned, memory-enabled AI character built on real ML substrate (not a system-prompt wrapper), inspired by Kurisu Makise from *Steins;Gate*. Everything in this repo is groundwork for getting there honestly.

## Following along

Build-in-public updates on X: *@hxdlab*
