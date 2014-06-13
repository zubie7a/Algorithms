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
    int T;
    // Number of test cases
    int N;
    // Number of wall heights to read
    cin >> T;
    for(int k = 1; k <= T; k++) {
        cin >> N;
        int walls[N];
        int high = 0, low = 0;
        // Amount of high/low jumps between all walls.
        for(int i = 0; i < N; i++) {
            cin >> walls[i];
            if(i > 0){
                if(walls[i] > walls[i - 1]) {
                // If the current wall is taller than the previous one
                    high++;
                }
                if(walls[i] < walls[i - 1]) {
                // If the current wall is lower than the previous one
                    low++;
                }
                // It seems that walls of equal height do not matter
            }
        }
        cout << "Case " << k << ": " << high << " " << low << endl;
    }
}