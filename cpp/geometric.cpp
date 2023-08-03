#include <iostream> 
#include <cmath> // For sqrt() 
using namespace std;

/*
    14. Given the slope and the point of intersection of two lines, determine if they are parallel, 
    perpendicular or none of the above.
*/

string lines(float m1, float m2, float b1, float b2) {
    if((m1 == m2) && (b1 != b2)) {
        return "Parallel";
    }
    else if(m1 * m2 == -1) {
        return "Perpendicular";
    }
    else {
        return "Neither";
    }
}


/*
    15. Given the slope and the point of intersection at the origin of two lines, determine the point of 
    intersection beetwen the lines.
*/

pair<float, float> intersectionPoint(float m1, float m2, float b1, float b2) {
    float x = (b2 - b1) / (m1 - m2);
    if(m1 != m2) {
        return {x, (m1 * x) + b1};
    }
    else {
        return {}; 
    }
}


/*
    16. Given the radius of a circle, calculate the area of the triangle that circumscribes the circle 
    (triangle outside).
*/

float triangleArea(float r) {
    return 3 * sqrt(3) * (r * r);
}


/*
    17. Given the radius of a circle, calculate the area and perimeter of the square inside (inscribed in a 
    circle) and outside (inscribed in the circle).
*/

float squarePerimeterInside(float r) {
    return 4 * sqrt(2) * r;
}

float squareAreaInside(float r) {
    return 2 * (r * r);
}

float squarePerimeterOutside(float r) {
    return 8 * r;
}

float squareAreaOutside(float r) {
    return 4 * (r * r);
}


/*
    18. If a spider uses a regular hexagon pattern for its cobweb, and each hexagon is separated from the other 
    by 1cm, and the spider wants to make a web of πr2, how much cobweb does the spider require?
*/

float cobweb(float r) {
    return (6 * r) + (3 * r * (r + 1));
}