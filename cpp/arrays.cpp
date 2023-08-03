#include <iostream>
#include <vector>
#include <algorithm> // for sort()
using namespace std;

/*
    Useful functions.
*/

int gcd(int a, int b) {
    if(b > a) {
        return gcd(b, a);
    }
    else if(a % b == 0) {
        return b;
    }
    else {
        return gcd(b, a % b);
    }
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int power(int b, int e) {
    if(e == 0) {
        return 1;
    }
    else {
        return b * power(b, e - 1);
    }
}

vector<int> concatenateVectors(const vector<int> &a, const vector<int> &b) {
    vector<int> c = a;
    c.insert(a.end(), b.begin(), b.end());
    return a;
}


/*
    23. Develop an algorithm that calculates the sum of the elements of an array of real numbers.
*/

float sumArray(vector<float> a) {
    float s = 0;
    for(float x : a) {
        s += x;
    }
    return s;
}


/*
    24. Develop an algorithm that calculates the average of the elements of an array of real numbers.
*/

float averageArray(vector<float> a) {
    int n = a.size();
    return sumArray(a) / n;
}


/*
    25. Develop an algorithm that calculates the dot product of two arrays of real numbers of equal size.
*/

float dotProduct(vector<float> v, vector<float> w) {
    int n = v.size();
    int s = 0;
    for(int i = 0; i < n; i++) {
        s += v[i] * w[i];
    }
    return s;
}


/*
    26. Develop an algorithm that calculates the minimum of an array of real numbers.
*/

float minArrayAux(vector<float> a, int n) {
    if(n == 1) {
        return a[0];
    }
    else {
        return min(a[n - 1], minArrayAux(a, n - 1));
    }
}

float minArray(vector<float> a) {
    return minArrayAux(a, a.size());
}


/*
    27. Develop an algorithm that calculates the maximum of an array of real numbers.
*/

float maxArrayAux(vector<float> a, int n) {
    if(n == 1) {
        return a[0];
    }
    else {
        return max(a[n - 1], maxArrayAux(a, n - 1));
    }
}

float maxArray(vector<float> a) {
    return maxArrayAux(a, a.size());
}


/*
    28. Develop an algorithm that calculates the direct product of two arrays of real numbers of same size. 
*/

vector<float> directProduct(vector<float> v, vector<float> w) {
    int n = v.size();
    vector<float> u(n);
    for(int i = 0; i < n; i++) {
        u[i] = v[i] + w[i]; 
    }
    return u;
}


/*
    29. Develop an algorithm that determines the median of an array of real numbers. The median is the 
    number that remains in the middle of the array after being sorted.
*/

float medianArray(vector<float> a) {
    int n = a.size();
    sort(a.begin(), a.end());
    if (n % 2 != 0) {
        return a[n / 2];
    } else {
        return (a[n / 2] + a[n / 2 - 1]) / 2.0;
    }
}
    

/*
    30. Make an algorithm that counts all the zeros that appeared in said array.
*/

int countZeros(vector<float> a) {
    int n = a.size();
    int s = 0;
    for(int i = 0; i < n; i++) {
        if(a[i] == 0) {
            s++;
        }
    }
    return s;
}
   

/*
    31. Suppose that an array of integers is full of 1's and 0's and that the array represents a backwards 
    binary number. Make an algorithm that calculates the numbers in decimal that represents said array of 
    ones and zeros.
*/

int binaryToDecimal(vector<int> a) {
    int n = a.size();
    int s = 0;
    for(int i = 0; i < n; i++) {
        s += a[i] * power(2, i);
    }
    return s;
}


/*
    32. Make an algorithm that, given a nonnegative integer, creates an array of ones and zeros which 
    represents the number in binary backwards.
*/

vector<int> decimalToBinary(int n) {
    if(n < 2) {
        return {n};
    }
    else {
        return concatenateVectors({n % 2}, decimalToBinary(n / 2));
    }
}


/*
    33. Make an algorithm that calculates the Greatest Common Divisor (GCD) for an array of integers positives.
*/

int gcdArrayAux(vector<int> a, int n) {
    if(n == 1) {
        return a[0];
    }
    else {
        return gcd(a[n - 1], gcdArrayAux(a, n - 1));
    }
}

int gcdArray(vector<int> a) {
    return gcdArrayAux(a, a.size());
}


/*
    34. Make an algorithm that calculates the Least Common Multiple (LCM) for an array of integers positives.
*/

int lcmArrayAux(vector<int> a, int n) {
    if(n == 1) {
        return a[0];
    }
    else {
        return lcm(a[n - 1], lcmArrayAux(a, n - 1));
    }
}

int lcmArray(vector<int> a) {
    return lcmArrayAux(a, a.size());
}