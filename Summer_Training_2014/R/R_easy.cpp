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
    int N;
    while(cin >> N) {
        if(!N) {
        // Input terminates with 0
            break;
        }
        int count = 0;
        // Amount of items that have <= 1000 calories each, so Ana can eat it
        for(int k = 0; k < N; k++) {
            int num;
            cin >> num;
            if(num <= 1000) {
            // If the current item calory count is <= 1000, Ana can eat it!
                count++;
            }
        }
        cout << count << endl;
    }
}