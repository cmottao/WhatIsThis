#include <iostream> 
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


/*
    5. Function power of an integer raised to an integer. 
*/

int power(int b, int e) {
    if(e == 0) {
        return 1;
    }
    else {
        return b * power(b, e - 1);
    }
}


/*
    6. A function that determines whether one number is divisible by another.
*/

bool divisible(int a, int b) {
    return a % b == 0;
}


/*
    7. Determine if a number is prime.
*/

bool prime(int n) {
    bool s = true;
    for(int i = 2; i < n; i++) {
        s &= (n % i != 0);
    }
    return s;
}


/*
    8. Given two natural, determine if they are relative primes.
*/

bool relativePrimes(int a, int b) {
    return gcd(a, b) == 1;
}


/*
    9. Determine if a number is a multiple of the sum of two others.
*/

bool multiple(int a, int x, int y) {
    return divisible(a, x + y);
}


/*
    10. Given the coefficients of a polynomial of degree two, evaluate the polynomial at a given value.
*/

float evaluate(float a, float b, float c, float x) {
    return (a * (x * x)) + (b * x) + c;
}


/*
    11. Given the coefficients of a polynomial of degree two, calculate the linear coefficient of the derivative.
*/

float coefficientLinearDerivate(float a) {
    return 2 * a;
}


/*
    12. Given the coefficients of a polynomial of degree two and a real number, evaluate the derivative of
    polynomial in that number.
*/

float evaluateDerivate(float a, float b, float x) {
    return (2 * a * x) + b;
}


/*
    13. Given a natural, determine if it is a Fibonacci number or not.
*/

bool fibonacciAux(int n, int a, int b) {
    if(n == a) {
        return true;
    }
    else if(n < a) {
        return false;
    }
    else {
        return fibonacciAux(n, b, a + b);
    }
}
    
bool fibonacci(int n) {
    return fibonacciAux(n, 0, 1);
}