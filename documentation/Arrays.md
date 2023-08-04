# Arrays

## Problem 23

Develop an algorithm that calculates the sum of the elements of an array of real numbers.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

Sum of array elements $(\in \mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
sumArray: & \mathbb{R}^n & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & \underset{x \in a}{\sum} x
\end{array}
$$

## Problem 24

Develop an algorithm that calculates the average of the elements of an array of real numbers.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

Average of array elements $(\in \mathbb{R})$

**Function:** 

$$
\begin{array}{cccc}
averageArray: & \mathbb{R}^n & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & sumArray(a) / n
\end{array}
$$

## Problem 25

Develop an algorithm that calculates the dot product of two arrays of real numbers of equal size. Let v = (v1, v2, ..., vn) and w = (w1, w2, ..., wn) be two arrangements, the product of v and w (noted v ⋅ w) is the number: v1 ∗ w1 + v2 ∗ w2 + ⋯ + vn ∗ wn.

**Input:**

$v:=$ First array $(\in \mathbb{R}^n)$

$w:=$ Second array $(\in \mathbb{R}^n)$

**Output:**

Dot product $(\in \mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
dotProduct: & \mathbb{R}^n \times \mathbb{R}^n & \longrightarrow & \mathbb{R} \\
& (v, w) & \longmapsto & \stackrel{n - 1}{\underset{i = 0}{\sum}} v_{i} \cdot w_{i}
\end{array}
$$

## Problem 26

Develop an algorithm that calculates the minimum of an array of real numbers.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

Minimum of array $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
minArrayAux: & \mathbb{R}^n \times \mathbb{N} & \longrightarrow & \mathbb{R} \\
& (a, n) & \longmapsto &
\begin{cases}
a_{0} & \textrm{if } n = 1 \\
min(a_{n - 1}, minArrayAux(a, n - 1)) & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
minArray: & \mathbb{R}^n & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & minArrayAux(a, n)
\end{array}
$$

## Problem 27

Develop an algorithm that calculates the maximunm of an array of real numbers.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

Maximum of array $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
maxArrayAux: & \mathbb{R}^n \times \mathbb{N} & \longrightarrow & \mathbb{R} \\
& (a, n) & \longmapsto & 
\begin{cases}
a_{0} & \textrm{if } n = 1 \\
max(a_{n - 1}, maxArrayAux(a, n - 1)) & \textrm{in another case}
\end{cases}
\end{array}
$$

$$
\begin{array}{cccc}
maxArray: & \mathbb{R}^n & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & maxArrayAux(a, n)
\end{array}
$$

## Problem 28

Develop an algorithm that calculates the direct product of two arrays of real numbers of same size. Let v = (v1, v2, ..., vn) and w = (w1, w2, ..., wn) be two arrangements, the direct product of v and w (noted v ∗ w) is the vector: (v1 ∗ w1, v2 ∗ w2, ..., vn ∗ wn).

**Input:**

$v:=$ First array $(\in \mathbb{R}^n)$

$w:=$ Second array $(\in \mathbb{R}^n)$

**Output:**

$u:=$ Direct product $(\in \mathbb{R}^n)$

**Function:**

$$
\begin{array}{cccc}
directProduct: & \mathbb{R}^n \times \mathbb{R}^n & \longrightarrow & \mathbb{R}^n \\
& (v, w) & \longmapsto & u^n : u_{i} = v_{i} \cdot w_{i}
\end{array}
$$

## Problem 29

Develop an algorithm that determines the median of an array of real numbers. The median is the number that remains in the middle of the array after being sorted.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

Median of array $(\in\mathbb{R})$

**Helpers variables:**

$a:=$ a but sorted $(\in \mathbb{R}^n)$

$a = sort(a)$

**Function:**

$$
\begin{array}{cccc}
medianArray: & \mathbb{R^n} & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & 
\begin{cases}
a_{\lfloor n / 2 \rfloor} & \textrm{if } mod(n, 2) \neq 0 \\
(a_{\lfloor n / 2 \rfloor} + a_{\lfloor n / 2 \rfloor - 1}) / 2 & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 30

Make an algorithm that counts all the zeros that appeared in said array.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**:

Number of zeros in the array $(\in \mathbb{N})$

Función:

$$
\begin{array}{cccc}
countZeros: & \mathbb{R}^n & \longrightarrow & \mathbb{N} \\
& a & \longmapsto & \stackrel{n - 1}{\underset{i = 0}{\sum}} & 
\begin{cases}
1 & \textrm{if } a_{i} = 0 \\
0 & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 31

Suppose that an array of integers is full of ones and zeros and that the array represents a backwards binary number. Make an algorithm that calculates the numbers in decimal that represents said arrangement of ones and zeros.

**Input:**

$a:=$ Array representing the binary number $(\in {\lbrace 0, 1 \rbrace}^n)$

**Output:**

Number in decimal $(\in \mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
binaryToDecimal: & {\lbrace 0, 1 \rbrace}^n & \longrightarrow & \mathbb{N} \\
& a & \longmapsto & \stackrel{n - 1}{\underset{i = 0}{\sum}} a_{i} \cdot 2^i
\end{array}
$$

## Problem 32

Make an algorithm that, given a nonnegative integer, creates an array of ones and zeros which represents the number in binary backwards.

**Input:**

$n:=$ Number in decimal $(\in \mathbb{N})$

**Output:**

Array representing the binary number $(\in {\lbrace 0, 1 \rbrace}^*)$

**Function:**

$$
\begin{array}{cccc}
decimalToBinary: & \mathbb{N} & \longrightarrow & {\lbrace 0, 1 \rbrace}^* \\
& n & \longmapsto & 
\begin{cases}
[n] & \textrm{if } n < 2 \\
[mod(n, 2)] + decimaltoBinary(\lfloor n / 2 \rfloor) & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 33

Make an algorithm that calculates the Greatest Common Divisor ($gcd$) for an array of integers positives.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

$gcd$ of the array $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
gcdArrayAux: & \mathbb{N}^n \times \mathbb{N} & \longrightarrow & \mathbb{N} \\
& (a, n) & \longmapsto & 
\begin{cases}
a_{0} & \textrm{if } n = 1 \\
gcd(a_{n - 1}, gcdArrayAux(a, n - 1)) & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
gcdArray: & \mathbb{N}^n & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & gcdArrayAux(a, n)
\end{array}
$$

## Problem 34

Make an algorithm that calculates the Least Common Multiple ($lcm$) for an array of integers positives.

**Input:**

$a:=$ Array to evaluate $(\in \mathbb{R}^n)$

**Output:**

$lcm$ of the array $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
lcmArrayAux: & \mathbb{N}^n \times \mathbb{N} & \longrightarrow & \mathbb{N} \\
& (a, n) & \longmapsto & 
\begin{cases}
a_{0} & \textrm{if } n = 1 \\
lcm(a_{n - 1}, lcmArrayAux(a, n - 1)) & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
lcmArray: & \mathbb{N}^n & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & lcmArrayAux(a, n)
\end{array}
$$
