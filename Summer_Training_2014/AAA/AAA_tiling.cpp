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

int tileNum(int n) {
// The recursive definition of tile numbers, which is VERY SLOW and fucks up
// for really large numbers, but helps to identify the 'almost' fibonacciesque
// nature of this problem.
    if(n < 0) {
    // It will be lower than 0 if we attempt to put a width->2 piece and only
    // have a single space remaining, so ignore the width-> placement then.
        return 0;
    }
    if(n == 0) {
    // A leaf, with counts as a unique combination.
        return 1;
    }
    int sum = 0;
    // Possible tiles:
    // |||  : width->2 *
    // | |  : width->2
    // |-|  : width->2
    // ||   : width->1 *
    // The ones with * are basically the same, consider just the smaller one. 
    sum += 1 * tileNum(n - 1);
    // Consume only one horizontal space, will add only one multiplier to the
    // sub-tree amount since there is only one width->1 possible block.
    sum += 2 * tileNum(n - 2);
    // Consume two horizontal spaces, will add two multipliers to the sub-tree
    // amount, one may think that there are three possible width->2 blocks, but
    // one of these is simply the width-1 block repeated twice.
    return sum;
}

string combinations[255];

string sum(string a, string b) {
// To add VERY LARGE NUMBERS using strings.
    if(a.length() != b.length()) {
    // If both numbers are different in length, lets pad the smaller one with 0
        if(a.length() < b.length()) {
        // Change a and b if a is smaller, since we'll asume b is smaller so
        // we can pad it later with 0s, and know that b will be the one to pad.
            string temp;
            temp = a;
            a = b;
            b = temp;
        }
        int diff = a.length() - b.length();
        for(int k = 0; k < diff; k++) {
        // Pad b with 0s to the left depending on the difference in the lengths
            b = "0" + b;
        }
    }
    string num = "";
    bool carry = false;
    for(int k = a.length() - 1; k >= 0; k--) {
    // Add up each decimal place from the right to the left, and keeping record
    // of the carry value in case it does occur when adding up both the numbers
        int n1 = a[k] - '0';
        int n2 = b[k] - '0';
        int res = n1 + n2 + carry;
        carry = ((res / 10) > 0);
        res %= 10;
        num = (char)(res + '0') + num;
    }
    if(carry) {
    // If there's a final carry put an extra 1 to the left of the resulting num
        num = "1" + num;
    }
    return num;
}

string mult(string s, int n) {
// Multiplication is simply defined as a repeated sum, for VERY LARGE NUMBERS
    string res = "0";
    for(int k = 0; k < n; k++) {
        res = sum(res, s);
    }
    return res;
}

void initCombinations() {
    // Precomputed list of cuasi fibonacci numbers. Since they are WAY TOO BIG,
    // I've preferred to calculate them using strings to add up or multiply
    // VERY LARGE NUMBERS.
    combinations[0] = "1";
    // I don't yet understand with for a width->0 block there is 1 possible
    // combination instead of none. I guess its just by mathematical definition
    combinations[1] = "1";
    for(int k = 2; k < 255; k++) {
        string n1 = combinations[k - 1];
        string n2 = combinations[k - 2];
        n2 = mult(n2, 2);
        combinations[k] = sum(n1, n2);
    }
}

int main() {
    int N;
    // Each test case to be read until the EOF
    initCombinations();
    while (cin >> N) {
        // cout << tileNum(N) << endl;
        // This would give the result but its WAY TOO SLOW. What I've just 
        // realized is that this could be given in terms of the subproblem of
        // 1 possible tiles of width 1 and 2 possible tiles of width 2, which 
        // at the end boils down to the base cases and this is a behaviour much
        // like the fibonacci sequence, so...
        cout << combinations[N] << endl;
        // Immediatly output the precomputed amount of combinations for the
        // given width, bounded by 0 <= N <= 250.
    }
}