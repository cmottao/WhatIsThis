# Strings

## Problem 71

Develop an algorithm that receives a character as input and outputs the number of occurrences of that character in a character string.

**Input:**

Character to search $(a \in\mathbb{ASCII})$

String $(b \in\mathbb{ASCII}^n)$

**Output:**

Number of occurrences of the character in the string $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
countOcurrences: & \mathbb{ASCCI}\times\mathbb{ASCII}^n & \longrightarrow & \mathbb{N}\\
& (a, b) & \longmapsto & \underset{x\in b}{\sum}\begin{cases}
1 & \textrm{if } a=x\\
0 & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 72

Develop an algorithm that takes two strings as input and determines if the first is substring of the second. (Do not use language-specific substring operations of programming).

**Input:**

Substring $(a \in\mathbb{ASCII}^n)$

String $(b \in\mathbb{ASCII}^m)$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
substring: & \mathbb{ASCCI}^n\times \mathbb{ASCCI}^m & \longrightarrow & \mathbb{B}\\
& (a, b) & \longmapsto & \begin{cases}
False & \textrm{if } n>m\\
\stackrel{n-m}{\underset{i=0}{\exists}} \stackrel{m-1}{\underset{j=0}{\forall}} b_{i+j}=a_j & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 73

Develop an algorithm that receives two character strings and determines if the first one is included in the second. A string is said to be included in another if all characters (with repetitions)  of the string is in the second string regardless of the order of the characters.

**Input:**

String to evaluate $(a \in\mathbb{ASCII}^n)$

String $(b \in\mathbb{ASCII}^m)$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
included: & \mathbb{ASCCI}^n\times \mathbb{ASCCI}^m & \longrightarrow & \mathbb{B}\\
& (a, b) & \longmapsto & \begin{cases}
False & \textrm{if } n>m\\
\underset{x\in a}{\forall} countOcurrences(x, a)\leq countOcurrences(x,b) & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 74

Develop an algorithm that reverses a string of characters.

**Input:**

String to reverse $(a \in\mathbb{ASCII}^n)$

**Output:**

Reverse string $(\in\mathbb{ASCII}^n)$

**Function:**

$$
\begin{array}{cccc}
reverseStringAux: & \mathbb{ASCCI}^n\times\ mathbb{N} & \longrightarrow & \mathbb{ASCII}^n\\
& (a,n) & \longmapsto & \begin{cases}
a_0 & \textrm{if } n=1\\
a_{n-1} + reverseStringAux(a, n-1) & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
reverseString: & \mathbb{ASCCI}^n & \longrightarrow & \mathbb{ASCII}^n\\
 & (a) & \longmapsto & reverseStringAux(a,n)
\end{array}
$$

## Problem 75

Develop an algorithm that determines if a character string is a palindrome. A chain it is called a palindrome if when inverted it is equal to itself.

**Input:**

String to evaluate $(a \in\mathbb{ASCII}^n)$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
palindrome: & \mathbb{ASCCI}^n & \longrightarrow & \mathbb{B}\\
& (a) & \longmapsto & \stackrel{\lfloor n/2\rfloor}{\underset{i=0}{\forall}} a_{i}=a_{n-i}
\end{array}
$$

## Problem 76

Develop an algorithm that determines if a character string is a palindrome sentence. A string is called a palindrome phrase if the string is palindrome when removing the spaces.

**Input:**

String to evaluate $(a \in\mathbb{ASCII}^n)$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
removeSpacesAux: & \mathbb{ASCCI}^n\times\mathbb{N} & \longrightarrow & \mathbb{ASCII}^*\\
& (a,n) & \longmapsto & \begin{cases}
a_0 & \textrm{if }n=1\\
removeSpacesAux(a,n-1) & \textrm{if }a_{n-1}=\textrm{" "}\\
removeSpacesAux(a,n-1)+a_{n-1} & \textrm{in another case}
\end{cases}
\end{array}
$$

---

$$
\begin{array}{cccc}
removeSpaces: & \mathbb{ASCCI}^{n} & \longrightarrow & \mathbb{ASCII}^*\\
& (a) & \longmapsto & removeSpacesAux(a,n))
\end{array}
$$

---

$$
\begin{array}{cccc}
palindromeSentence: & \mathbb{ASCCI}^n & \longrightarrow & \mathbb{B}\\
& (a) & \longmapsto & palindrome(removeSpaces(a))
\end{array}
$$

## Problem 77

Develop an algorithm that determines if a character string is a palindrome. A chain it is called a palindrome if when inverted it is equal to itself.

**Input:**

String to evaluate $(a \in\mathbb{ASCII}^n)$

**Output:**

True or False $(\in\mathbb{B})$

**Function:**

$$
\begin{array}{cccc}
palindrome: & \mathbb{ASCCI}^n & \longrightarrow & \mathbb{B}\\
& (a) & \longmapsto & \stackrel{\lfloor n/2\rfloor}{\underset{i=0}{\forall}} a_{i}=a_{n-i}
\end{array}
$$

