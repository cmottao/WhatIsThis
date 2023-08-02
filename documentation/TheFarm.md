# The farm

A number of $C$ - Cows, $B$ - Birds (chickens and hens) and $S$ - Scorpions are bred on a farm. The cows are enclosed in a pen of $N \times M$ square meters, the birds in a barn and the scorpions in showcases.

## Problem 1

If a cow needs $G$ square meters of grass to produce $L$ liters of milk, how many liters of milk are produced on the farm?

**Input:**

$n:=$ Pen length $(\in \mathbb{R^{+}})$

$m:=$ Pen width $(\in \mathbb{R^{+}})$

$g:=$ Grass consumption $(\in \mathbb{R^{+}})$

$l:=$ Liters of milk $(\in \mathbb{R^{+}})$

**Output:**

Total production $(\in \mathbb{R^{+}})$

**Function:**

$$
\begin{array}{cccc}
milkProduction: & \mathbb{R^{+} \times R^{+} \times R^{+} \times R^{+}} & \longrightarrow & \mathbb{R^{+}} \\
& (n, m, g, l) & \longmapsto & (n \cdot m \cdot l) / g
\end{array}
$$

## Problem 2

If 1/3 of the birds on the farm are chickens, and half of the chickens lay 1 egg every 3 days and the other half 1 egg every 5 days, in a month how many eggs do they produce? (1 month ≡ 30 days).

**Input:**

$b:=$ Number of birds $(\in \mathbb{N})$

**Output:**

Total egg production in a month $(\in \mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
eggProduction: & \mathbb{N} & \longrightarrow & \mathbb{N} \\
& b & \longmapsto & \lfloor b \cdot (8 / 3) \rfloor
\end{array}
$$

## Problem 3

If the scorpions from the farm are sold to China, and there are scorpions of three different sizes: small (with a weight of 20 grams), medium (with a weight of 30 grams) and large (with weighing 50 grams), how many kilos of scorpions can be sold without decreasing the population to less than 2/3?

**Input:**

$s:=$ Number of small scorpions $(\in \mathbb{N})$

$m:=$ Number of medium scorpions $(\in \mathbb{N})$

$b:=$ Number of big scorpions $(\in \mathbb{N})$

**Output:**

Kilos that can be sold $(\in \mathbb{R^{+}})$

**Function:**

$$
\begin{array}{cccc}
scorpions: & \mathbb{N \times N \times N} & \longrightarrow & \mathbb{R^{+}} \\
& (s, m, b) & \longmapsto & ((s \cdot 0.02) + (m \cdot 0.03) + (b \cdot 0.05)) / 3
\end{array}
$$

## Problem 4

The farmer's corral was damaged and he doesn't know whether to re-enclose the corral with wood, wire or put a metal fence. If you are going to fence with wood you should put 4 rows of boards, with rod 8 rows and with wire only 5 rows, he wants to know what is the least expensive for fencing if you know that the barbed wire is worth $W$ per meter, the boards at $B$ per meter and the rods $R$ per meter. Given the size of the pen and the prices of the elements, what enclosure is the most economical?

**Input:**

$n:=$ Pen length $(\in \mathbb{R^{+}})$

$m:=$ Pen width $(\in \mathbb{R^{+}})$

$w:=$ Wire cost $(\in \mathbb{R^{+}})$

$b:=$ Board cost $(\in \mathbb{R^{+}})$

$r:=$ Rod cost $(\in \mathbb{R^{+}})$

**Output:**

Most economical enclosure: “Wire”, “Board” or “Rod” $(\in \mathbb{ASCII^{*}})$

**Helpers variables:**

$p:=$ Perimeter $(\in \mathbb{R^{+}})$

$p = 2 \cdot (n + m)$

$wc:=$ Wire enclosure cost $(\in \mathbb{R^{+}})$

$wc = 5 \cdot w \cdot p$

$bc:=$ Board enclosure cost $(\in \mathbb{R^{+}})$

$bc = 5 \cdot b \cdot p$

$rc:=$ Rod enclosure cost $(\in \mathbb{R^{+}})$

$rc = 8 \cdot r \cdot p$

**Function:**

$$
\begin{array}{cccc}
economical: & \mathbb{R^{+} \times R^{+} \times R^{+} \times R^{+} \times R^{+}} & \longrightarrow & \mathbb{ASCII}^{*} \\
& (n, m, w, b, r) & \longmapsto &
\begin{cases}
\textrm{"Wire"} & \textrm{if } (wc < bc) \land (wc < rc) \\
\textrm{"Board"} & \textrm{if } (bc < wc) \land (bc < rc) \\
\textrm{"Rod"} & \textrm{in another case}
\end{cases}
\end{array}
$$
