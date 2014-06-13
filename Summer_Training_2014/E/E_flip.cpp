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
    // This will keep flipping until the largest element is at the last positon
    int N;
    int count;
    while(cin >> N) {
        int arr[N];
        for(int i = 0; i < N; i++) {
            cin >> arr[i];
        }
        count = 0;
        // Count of flips made
        for(int k = 0; k < N - 1; k++) {
        // Up to what point iterate. This helps because the right-most part of
        // the array will be invariant, since at each pass, it is assured that
        // the biggest elements will start to be placed there at the right.
            for(int i = 0; i < N - 1 - k; i++) {
                int j = i + 1;
                // The next position from the current one
                if(arr[i] > arr[j]) {
                // If the current value is bigger than the next, swap both. It
                // will move a value to the right until a bigger one is found.
                // This assures that the biggest of all will end at the right.
                    arr[i] = arr[i] ^ arr[j];
                    arr[j] = arr[i] ^ arr[j];
                    arr[i] = arr[i] ^ arr[j];
                    // Good old XOR swap :-)
                    count++;
                }
            }
        }
        cout << "Minimum exchange operations : " << count << endl;
    }
}