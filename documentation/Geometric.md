# Geometric

## Problem 14

Given the slope and the point of intersection of two lines, determine if they are parallel, perpendicular or none of the above.

**Input:**

Slope of line one $(m1 \in\mathbb{R})$

Slope on line two $(m2 \in\mathbb{R})$

Point of intersection of line one $(b1 \in\mathbb{R})$

Point of intersection of line two $(b2 \in\mathbb{R})$

**Output:**

“Parallel” or “Perpendicular” or "Neither" $(\in\mathbb{ASCII^{*}})$

**Function:**

$$
\begin{array}{cccc}
lines: & \mathbb{R\times R\times R\times R} & \longrightarrow & \mathbb{ASCII^{*}}\\
& (m1, m2, b1, b2) & \longmapsto & \begin{cases}
"Parallel" & \textrm{if } m1 = m2 \wedge b1 \neq b2\\
"Perpendicular" & \textrm{if } m1 × m2 = -1\\
"Neither" & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 15

Given the slope and the point of intersection of two lines, determine the points of intersection at origin.

**Input:**

Slope of line one $(m1 \in\mathbb{R})$

Slope on line two $(m2 \in\mathbb{R})$

Point of intersection of line one $(b1 \in\mathbb{R})$

Point of intersection of line two $(b2 \in\mathbb{R})$

**Output:**

Intersection point $((x, y) \in\mathbb{R\times R})$

**Function:**

$$
\begin{array}{cccc}
intersectionpoint: & \mathbb{R\times R\times R\times R} & \longrightarrow & \mathbb{R\times R}\\
 & (m1, m2, b1, b2) & \longmapsto & \begin{cases}
(x, b1 + m1 × x) & \textrm{if } m1 \neq m2\\
\nexists & \textrm{in another case}
\end{cases}
\end{array}
$$

$$
\begin{array}{c}
x = (b2 - b1) / (m1 - m2)
\end{array}
$$

## Problem 16

Given the radius of a circle, calculate the area of ​​the triangle that circumscribes the circle (triangle outside).

**Input:**

Circle radius $(r \in\mathbb{R})$

**Output:**

Area of ​​the triangle that circumscribes the circle $( \in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
areatriangle: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & (b × h) / 2
\end{array}
$$

$$
\begin{array}{c}
b = 4 × r\\
h = r × \sqrt{12}
\end{array}
$$

## Problem 17

Given the radius of a circle, calculate the area and perimeter of the square, pentagon, and hexagon inside (inscribed in a circle) and outside (inscribed in the circle).

**Input:**

Circle radius $(r \in\mathbb{R})$

**Output:**

Perimeter of the square inscribed in the circle $(\in\mathbb{R})$

Area of ​​the square inscribed in the circle $(\in\mathbb{R})$

Perimeter of the square inscribing the circle $(\in\mathbb{R})$

Area of ​​the square inscribing the circle $(\in\mathbb{R})$

Perimeter of the pentagon inscribed in the circle $(\in\mathbb{R})$

Area of ​​the pentagon inscribed in the circle $(\in\mathbb{R})$

Perimeter of the pentagon inscribing the circle $(\in\mathbb{R})$

Area of ​​the pentagon inscribing the circle $(\in\mathbb{R})$

Perimeter of the hexagon inscribed in the circle $(\in\mathbb{R})$

Area of ​​the hexagon inscribed in the circle $(\in\mathbb{R})$

Perimeter of the hexagon inscribing the circle $(\in\mathbb{R})$

Area of ​​the hexagon inscribing the circle $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
squareperimeterinside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & l × 4
\end{array}
$$

$$
\begin{array}{c}
l = r × \sqrt{2}
\end{array}
$$

$$
\begin{array}{cccc}
square\_area\_inside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l^{2}
\end{array}
$$

$$
\begin{array}{c}
l = r × \sqrt{2}
\end{array}
$$

$$
\begin{array}{cccc}
squareperimeteroutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & l × 4
\end{array}
$$

$$
\begin{array}{c}
l = r × 2
\end{array}
$$

$$
\begin{array}{cccc}
squareareaoutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l^{2}
\end{array}
$$

$$
\begin{array}{c}
l = r × 2
\end{array}
$$

$$
\begin{array}{cccc}
pentagonperimeterinside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l × 5
\end{array}
$$

$$
\begin{array}{c}
k = r / 4\\
l = 2 × k × (\sqrt{10 - 2 × \sqrt{5}})
\end{array}
$$

$$
\begin{array}{cccc}
pentagonareainside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & (apo + pentagonperimeterinside(r)) / 2
\end{array}
$$

$$
\begin{array}{c}
k = r / 4\\
apo = k × (\sqrt{5} + 1)
\end{array}
$$

$$
\begin{array}{cccc}
pentagonperimeteroutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l × 5
\end{array}
$$

$$
\begin{array}{c}
k = r / (\sqrt{5} + 1)\\
l = 2 × k × (\sqrt{10 - 2 × \sqrt{5}})
\end{array}
$$

$$
\begin{array}{cccc}
pentagonareaoutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & (apo + pentagonperimeteroutside(r)) / 2
\end{array}
$$

$$
\begin{array}{c}
apo = r
\end{array}
$$

$$
\begin{array}{cccc}
hexagonperimeterinside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l × 6
\end{array}
$$

$$
\begin{array}{c}
apo = r
\end{array}
$$

$$
\begin{array}{cccc}
hexagonareainside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & (apo + hexagonperimeterinside(r)) / 2
\end{array}
$$

$$
\begin{array}{c}
k = r / 2\\
apo = k × \sqrt{3}
\end{array}
$$

$$
\begin{array}{cccc}
hexagonperimeteroutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & l × 6
\end{array}
$$

$$
\begin{array}{c}
k = r / \sqrt{3}\\
l = k × 2
\end{array}
$$

$$
\begin{array}{cccc}
hexagonareaoutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & (apo + hexagonperimeteroutside(r)) / 2
\end{array}
$$

$$
\begin{array}{c}
apo = r
\end{array}
$$
