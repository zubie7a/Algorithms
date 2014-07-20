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
// There are n lightbulbs down a corridor. A man goes through the corridor n
// times, each time turning on/off the lightbulbs that have a serial number
// (from 1 to n) that is divided by the number of the current travel (k-th),
// we want to know the state of the last lightbulb at the end of the n times
// the man goes through the corridor.

// This could be also understood regarding the amount of divisors that the last
// lightbulb has. For each divisor found along the travels, the switch will be
// toggled. Every number has at least 2 divisors, 1 and itself. Then, every
// number k that divides the number, lets us find another number n/k that also
// divides the number, meaning that most numbers have an even number of divi-
// sors. The only case for an odd number of divisors is that the number is a
// perfect square, since k (a found divisor) would be equal to n/k (the other
// found divisor)

// An odd number of divisors will leave the last lightbulb on, whereas an even
// number of divisors will leave the last lightbulb off.

    unsigned long long int n;
    // The number of lightbulbs that the corridor has
    while(cin >> n) {
        if(!n) {
        // 0 lightbulbs means the end of the input
            break;
        }
        unsigned long long int root = sqrt(n);
        if(root * root == n) {
            cout << "yes" << endl;
        }
        else {
            cout << "no" << endl;
        }
    }
}