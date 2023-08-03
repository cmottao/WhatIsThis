# Geometric

## Problem 14

Given the slope and the point of intersection of two lines, determine if they are parallel, perpendicular or none of the above.

**Input:**

$m1:=$ Slope of line one $(\in \mathbb{R})$

$m2:=$ Slope of line two $(\in \mathbb{R})$

$b1:=$ Point of intersection of line one $(\in \mathbb{R})$

$b2:=$ Point of intersection of line two $(\in \mathbb{R})$

**Output:**

Relative position of the two lines: “Parallel”, “Perpendicular” or "Neither" $(\in \mathbb{ASCII^{*}})$

**Function:**

$$
\begin{array}{cccc}
lines: & \mathbb{R \times R \times R \times R} & \longrightarrow & \mathbb{ASCII^{*}} \\
& (m1, m2, b1, b2) & \longmapsto &
\begin{cases}
\textrm{"Parallel"} & \textrm{if } (m1 = m2) \land (b1 \neq b2) \\
\textrm{"Perpendicular"} & \textrm{if } m1 \cdot m2 = -1\\
\textrm{"Neither"} & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 15

Given the slope and the point of intersection at the origin of two lines, determine the point of intersection beetwen the lines.

**Input:**

$m1:=$ Slope of line one $(\in \mathbb{R})$

$m2:=$ Slope of line two $(\in \mathbb{R})$

$b1:=$ Point of intersection of line one $(\in \mathbb{R})$

$b2:=$ Point of intersection of line two $(\in \mathbb{R})$

**Output:**

Intersection point $((x, y) \in \mathbb{R \times R})$

**Helpers variables:**

$x:=$ x coordinate of intersection point $(\in \mathbb{R})$

$x = (b2 - b1) / (m1 - m2)$

**Function:**

$$
\begin{array}{cccc}
intersectionPoint: & \mathbb{R \times R \times R \times R} & \longrightarrow & \mathbb{R \times R} \\
& (m1, m2, b1, b2) & \longmapsto &
\begin{cases}
(x, (m1 \cdot x) + b1) & \textrm{if } m1 \neq m2 \\
\nexists & \textrm{in another case}
\end{cases}
\end{array}
$$

## Problem 16

Given the radius of a circle, calculate the area of ​​the triangle that circumscribes the circle (triangle outside).

**Input:**

$r:=$ Circle radius $(\in \mathbb{R^{+}})$

**Output:**

Area of ​​the triangle that circumscribes the circle $(\in \mathbb{R^{+}})$

**Function:**

$$
\begin{array}{cccc}
triangleArea: & \mathbb{R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& r & \longmapsto & 3 \cdot \sqrt{2} \cdot r^{2}
\end{array}
$$

## Problem 17

Given the radius of a circle, calculate the area and perimeter of the square inside (inscribed in a circle) and outside (inscribed in the circle).

**Input:**

$r:=$ Circle radius $(\in \mathbb{R^{+}})$

**Output:**

Perimeter of the square inscribed in the circle $(\in\mathbb{R^{+}})$

Area of ​​the square inscribed in the circle $(\in\mathbb{R^{+}})$

Perimeter of the square inscribing the circle $(\in\mathbb{R^{+}})$

Area of ​​the square inscribing the circle $(\in\mathbb{R^{+}})$

**Function:**

$$
\begin{array}{cccc}
squarePerimeterInside: & \mathbb{R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& r & \longmapsto & 4 \cdot \sqrt{2} \cdot r
\end{array}
$$

---

$$
\begin{array}{cccc}
squareaAreaInside: & \mathbb{R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& r & \longmapsto & 2 \cdot r^{2}
\end{array}
$$

---

$$
\begin{array}{cccc}
squarePerimeterOutside: & \mathbb{R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& r & \longmapsto & 8 \cdot r
\end{array}
$$

---

$$
\begin{array}{cccc}
squareAreaOutside: & \mathbb{R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& r & \longmapsto & 4 \cdot r^{2}
\end{array}
$$

## Problem 18

If a spider uses a regular hexagon pattern for its cobweb, and each hexagon is separated from the other by 1cm, and the spider wants to make a web of $πr2$, how much cobweb does the spider require?

**Input:**

$r:=$ Cobweb "radius" $(\in \mathbb{R^{+}})$

**Output:**

Amount of cobweb needed $(\in \mathbb{R^{+}})$

**Function:**

$$
\begin{array}{cccc}
cobweb: & \mathbb{R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& r & \longmapsto & 6 \cdot r + (3 \cdot r \cdot (r + 1))
\end{array}
$$
