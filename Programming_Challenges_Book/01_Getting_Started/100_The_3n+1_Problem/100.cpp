/*Santiago Zubieta*/
#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>

using namespace std;

void swap(int* a, int* b) {
// Call this function with swap(&a, &b) this will pass the pointers of the var-
// iables as a reference. Here, we put the value 'a' is pointing at into a temp
// then we put whatever 'b' is pointing at to whatever 'a' is pointing at, and
// then what 'a' the value was originally pointing at is put at 'b'
    int temp = *a;
    *a = *b;
    *b = temp;
}

int applyAlgorithm(int k) {
// Recursive definition for the 3n + 1 algorithm as defined in the problem sta-
// tement. If its even, divides by two. If its odd, multiplies by 3 and adds 1.
// If its 1, it has reached the bottom of the chain. For every recursive call,
// add 1 consumed step to the result.
    if(k == 1) {
        return 1;
    }
    if(k % 2 == 0) {
        k /= 2;    
    }
    else {
        k *= 3;
        k += 1;
    }
    return applyAlgorithm(k) + 1;
}

int main() {
// This program helps finding the number in a given range that has the longest 
// chain (and its length) when applying the '3n + 1' algorithm. This algorithm
// is, if a number is even, divide it by two. If its odd, multiply by 3 and add
// 1. It is conjectured (but not yet proven) that for every possible number the
// algorithm will always arrive to 1.
    int a, b;
    // Pair of numbers to be read
    bool swapped = false;
    // This will help keep track if numbers were swapped, since its easier to
    // have a single algorithm where we increment the first number until reach-
    // ing the second, and this requires the first number to be lower
    while(scanf("%d %d", &a, &b) != EOF) {
        swapped = false;
        if(b < a) {
            swapped = true;
            swap(&a, &b);
        }
        int maxSteps = 0;
        for(int k = a; k <= b; k++) {
            int steps = applyAlgorithm(k);
            if(steps > maxSteps) {
                maxSteps = steps;
            }
        }
        if(swapped == true) {
        // Swap the numbers back since in output it matters the order they were
        // originally given in the input, 201 210 != 210 201, may have the same
        // result but the output is strict in demanding their original order.
            swap(&a, &b);
        }
        printf("%d %d %d\n", a, b, maxSteps);
    }
}