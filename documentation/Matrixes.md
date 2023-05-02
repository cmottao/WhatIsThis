# Matrixes

## Problem 50

Develop an algorithm that allows the addition of two matrices of real numbers (integers).

**Input:**

First matrix $(A \in\mathbb{R}^{n\times m})$

Second matrix $(B \in\mathbb{R}^{n\times m})$

**Output:**

Sum matrix $(C \in\mathbb{R}^{n\times m})$

**Function:**

$$
\begin{array}{cccc}
sumMatrix: & \mathbb{R^{n\times m}}\times \mathbb{R^{n\times m}} & \longrightarrow & \mathbb{R^{n\times\ m}}\\
& (A, B) & \longmapsto & C: \stackrel{n-1}{\underset{i=0}{\forall}} \stackrel{m-1}{\underset{j=0}{\forall}} C_{ij}=A_{ij}+B_{ij}
\end{array}
$$

## Problem 51

Develop an algorithm that allows multiplying two matrices of real numbers (integers).

**Input:**

First matrix $(A \in\mathbb{R}^{n\times m})$

Second matrix $(B \in\mathbb{R}^{m\times l})$

**Output:**

Multiplication matrix $(C \in\mathbb{R}^{n\times l})$

**Function:**

$$
\begin{array}{cccc}
multiplicationMatrix: & \mathbb{R^{n\times m}}\times \mathbb{R^{n\times m}} & \longrightarrow & \mathbb{R^{n\times\ m}}\\
& (A, B) & \longmapsto & C: \stackrel{n-1}{\underset{i=0}{\forall}} \stackrel{m-1}{\underset{j=0}{\forall}} C_{ij}= \stackrel{m-1}{\underset{k=0}{\sum}} A_{ik} \cdot B_{kj}
\end{array}
$$

## Problem 52

Develop a program that adds the elements of a given column of a matrix.

**Input:**

Matrix to evaluate $(A \in\mathbb{R}^{n\times m})$

Column index $(k \in\mathbb{N})$

**Output:**

Sum of column elements $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
columnSum: & \mathbb{R^{n\times m}}\times \mathbb{N} & \longrightarrow & \mathbb{R}\\
& (A, k) & \longmapsto & \stackrel{n-1}{\underset{i=0}{\sum}} A_{ik}
\end{array}
$$

## Problem 53

Develop a program that adds the elements of a given row of a matrix.

**Input:**

Matrix to evaluate $(A \in\mathbb{R}^{n\times m})$

Row index $(k \in\mathbb{N})$

**Output:**

Sum of row elements $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
rowSum: & \mathbb{R^{n\times m}}\times \mathbb{N} & \longrightarrow & \mathbb{R}\\
& (A, k) & \longmapsto & \stackrel{m-1}{\underset{i=0}{\sum}} A_{kj}
\end{array}
$$

## Problem 54

Develop an algorithm that determines if a matrix is ​​magic. A matrix is ​​said to square is magical if the sum of each of its rows, of each of its columns and of each diagonal is equal.

**Input:**

Matrix to evaluate $(A \in\mathbb{R}^{n\times m})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
magicMatrix: & \mathbb{R^{n\times m}} & \longrightarrow & \mathbb{B}\\
& (A) & \longmapsto & \stackrel{n-1}{\underset{i=1}{\forall}} rowSum(A,i) =x \land \stackrel{n-1}{\underset{j=1}{\forall}} rowColumn(A,j) = y \land x=y \land x=trace(A) \land x=secondaryTrace(A)
\end{array}
$$

$$
\begin{array}{c}
x=rowSum(A,0)\\
y=columnSum(A,0)
\end{array}
$$

## Problem 55

Develop an algorithm that, given an integer, replaces all numbers in a matrix greater than a given number by a one and all those less than or equal by a zero.

**Input:**

Matrix to make replacements $(A \in\mathbb{R}^{n\times m})$

Number to evaluate $(x \in\mathbb{R})$

**Output:**

Matrix with replaced elements $(B \in\left\{0,1\right\}^{n\times m})$

**Function:**

$$
\begin{array}{cccc}
replace: & \mathbb{R^{n\times m}}\times \mathbb{N} & \longrightarrow & \left\{0,1\right\}^{n\times m}\\
& (A, x) & \longmapsto & B:\stackrel{n-1}{\underset{i=0}{\forall}} \stackrel{m-1}{\underset{j=0}{\forall}} B_{ij}= \begin{cases}
1 & \textrm{if } A_{ij}>x\\
0 & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 56

Develop a program that calculates the determinant of a square matrix.

**Input:**

Matrix to evaluate $(A \in\mathbb{R}^{n\times n})$

**Output:**

Determinant $(\in \mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
determinant: & \mathbb{R^{n\times n}} & \longrightarrow & \mathbb{R}\\
& (A) & \longmapsto &
\end{array}
$$
