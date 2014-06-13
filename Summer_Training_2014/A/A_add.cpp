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

#define llu unsigned long long int 
using namespace std;

struct Num {
    int n;
    bool operator < (const Num &that) const {
    // Overload < operator because this structure will be used in a priority
    // queue, and in such a structure, it will always maintain the 'biggest'
    // element on top of it, and we want the 'smallest' element instead.
        return n > that.n; 
    }
};

int main() {
    int T;
    // Number of test cases
    int N;
    // Placeholder for read numbers
    llu sum;
    // The sum of the 2 lowest numbers available
    llu total;
    // The total of the costs of each pair of numbers added
    int index;
    while(cin >> T) {
        priority_queue < Num > nums;
        if(!T) {
            break;
        }
        sum = 0;
        total = 0;
        index = 0;
        for(int k = 0; k < T; k++) {
            cin >> N;
            Num num;
            num.n = N;
            nums.push(num);
        }
        while(nums.size() > 1) {
            int n1 = nums.top().n;
            // Take the lowest element out of the priority queue
            nums.pop();
            int n2 = nums.top().n;
            // Take the second lowest element out of it too
            nums.pop();
            sum = n1 + n2;
            // Add the two lowest values that were in the queue
            total += sum;
            // Add this to the total as a cost of adding up
            Num num;
            num.n = sum;
            nums.push(num);
            // Put back the result back into the priority queue
        }
        cout << total << endl;
    }
}