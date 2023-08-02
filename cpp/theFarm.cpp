#include <iostream> 
using namespace std;

/*
    1. If a cow needs M square meters of grass to produce X liters of milk, how many liters of milk are produced 
    on the farm?
*/

float milkProduction(float n, float m, float g, float l) {
    return (n * m * l) / g;
}


/*
    2. If 1/3 of the birds on the farm are chickens, and half of the chickens lay 1 egg every 3 days and the 
    other half 1 egg every 5 days, in a month how many eggs do they produce? (1 month ≡ 30 days).
*/

int eggProduction(int b) {
    return b * (8.0 / 3.0);
}


/*
    3. If the scorpions from the farm are sold to China, and there are scorpions of three different sizes: small
    (with a weight of 20 grams), medium (with a weight of 30 grams) and large (with weighing 50 grams), how many 
    kilos of scorpions can be sold without decreasing the population to less than 2/3?
*/

float scorpions(int s, int m, int b) {
    return (float) ((s * 0.02) + (m * 0.03) + (b * 0.05)) / 3;
}


/*
    4. The farmer's corral was damaged and he doesn't know whether to re-enclose the corral with wood, wire or 
    put a metal fence. If you are going to fence with wood you should put 4 rows of boards, with rod 8 rows and 
    with wire only 5 rows, he wants to know what is the least expensive for fencing if you know that the barbed 
    wire is worth P per meter, the boards at Q per meter and the rods S per meter. Given the size of the pen and 
    the prices of the elements, what enclosure is the most economical?
*/

string economical(float n, float m, float w, float b, float r) {
    float p = 2 * (n + m);
    float wc = 5 * w * p;
    float bc = 4 * b * p;
    float rc = 8 * r * p;
    if((wc < bc) && (wc < rc)) {
        return "Wire";
    }  
    else if((bc < wc) && (bc < rc)) {
        return "Board";
    }
    else {
        return "Rod";
    }
}