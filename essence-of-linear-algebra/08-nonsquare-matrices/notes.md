# Chapter 8 — Nonsquare matrices as transformations between dimensions

## Geometric intuition (3Blue1Brown)

A non-square matrix represents a transformation **between different dimensions** — e.g.
a 3×2 matrix maps 2D vectors into 3D space (two columns = two input basis vectors, each
living in 3D output space); a 2×3 matrix maps 3D vectors down into 2D.

- Mapping 2D → 3D: the two input basis vectors land somewhere in 3D, and their span
  (generically) is a flat plane living inside 3D space.
- Mapping 3D → 2D (or more generally, mapping down to a smaller number of dimensions) is
  also possible — in that case, "squishing" happens, and the output can even collapse to
  the number line (1D), if every input basis vector is mapped to a scalar multiple of a
  single direction.
- The **null space** definition generalizes cleanly here too: it's simply the set of
  vectors that land on the origin after the transformation, regardless of whether the
  matrix is square.

## Key takeaway

Don't think of matrices as inherently "square objects that act on a fixed space." A
matrix's shape (rows × columns) literally encodes "input dimension → output dimension,"
and rectangular matrices are just as legitimate as square ones — they're the natural tool
for dimension-changing transformations (e.g. projecting 3D data into 2D, or embedding 2D
data into a higher-dimensional space).
