# Numerical

## Problem 5

Function power of an integer raised to an integer.

**Input:**

$b:=$ Base $(\in \mathbb{N})$

$e:=$ Exponent $(\in \mathbb{N})$

**Output:**

Power $(\in \mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
power: & \mathbb{N \times N} & \longrightarrow & \mathbb{N} \\
& (b, e) & \longmapsto &
\begin{cases}
1 & \textrm{if } e = 0 \\
b \cdot power(b, e - 1) & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 6

A function that determines whether one number is divisible by another.

**Input:**

$a:=$ Dividend $(\in \mathbb{N})$

$b:=$ Divisor $(\in \mathbb{N})$

**Output:**

True if $a$ is divisible by $b$ or False if not $(\in \mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
divisible: & \mathbb{N\times N} & \longrightarrow & \mathbb{B} \\
& (a, b) & \longmapsto & \begin{cases}
True & \textrm{if } mod(a, b) = 0 \\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 7

Determine if a number is prime.

**Input:**

$n:=$ Number to evaluate $(\in \mathbb{N})$

**Output:**

True if $n$ is prime or False if not $(\in \mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
prime: & \mathbb{N} & \longrightarrow & \mathbb{B} \\
& n & \longmapsto & \begin{cases}
True & \textrm{if } \stackrel{n - 1}{\underset{i = 2}{\forall}} mod(n, i) \neq 0 \\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 8

Given two natural, determine if they are relative primes.

**Input:**

$a:=$ First number to evaluate $(\in \mathbb{N})$

$b:=$ Second number to evaluate $(\in \mathbb{N})$

**Output:**

True if $a$ and $b$ are relative primes or False if not $(\in \mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
relativePrimes: & \mathbb{N \times N} & \longrightarrow & \mathbb{B} \\
& (a, b) & \longmapsto &
\begin{cases}
True & \textrm{if } gcd(a, b) = 1 \\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 9

Determine if a number is a multiple of the sum of two others.

**Input:**

$a:=$ Number to evaluate $(\in \mathbb{N})$

$x:=$ Number to evaluate $(\in \mathbb{N})$

$y:=$ Number to evaluate $(\in \mathbb{N})$

**Output:**

True if $a$ is multiple of $x + y$ or False if not $(\in \mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
multiple: & \mathbb{N \times N \times N} & \longrightarrow & \mathbb{B} \\
& (a, x, y) & \longmapsto & divisible(a, x + y)
\end{array}
$$

## Problem 10

Given the coefficients of a polynomial of degree two, evaluate the polynomial at a given value.

**Input:**

$a:=$ Cuadratic coefficient $(\in \mathbb{R})$

$b:=$ Linear coefficient $(\in \mathbb{R})$

$c:=$ Constant coefficient $(\in \mathbb{R})$

$x:=$ Number to evaluate $(\in \mathbb{R})$

**Output:**

Value of the polynomial in $x$ $(\in \mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
evaluate: & \mathbb{R \times R \times R \times R} & \longrightarrow & \mathbb{R} \\
& (a, b, c, x) & \longmapsto & ax^{2} + bx + c
\end{array}
$$

## Problem 11

Given the coefficients of a polynomial of degree two, calculate the linear coefficient of the derivative.

**Input:**

$a:=$ Cuadratic coefficient $(\in \mathbb{R})$

**Output:**

Linear coefficient of the derivate $(\in \mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
coefficientLinearDerivate: & \mathbb{R} & \longrightarrow & \mathbb{R} \\
& a & \longmapsto & 2a
\end{array}
$$

## Problem 12

Given the coefficients of a polynomial of degree two and a real number, evaluate the derivative of polynomial in that number.

**Input:**

$a:=$ Cuadratic coefficient $(\in \mathbb{R})$

$b:=$ Linear coefficient $(\in \mathbb{R})$

$x:=$ Number to evaluate $(\in \mathbb{R})$

**Output:**

Value of the derivate in $x$ $(\in \mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
evaluateDerivate: & \mathbb{R \times R \times R} & \longrightarrow & \mathbb{R} \\
& (a, b, x) & \longmapsto & 2ax + b
\end{array}
$$

## Problem 13

Given a natural, determine if it is a Fibonacci number or not.

**Input:**

$n:=$ Number to evaluate $(\in \mathbb{N})$

**Output:**

True if $n$ is a Fibonacci number or False if not $(\in \mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
fibonacciAux: & \mathbb{N \times N \times N} & \longrightarrow & \mathbb{B} \\
& (n, a, b) & \longmapsto &
\begin{cases}
True & \textrm{if } n = a \\
False & \textrm{if } n < a \\
fibonacciAux(n, b, a + b) & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
fibonacci: & \mathbb{N} & \longrightarrow & \mathbb{B} \\
& n & \longmapsto & fibonacciAux(n, 0, 1)
\end{array}
$$
