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

//
//_______ A
//_______ B  glass 1
//_______ C  glass 2
//
// A ray will always enter the couple of glasses. Each letter defines a 
// boundary between those glasses. Then, the following happens:
//
//     A
//    / \     a ray coming from the A boundary, can either be reflected by
//   B   C    the B boundary, or the C boundary. In case it is reflected by
//  /         the B boundary, then it must leave or be reflected at A again.
// A
//
//
//     C
//    / \     a ray coming from the C boundary, can either be reflected by
//   B   A    the B boundary, or the A boundary. In case it is reflected by
//  /         the B boundary, then it must leave or be reflected at C again.
// C
//
// At the moment a ray is reflected at a boundary, the available number of
// direction-changes is reduced. If it was reflected at A, and has available
// moves, then it can be reflected again at two different places, B or C. The
// sames applies for a ray that was reflected at C, given that it has available
// moves, then it can be re-reflected at two different places, B or A. A ray
// that was reflected at B, and has available 'moves', can only be re-reflected
// at the boundary where it came from.

int reflect(char from, char to, int moves) {
// The recursive definition of glass reflections, which is VERY SLOW and fucks
// up for really large numbers, but helps to identify the fibonacciesque nature
// of this problem.
    if(to == 'C') {
    // The next possible reflection after reflecting at C will happen either at
    // B or A and a possible move/reflection has been consumed
        if(moves - 1 == 0) return 1;
        return reflect(to, 'A', moves - 1) +
               reflect(to, 'B', moves - 1);
    }
    if(to == 'A') {
    // The next possible reflection after reflecting at A will happen either at
    // C or A and a possible move/reflection has been consumed
        if(moves - 1 == 0) return 1;
        return reflect(to, 'A', moves - 1) +
               reflect(to, 'B', moves - 1);
    }
    if(to == 'B') {
    // The next possible reflection after reflecting at B can only happen at
    // the point where the last reflection took place
        if(moves - 1 == 0) return 1;
        return reflect(to, from, moves - 1);
    }
}

string moves[1001];

string sum(string a, string b) {
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

void initMoves() {
    // Precomputed list of fibonacci numbers. Since they are WAY TOO BIG, I've
    // preferred to calculate them using strings to add up VERY LARGE NUMBERS.
    moves[0] = "1";
    moves[1] = "2";
    for(int k = 2; k < 1001; k++) {
        string n1 = moves[k - 1];
        string n2 = moves[k - 2];
        moves[k] = sum(n1, n2);
    }
}

int main(){
    int N;
    char cur;
    initMoves();
    while(cin >> N){
        if(N == 0){
            cout << 1 << endl;
            continue;
        }
        // cout << reflect('A', 'C', N) +
        //         reflect('A', 'B', N);
        // This would give the result but its WAY TOO SLOW. What I've just 
        // realized is that this could be given in terms of the subproblem of
        // n - 1 reflections, which at the end boils down to the base cases
        // and this is a behaviour much like in the fibonacci sequence, so...
        cout << moves[N] << endl;
    }
}