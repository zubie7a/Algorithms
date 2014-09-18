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

bool checkPalin(string s, int l, int r) {
    int mid = (l + r) / 2;
    bool palin = true;
    for(int k = l; k < mid; k++) {
        if(s[k] != s[r - k + l - 1]) {
            palin = false;
        }
    }
    return palin;
}

int main() {
    int T;
    string s;
    cin >> T;
    bool palin, alin;
    while(T--) {
        palin = false;
        alin = false;
        cin >> s;
        palin = checkPalin(s, 0, s.length());
        for(int k = 1; k < s.length() / 2 + 1; k++) {
            if(checkPalin(s, 0, k)) {
                if(checkPalin(s, k, s.length())) {
                    alin = true;
                }
            }
            if(checkPalin(s, s.length() - k, s.length())) {
                if(checkPalin(s, 0, s.length() - k)) {
                    alin = true;
                }
            }
            if(alin == true) {
                break;
            }
        }
        if(alin) {
            cout << "alindrome" << endl;
        }
        else if(palin) {
            cout << "palindrome" << endl;
        }
        else {
            cout << "simple" << endl;
        }
    }
}