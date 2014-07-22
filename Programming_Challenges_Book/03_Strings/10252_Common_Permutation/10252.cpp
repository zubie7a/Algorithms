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

int dictA[30];
int dictB[30];

void initDicts() {
    for(int k = 0; k < 30; k++) {
        dictA[k] = 0;
        dictB[k] = 0;
    }
}

void findCommon() {
// Having counted the amount of occurrences for each character in each of the
// words, lets print n times each character, being n the shared amount of occu-
// rences. Since the dictionary is in alphabetical order, the printed string
// will be the lexicographically earliest possible permutation of the answer.
    for(int k = 0; k < 30; k++) {
        int amountA = dictA[k];
        int amountB = dictB[k];
        int least = min(amountA, amountB);
        for(int l = 0; l < least; l++) {
            cout << (char)(k + 'a');
        }
    }
}

int main() {
// Given two strings such as 'walking' and 'down', lets find the longest string
// x of letters such that there is a permutation of x that is a subsequence of
// a and there is a permutation of x that is a subsequence of b. In the case of
// those two words, the answer would be 'nw'
    string lineA;
    string lineB;
    while(getline(cin, lineA)) {
        getline(cin, lineB);
        initDicts();
        // Lets first count the amount of characters in each of the given words
        // so that we may later check for the same character the common occure-
        // nces (lets say, 3 and 5 ocurrences of 'a', means there are 3 shared
        // ocurrences of 'a', 0 and 2, means there are 0).
        for(int k = 0; k < lineA.length(); k++) {
            int curIndex = lineA[k] - 'a';
            dictA[curIndex]++;
            // Increase the ocurrences of the given character
        }
        for(int k = 0; k < lineB.length(); k++) {
            int curIndex = lineB[k] - 'a';
            dictB[curIndex]++;
            // Increase the ocurrences of the given character
        }
        findCommon();
        cout << endl;
    }
}