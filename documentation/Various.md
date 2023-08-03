# Various

## Problem 19

If in the UN they are pruning trees and each branch has $P$ leaves, and they removed $K$ from each tree branches, how many trees must be pruned to obtain $T$ leaves?

**Input:**

$p:=$ Leaves per branch $(\in \mathbb{N})$

$k:=$ Branches removed for each tree $(\in \mathbb{N})$

$t:=$ Number of leaves $(\in \mathbb{N})$

**Output:**

Number of trees that must be pruned $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
treeTriming: & \mathbb{N \times N \times N} & \longrightarrow & \mathbb{N} \\
& (p, k, t) & \longmapsto & \lfloor (t + (p \cdot k) - 1) / (p \cdot k) \rfloor
\end{array}
$$

## Problem 20

If a friend, not such a friend, lends me $K$ pesos at $i$ pesos of daily interest, how much will I pay him in a week if the interest is simple?

**Input:**

$k:=$ Amount of money $(\in \mathbb{R^{+}})$

$i:=$ Interest per day $(\in \mathbb{R^{+}})$

**Output:**

Total money to pay $(\in\mathbb{R^{+}})$

**Function:**

$$
\begin{array}{cccc}
simpleInterest: & \mathbb{R^{+} \times R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& (k, i) & \longmapsto & (k + i) \cdot 7

\end{array}
$$

## Problem 21

A child spent his time playing with lego tiles, he had two types of lego tiles, 1 × 1 squares (red) and 2 × 1 square tiles (blue), and given a base of 1 × n little squares, in how many different ways can you place the red and blue tiles on the base? What if they give you a yellow 1 × 3 tile?

**Input:**

$n:=$ Base length $(\in \mathbb{N})$

**Output:**

Different ways in which the tiles can be located $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
twoLego: & \mathbb{N} & \longrightarrow & \mathbb{N} \\
& n & \longmapsto &
\begin{cases}
1 & \textrm{if } n = 1\\
2 & \textrm{if } n = 2\\
twoLego(n - 1) + twoLego(n - 2) & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
threeLego: & \mathbb{N} & \longrightarrow & \mathbb{N} \\
& n & \longmapsto &
\begin{cases}
1 & \textrm{if } n = 1\\
2 & \textrm{if } n = 2\\
4 & \textrm{if } n = 3\\
threeLego(n - 1) + threeLego(n - 2) + threeLego(n - 3) & \textrm{in another case}
\end{cases}
\end{array}
$$
