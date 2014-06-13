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
    string s;
    while(cin >> s) {
        if(s == ".") {
        // Input terminates with "."
            break;
        }
        set<int> divs;
        // A set to put into the divisors of a given number, in this case the
        // divisors of the string length, since those will be the appropiate
        // diving blocks to check if these are concatenated several times, whi-
        // ch in the problem definition was defined as the power of a string.
        for(int jump = 1; jump <= sqrt(s.length()); jump++) {
        // Go up to the square root because from there on the divisors will be
        // the opposite of the numbers just tested. 
            if(s.length() % jump != 0) {
                continue;
            }
            divs.insert(jump);
            divs.insert(s.length() / jump);
        }
        // Using a set helps with avoiding repeated ocurrences, though I don't
        // think this can have too much of a performance impact, but its better
        // to be safe than sorry!
        set<int>::iterator it;
        vector<int> divisors;
        for(it = divs.begin(); it != divs.end(); it++) {
            // Iterate the set (which I have no idea in which order keeps its
            // elements) and put the elements into an array.
            int divisor = *it;
            divisors.push_back(divisor);
        }
        sort(divisors.begin(), divisors.end());
        // The array will be then sorted, such that we start with the lower di-
        // visors (the ones that yield a big number of dividing blocks) because
        // we are interested in the biggest number of repetitions of concatena-
        // tions of the same block, that can result in the original string.
        for(int k = 0; k < divisors.size(); k++) {
            int jump = divisors[k];
            int parts = s.length() / jump;
            string _s = "";
            for(int l = 0; l < jump; l++) {
            // Assemble a little block that would be equal to dividing the ori-
            // ginal string into several blocks of length 'jump' between them.
                _s += s[l];
            }
            string final = "";
            for(int l = 0; l < parts; l++) {
            // Put back the block into a repeating chain of blocks
                final += _s;
            }
            if(final == s) {
            // Check if this block is the same original string, meaning its the
            // power/concatenation of strings as detailed in the problem def.
                cout << parts << endl;
                break;
            }
        }
    }
}