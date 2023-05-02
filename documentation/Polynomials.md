# Polynomials

A polynomial of degree $n$, such as $P(x) = a_nx^n + a_{n−1}x^{n−1} + ... + a_1x^1 + a_0x^0$ can be represented by means of an array of reals in the following way: $(a_0, a_1, ..., a_{n−1}, a_n)$.

Using this representation make a program that allows the user to read two polynomials and choose through a menu, one of the following operations on said polynomials:

## Problem 43 (Evaluate)

Reads a real and prints the evaluation of the two polynomials in said data.

**Input:**

Polynomial $(P \in\mathbb{R}^n)$

Number to evaluate $(x \in\mathbb{R})$

**Output:**

Value of the polynomial in that point $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
evaluate: & \mathbb{R}^n\times\mathbb{R} & \longrightarrow & \mathbb{R}\\
& (P,x) & \longmapsto & \stackrel{n-1}{\underset{i=0}{\sum}} P_i \cdot x^i
\end{array}
$$

## Problem 44 (Add)

Calculates the sum polynomial and prints it.

**Input:**

First polynomial $(P \in\mathbb{R}^n)$

Second polynomial $(Q \in\mathbb{R}^m)$

**Output:**

Sum polynomial $(R \in\mathbb{R})$

**Function:**

