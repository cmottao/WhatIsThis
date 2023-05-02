# Sets

An array of elements of type $\mathbb{T}$ can be used to represent a finite set of elements of type $\mathbb{T}$. This representation is as follows:

The set $A = \left\{x_0, x_1, x_2, .., x_{n-1}\right\}$ is represented as the array $(x_0, x_1, x_2, ..., x_{n−1})$.

Using this representation make a program that allows the user to read two sets of integers and choose through a menu, one of the following operations on them:

## Problem 35 (Union)

Calculates the union of the sets in an array and prints it.

**Input:**

First set $(A \in\mathbb{T}^*)$

Second set $(B \in\mathbb{T}^*)$

**Output:**

Union set $(C \in\mathbb{T}^*)$

**Function:**

$$
\begin{array}{cccc}
unionSet: & \mathbb{T}^*\times \mathbb{T}^* & \longrightarrow & \mathbb{T}^*\\
& (A, B) & \longmapsto & C=\left\{x\mid x\in A\vee x\in B\right\}
\end{array}
$$

## Problem 36 (Intersection)

Calculates the intersection of the sets in an array and prints it.

**Input:**

First set $(A \in\mathbb{T}^*)$

Second set $(B \in\mathbb{T}^*)$

**Output:**

Intersection set $(C \in\mathbb{T}^*)$

**Function:**

$$
\begin{array}{cccc}
intersectionSet: & \mathbb{T}^*\times \mathbb{T}^* & \longrightarrow & \mathbb{T}^*\\
& (A, B) & \longmapsto & C=\left\{x\mid x\in A\wedge x\in B\right\}
\end{array}
$$

## Problem 37 (Difference)

Calculates in an array the difference of the first with the second and prints it.

**Input:**

First set $(A \in\mathbb{T}^*)$

Second set $(B \in\mathbb{T}^*)$

**Output:**

Difference set $(C \in\mathbb{T}^*)$

**Function:**

$$
\begin{array}{cccc}
differenceSet: & \mathbb{T}^*\times \mathbb{T}^* & \longrightarrow & \mathbb{T}^*\\
& (A, B) & \longmapsto & C=\left\{ x\mid x\in A\wedge x\notin B\right\}
\end{array}
$$

## Problem 38 (Symmetric difference)

Calculates in an arrangement the symmetric difference of the sets and prints it.

**Input:**

First set $(A \in\mathbb{T}^*)$

Second set $(B \in\mathbb{T}^*)$

**Output:**

Symmetric difference set $(C \in\mathbb{T}^*)$

**Function:**

$$
\begin{array}{cccc}
symmetricDifferenceSet: & \mathbb{T}^*\times \mathbb{T}^* & \longrightarrow & \mathbb{T}^*\\
& (A, B) & \longmapsto & unionSet(differenceSet(A, B),differenceSet(B,A))
\end{array}
$$

## Problem 39 (Belongs)

Reads an integer and determines whether or not the element belongs to each of the sets and prints it.

**Input:**

Set $(A \in\mathbb{T}^*)$

Element to evaluate $(n \in\mathbb{T})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
belongs: & \mathbb{T}^*\times\mathbb{T} & \longrightarrow & \mathbb{B}\\
& (A,n) & \longmapsto & \begin{cases}
True & \textrm{if } \underset{x\in a}{\exists}=n\\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 40 (Content)

Determines if the first array is contained in the second and prints it.

**Input:**

First set $(A \in\mathbb{T}^*)$

Second set $(B \in\mathbb{T}^*)$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
content: & \mathbb{T}^*\times \mathbb{T}^* & \longrightarrow & \mathbb{B}\\
& (A, B) & \longmapsto & \begin{cases}
True & \textrm{if } intersectionSet(a,b) = a\\
False & \textrm{in another case}
\end{cases}
\end{array}
$$
