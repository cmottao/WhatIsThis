# Numerical

## Problem 5

Function power of an integer raised to an integer.

**Input:**

Base $(b \in\mathbb{N})$

Exponent $(e \in\mathbb{N})$

**Output:**

Power $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
power: & \mathbb{N\times N} & \longrightarrow & \mathbb{N}\\
& (b,e) & \longmapsto & \begin{cases}
1 & \textrm{if }e=0\\
b×power(b,e-1) & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 6

A function that determines whether one number is divisible by another.

**Input:**

Dividend $(a \in\mathbb{N})$

Divisor $(b \in\mathbb{N})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
divisible: & \mathbb{N\times N} & \longrightarrow & \mathbb{B}\\
& (a,b) & \longmapsto & \begin{cases}
True & \textrm{si }mod(a, b) = 0\\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 7

Determine if a number is prime.

**Input:**

Number to evaluate $(n \in\mathbb{N})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
prime: & \mathbb{N} & \longrightarrow & \mathbb{B}\\
& (n) & \longmapsto & \begin{cases}
True & \textrm{si } \forall_{i=2}^{\sqrt{n}} mod(n,i)\neq0\\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 8

Given two natural, determine if they are relative primes.

**Input:**

First number to evaluate $(a \in\mathbb{N})$

Second number to evaluate $(b \in\mathbb{N})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
relativeprimes: & \mathbb{N\times N} & \longrightarrow & \mathbb{B}\\
& (a,b) & \longmapsto & \begin{cases}
True & \textrm{si }mcd(a, b) = 1\\
False & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 9

Determine if a number is a multiple of the sum of two others.

**Input:**

Number to evaluate $(a \in\mathbb{N})$

Number to evaluate $(x \in\mathbb{N})$

Number to evaluate $(y \in\mathbb{N})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
multiple: & \mathbb{N\times N\times N} & \longrightarrow & \mathbb{B}\\
& (a,x,y) & \longmapsto & divisible(a,x+y)
\end{array}
$$

## Problem 10

Given the coefficients of a polynomial of degree two, evaluate the polynomial at a given value.

**Input:**

Cuadratic coefficient $(a \in\mathbb{R})$

Linear coefficient $(b \in\mathbb{R})$

Constant coefficient $(c \in\mathbb{R})$

Number to evaluate $(x \in\mathbb{R})$

**Output:**

Value of the polynomial at that point $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
evaluate: & \mathbb{R\times R\times R\times R} & \longrightarrow & \mathbb{R}\\
& (a,b,c,x) & \longmapsto & ax^{2}+bx+c
\end{array}
$$

## Problem 11

**Input:**

Cuadratic coefficient $(a \in\mathbb{R})$

**Output:**

Linear coefficient of the derivate $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
coefficientlinearderivate: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (a) & \longmapsto & 2a
\end{array}
$$

## Problem 12

Given the coefficients of a polynomial of degree two and a real number, evaluate the derivative of polynomial in that number.

**Input:**

Cuadratic coefficient $(a \in\mathbb{R})$

Linear coefficient $(b \in\mathbb{R})$

Number to evaluate $(x \in\mathbb{R})$

**Output:**

Value of the derivate at that point $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
evaluatederivate: & \mathbb{R\times R\times R} & \longrightarrow & \mathbb{R}\\
& (a,b,x) & \longmapsto & 2ax+b
\end{array}
$$

## Problem 13

Given a natural, determine if it is a Fibonacci number or not.

**Input:**

Number to evaluate $(n \in\mathbb{R})$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
fibonacciaux: & \mathbb{N\times N \times N} & \longrightarrow & \mathbb{B}\\
& (n,a,b) & \longmapsto & \begin{cases}
True & \textrm{si }n=a\\
False & \textrm{si }n<a\\
fibonacciaux(n,b,a+b) & \textrm{in another case}
\end{cases}
\end{array}
$$

$$
\begin{array}{cccc}
fibonacci: & \mathbb{N} & \longrightarrow & \mathbb{B}\\
& (n) & \longmapsto & fibonacciaux(n,0,1)
\end{array}
$$
