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

int main() {
// A sequence of n > 0 integer is called a Jolly Jumper if the absolute values
// of the differences between successive elements take on all possible values
// 1 through n - 1.
// 1 4 2 3 .. |1 - 4| = 3, |4 - 2| = 2, |2 - 3| = 1
// A single integer is a Jolly Jumper sequence
    int n;
    // The number of elements in every sequence
    while(cin >> n) {
    // Read the amount of elements in each sequence, until EOF
        int seq[n];
        for(int k = 0; k < n; k++) {
        // Read all the n elements of the sequence
            cin >> seq[k];
        }
        int dif[n - 1];
        for(int k = 0; k < n - 1; k++) {
        // Store the absolute value of the difference between each consecutive
        // pair of elements in the sequence
            dif[k] = abs(seq[k] - seq[k + 1]);
        }
        sort(dif, dif + n - 1);
        // Sort this list of differences. For every possible integer between
        // 1 and n - 1 being in this list, they must be unique. We will check
        // that the elements in this list are all the numbers possible between
        // 1 and n - 1. If a number isn't in the position it should be, it me-
        // ans there are repeated numbers or that there are numbers bigger than
        // n - 1, immediately invalidating the jolly jumper sequence.
        bool jolliness = true;
        for(int k = 0; k < n - 1; k++) {
            if(dif[k] != k + 1) {
                jolliness = false;
                break;
            }
        }
        if(jolliness) {
            cout << "Jolly" << endl;
        }
        else {
            cout << "Not jolly" << endl;
        }
    }
}