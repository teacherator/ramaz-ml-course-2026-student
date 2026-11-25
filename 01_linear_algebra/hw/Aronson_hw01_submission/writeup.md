# HW01 Writeup — Matrices as Transformations

Finish Part 3, then run `uv run --frozen --python 3.11 python analysis.py` to generate `transforms.png`
and the printed values. Answer the three questions below using **your own**
figure and output. Replace each `[your answer here]` with your response.

---

## Question 1 (3 pts)

**What does each transformation change, and what does it preserve?**

Look at the rotation, scaling, and shear panels of your `transforms.png`.
For each of the three transformations, describe in a sentence or two:

- What changed about the arrow (size? angles? direction it points? proportions?).
- What stayed the same.


Rotation: The arrow turned counterclockwise by 60 degrees. Its size, proportions, and angles stayed the same.

Scaling: The arrow was stretched to twice its width and compressed to half its height. Its proportions changed, while the origin stayed fixed.

Shear: Points kept the same y-coordinate, while their x-coordinates shifted to the right in proportion to their height. This slanted the arrow and changed its angles, while points on the x-axis stayed in place.

---

## Question 2 (3 pts)

**Why are the R @ S and S @ R panels different?**

Both panels apply the *same* two matrices — a $60^\circ$ rotation and a
$(2, 0.5)$ scaling — to the *same* arrow, just in opposite order. Using your
figure and the printed matrices and arrow-tip positions:

- Describe how the two results differ.
- Explain *why* the order changes the outcome. Connect your explanation to the
  principle that $AB \neq BA$ in general. (Hint: in each
  composition, which transformation does the arrow experience first?)

In the first result, the arrow is first stretched to twice its width and compressed to half its height, then rotated. In the second, it is rotated first and then stretched and compressed along the coordinate axes.

The order changes the outcome because matrix multiplication is not commutative: $AB \neq BA$ in general. With column-vector transformations, the rightmost matrix acts first, so $R @ S$ scales and then rotates, while $S @ R$ rotates and then scales. Since the scaling is different in the x and y directions, doing it before or after rotation produces different results.


---

## Question 3 (4 pts)

**What does the matrix part of a dense neural-network layer do?**

A dense layer uses a weight matrix to transform its input vectors. Here,
consider only that matrix operation, before adding a bias or applying a
nonlinearity. Your Part 3 figure shows several $2 \times 2$ examples.

Using your own figure and printed output, explain:

- Choose one panel and describe what its matrix did geometrically. If $X$
  stores $N$ two-dimensional points as rows and the weight matrix $W$ has
  shape $(2, 2)$, what shape should the transformed points have? Explain how
  storing points in rows fits the lecture's column-vector expression $Wp$.
- Why can changing the order of two weight matrices change the output?
  Support your answer with your two arrow-tip positions from Question 2,
  identifying which transformation acts first in each composition.

The 60-degree rotation panel shows that the matrix rotates each point without changing the shape's size. If $X$ contains $N$ points as rows, its shape is $(N, 2)$. Applying the matrix to every point gives another $(N, 2)$ array: each row is transformed as a column-vector product $Wp$, written for row-stored points as $p^T W^T$.

The arrow tip starts at $(3, 0.5)$. Under $R @ S$, scaling acts first and the tip lands at approximately $(2.7835, 5.3210)$. Under $S @ R$, rotation acts first and the tip lands at approximately $(2.1340, 1.4240)$. These different positions show that changing the order of the two weight matrices can change the output.
