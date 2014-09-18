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

#define ull unsigned long long int

using namespace std;

ull powers2[64];

void initPowers() {
// Lets calculate some powers of 2! unsigned long long int allows to store up
// to 2^64 - 1, which suffices to say, its TOO DAMN BIG! WE LIKE IT!
    powers2[0] = 1;
    for(int k = 1; k < 64; k++) {
        powers2[k] = 2 * powers2[k - 1];
    }
}

int main() {
    initPowers();
    int T;
    // Number of Test Cases to be read
    cin >> T;
    int N, K;
    // N: number of bits for the Gray Sequence 1 <= N <= 30
    // K: k-th value of the Gray Sequence. 0 <= K < 2^N
    while(T--) {
        cin >> N >> K;
        int c1 = 0;
        int c2 = powers2[N] - 1;
        // c1 and c2 are two values for holding the bounds to search within
        int res = 0;
        bool flip = false;
        for(int i = 0; i < N; i++) {
        // We'll find the value for each of the N bits of the desired value
            int mid = (c1 + c2) / 2;
            // We find the dividing point of the current range. The original
            // range goes from 0 to 2^N-1 values that can be in the Gray Seq-
            // uence. We update c2 (end bound) if the desired Kth term of the
            // Gray Sequence is before the middle. We update c1 (initial bound)
            // if the desired Kth term of the Gray Sequence is after the middle
            // so we reduce the searching by halves of the problem, and because
            // the sequence duplicates its size for every added bit. When pick-
            // ing from the first half, the bit value should be 0, and if pick-
            // ing from the second half, the bit value should be 1. But, when
            // picking from the second half, the expected bit values for the
            // next picking are reversed, since we picked from a mirrored half
            // which made the 0s added to the first half and the 1s added to
            // the second half in the previous subproblem to appear inverted.
            // Picking again from the first half immediately reverses back 1/0s
            if(K <= mid) {
                c2 = mid;
                if(flip) {
                    res += powers2[N - i - 1];
                }
                flip = false;
            }
            else {
                c1 = mid + 1;
                if(!flip) {
                    res += powers2[N - i - 1];
                }
                flip = true;
            }
        }
        cout << res << endl;
    }
}