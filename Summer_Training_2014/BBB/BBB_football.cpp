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

int main(){
    int D, M, S;
    // D: lower bound for defenders
    // M: lower bound midfields
    // S: lower bound strikers
    int range;
    while(cin >> D >> M >> S) {
    // Read until EOF
        int count = 0;
        int range = 10 - (D + M + S);
        // Range is the remaining amount that can go to any kind of player
        // this is found by taking from the total, the lower bounds of the
        // amounts for each kind of player defined.
        for(int d = D; d <= D + range; d++) {
            for(int m = M; m <= M + range; m++) {
                for(int s = S; s <= S + range; s++) {
                    if(d + m + s == 10) {
                        count++;
                        break;
                    }
                }
            }
        }
        cout << count << endl;
    }
}