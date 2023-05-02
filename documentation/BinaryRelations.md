# Binary relations

A matrix can be used to represent a relationship between two sets $A$ and $B$. It representation is as follows: If $A = \left\{x_0, x_1, x_2, .., x_{n-1}\right\}$ and $B = \left\{y_0, y_1, y_2, .., y_{m-1}\right\}$ a relation $R$ of $A$ on $B$ is represented by a matrix of ones and zeros of size ̃$n×m$, where $A_{ij} = 1$ if the element $x_i$ is related to the element $y_{j}$, otherwise $A_{ij} = 0$.

Using this representation make a program that allows the user to read two relationships between two sets and choose through a menu, one of the following operations on said relations:

## Problem 60 (Union)

Calculate and print the relation union.

**Input:**

First relation $(A \in\left\{0,1\right\}^{n \times m})$

Second relation $(B \in\left\{0,1\right\}^{n \times m})$

**Output:**

Union relation $(C \in\left\{0,1\right\}^{n \times m})$

**Function:**

$$
\begin{array}{cccc}
unionRelation: & \left\{0,1\right\}^{n\times m}\times\left\{0,1\right\} ^{n\times m} & \longrightarrow & \left\{ 0,1\right\} ^{n\times m}\\
& (A, B) & \longmapsto & C: \stackrel{n-1}{\underset{i=0}{\forall}} \stackrel{m-1}{\underset{j=0}{\forall}} C_{ij}\begin{cases}
1 & \textrm{if }A_{ij}=1\lor B_{ij}=1\\
0 & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 61 (Intersection)

Calculate and print the relation intersection.

**Input:**

First relation $(A \in\left\{0,1\right\}^{n \times m})$

Second relation $(B \in\left\{0,1\right\}^{n \times m})$

**Output:**

Intersection relation $(C \in\left\{0,1\right\}^{n \times m})$

**Function:**

$$
\begin{array}{cccc}
intersectionRelation: & \left\{0,1\right\}^{n\times m}\times\left\{0,1\right\} ^{n\times m} & \longrightarrow & \left\{ 0,1\right\} ^{n\times m}\\
& (A, B) & \longmapsto & C: \stackrel{n-1}{\underset{i=0}{\forall}} \stackrel{m-1}{\underset{j=0}{\forall}} C_{ij}\begin{cases}
1 & \textrm{if }A_{ij}=1\land B_{ij}=1\\
0 & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 62 (Simmetry)

Determines if the first relation is symmetric or not.

**Input:**

Relation to evaluate $(A \in\left\{0,1\right\}^{n \times m})$

**Output:**

True or False $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
isSimmetric: & \left\{ 0,1\right\} ^{n\times n} & \longrightarrow & \mathbb{B}\\
& (A) & \longmapsto & \stackrel{n-1}{\underset{i=0}{\forall}} \stackrel{m-1}{\underset{j=0}{\forall}} A_{ij}=A_{ji}
\end{array}
$$

## Problem 63 (Reflexivity)

Determines if the first relation is reflexive or not.

**Input:**

Relation to evaluate $(A \in\left\{0,1\right\}^{n \times m})$

**Output:**

True or False $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
isReflexive: & \left\{ 0,1\right\} ^{n\times n} & \longrightarrow & \mathbb{B}\\
& (A) & \longmapsto & \stackrel{n-1}{\underset{i=0}{\forall}} A_{ii}=1
\end{array}
$$

## Problem 64 (Transitivity)

Determines if the first relation read is transitive or not.

**Input:**

Relation to evaluate $(A \in\left\{0,1\right\}^{n \times m})$

**Output:**

True or False $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
isReflexive: & \left\{ 0,1\right\} ^{n\times n} & \longrightarrow & \mathbb{B}\\
& (A) & \longmapsto & \stackrel{n-1}{\underset{i=0}{\forall}} A_{ii}=1
\end{array}
$$