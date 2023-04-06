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
\textrm{"Parallel"} & \textrm{if } m1 = m2 \wedge b1 \neq b2\\
\textrm{"Perpendicular"} & \textrm{if } m1 \cdot m2 = -1\\
\textrm{"Neither"} & \textrm{in another case}
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
intersectionPoint: & \mathbb{R\times R\times R\times R} & \longrightarrow & \mathbb{R\times R}\\
 & (m1, m2, b1, b2) & \longmapsto & \begin{cases}
(x, b1 + m1 \cdot x) & \textrm{if } m1 \neq m2\\
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
areaTriangle: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & (b \cdot h) / 2
\end{array}
$$

$$
\begin{array}{c}
b = 4 \cdot r\\
h = r \cdot \sqrt{12}
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
squarePerimeterInside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & l \cdot 4
\end{array}
$$

$$
\begin{array}{c}
l = r \cdot \sqrt{2}
\end{array}
$$

---

$$
\begin{array}{cccc}
squareaAreaInside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l^{2}
\end{array}
$$

$$
\begin{array}{c}
l = r \cdot \sqrt{2}
\end{array}
$$

---

$$
\begin{array}{cccc}
squarePerimeterOutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & l \cdot 4
\end{array}
$$

$$
\begin{array}{c}
l = r \cdot 2
\end{array}
$$

---

$$
\begin{array}{cccc}
squareAreaOutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l^{2}
\end{array}
$$

$$
\begin{array}{c}
l = r \cdot 2
\end{array}
$$

---

$$
\begin{array}{cccc}
pentagonPerimeterInside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l \cdot 5
\end{array}
$$

$$
\begin{array}{c}
k = r / 4\\
l = 2 \cdot k \cdot (\sqrt{10 - 2 \cdot \sqrt{5}})
\end{array}
$$

---

$$
\begin{array}{cccc}
pentagonAreaInside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & (pentagonPerimeterInside(r) \cdot apo) / 2
\end{array}
$$

$$
\begin{array}{c}
k = r / 4\\
apo = k \cdot (\sqrt{5} + 1)
\end{array}
$$

---

$$
\begin{array}{cccc}
pentagonPerimeterOutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l \cdot 5
\end{array}
$$

$$
\begin{array}{c}
k = r / (\sqrt{5} + 1)\\
l = 2 \cdot k \cdot (\sqrt{10 - 2 \cdot \sqrt{5}})
\end{array}
$$

---

$$
\begin{array}{cccc}
pentagonAreaOutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & (pentagonPerimeterOutside(r) \cdot apo) / 2
\end{array}
$$

$$
\begin{array}{c}
apo = r
\end{array}
$$

---

$$
\begin{array}{cccc}
hexagonPerimeterInside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
 & (r) & \longmapsto & l \cdot 6
\end{array}
$$

$$
\begin{array}{c}
apo = r
\end{array}
$$

---

$$
\begin{array}{cccc}
hexagonAreaInside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & (hexagonPerimeterInside(r) \cdot apo) / 2
\end{array}
$$

$$
\begin{array}{c}
k = r / 2\\
apo = k \cdot \sqrt{3}
\end{array}
$$

---

$$
\begin{array}{cccc}
hexagonPerimeterOutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & l \cdot 6
\end{array}
$$

$$
\begin{array}{c}
k = r / \sqrt{3}\\
l = k \cdot 2
\end{array}
$$

---

$$
\begin{array}{cccc}
hexagonAreaOutside: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & (hexagonPerimeterOutside(r) \cdot apo) / 2
\end{array}
$$

$$
\begin{array}{c}
apo = r
\end{array}
$$

## Problem 18

If a spider uses a regular hexagon pattern for its cobweb, and each hexagon is separated from the other by 1cm, and the spider wants to make a web of $πr2$, how much cobweb does the spider require?

**Input:**

Cobweb "radius" $(r \in\mathbb{R})$

**Output:**

Amount of cobweb needed $(cw \in\mathbb{R})$

Función:

$$
\begin{array}{cccc}
cobweb: & \mathbb{R} & \longrightarrow & \mathbb{R}\\
& (r) & \longmapsto & 6r+3a(a+1)
\end{array}
$$

$$
\begin{array}{c}
cw = 6r + \sum_{a=0}^{r} 6 \cdot a\\
= 6r + 6 a(a + 1) / 2\\
= 6r + 3a(a + 1)
\end{array}
$$
