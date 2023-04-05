# Documentation of the problems

## The farm

A number of $V$ - Cows, $A$ - Birds (chickens and hens) and $E$ - Scorpions are bred on a farm. The cows are enclosed in a pen of $N × M$ square meters, the birds in a barn and the scorpions in showcases.

### Problem 1

If a cow needs $M$ square meters of grass to produce $X$ liters of milk, how many liters of milk are produced on the farm?

**Input:**

Pen length $(n \in\mathbb{R})$

Pen width $(m \in\mathbb{R})$

Grass consumption $(c \in\mathbb{R})$

Liters of milk $(l \in\mathbb{R})$

**Output:**

Total production $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
milk\textrm{\_}produced: & \mathbb{R\times R\times R\times R} & \longrightarrow & \mathbb{R}\\
& (n,m,c,l) & \longmapsto & l×n×m/c
\end{array}
$$

### Problem 2

If 1/3 of the birds on the farm are chickens, and half of the chickens lay 1 egg every 3 days and the other half 1 egg every 5 days, in a month how many eggs do they produce? (1 month ≡ 30 days).

**Input:**

Birds $(a \in\mathbb{N})$

**Output:**

Total egg production in a month $(\in\mathbb{N})$

**Function:**

$$
\begin{array}{cccc}
egg \textrm{\_} production: & \mathbb{N} & \longrightarrow & \mathbb{N}\\
& (a) & \longmapsto & (gt×10)+(gc×6)
\end{array}
$$

$$
\begin{array}{c}
g = a\\
gt = g/2\\
gc = g/2
\end{array}
$$

### Problem 3

If the scorpions from the farm are sold to China, and there are scorpions of three different sizes: small (with a weight of 20 grams), medium (with a weight of 30 grams) and large (with weighing 50 grams), how many kilos of scorpions can be sold without decreasing the population to less than 2/3?

**Input:**

Small scorpions $(s \in\mathbb{N})$

Medium scorpions $(m \in\mathbb{R})$

Big scorpions $(b \in\mathbb{R})$

Liters of milk $(l \in\mathbb{R})$

**Output:**

Kilos that can be sold $(\in\mathbb{R})$

**Function:**

$$
\begin{array}{cccc}
escorpions: & \mathbb{N\times N\times N} & \longrightarrow & \mathbb{N}\\
& (s,m,b) & \longmapsto & kgtotal/3
\end{array}
$$

$$
ks = 0.02 × s \\

km = 0.03 × m \\

kb = 0.05 × b \\

kgtotal = ks + km + kb
$$

### Problem 4

The farmer's corral was damaged and he doesn't know whether to re-enclose the corral with wood, wire or put a metal fence. If you are going to fence with wood you should put 4 rows of boards, with rod 8 rows and with wire only 5 rows, he wants to know what is the least expensive for fencing if you know that the barbed wire is worth P per meter, the boards at Q per meter and the rods S per meter. Given the size of the pen and the prices of the elements, what enclosure is the most economical?

**Input:**

Pen length $(n \in\mathbb{R})$

Pen width $(m \in\mathbb{R})$

Wire cost $(a \in\mathbb{R})$

wood board $(t \in\mathbb{R})$

Costo de la varilla $(v \in\mathbb{R})$

**Output:**

“Alambre” o “Tabla” o “Varilla” $(\in\mathbb{ASCII}^{*})$

**Function:**

$$
\begin{array}{cccc}
economia: & \mathbb{R\times R\times R\times R\times R} & \longrightarrow & \mathbb{ASCII}^{*}\\
 & (n,m,a,t,v) & \longmapsto & \begin{cases}
"Alambre" & \textrm{si ca < ct }{\land}\textrm{ ca < cv}\\
"Tabla"  & \textrm{si ct < ca }{\land}\textrm{ ct < cv}\\
"Varilla" & \textrm{si cv < ct }{\land}\textrm{ cv < ca}
\end{cases}
\end{array}
$$

$$
ks = 0.02 × s \\

km = 0.03 × m \\

kb = 0.05 × b \\

kgtotal = ks + km + kb
$$
