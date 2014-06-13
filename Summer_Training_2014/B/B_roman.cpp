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

// I -> 1, V -> 5, X -> 10
// I may only precede V & X (IV -> 4, IX -> 9)
// X -> 10, L -> 50, C -> 100
// X may only precede L & C (XL -> 40, XC -> 90)
// C -> 100, D -> 500, M -> 1000
// C may only precede D & M (CD -> 400, CM -> 900) 

// V, L and D are always followed of a symbol of smaller value.
// I, X, C, M, can't appear more than 3 consecutive times.
// V, L, and D can't appear more than 1 consecutive times.

// This code is not 'correct', as it assumes all inputs are valid. It doesn't
// check for invalid inputs, like a I preceding a C. The way it works is simply
// if the input is numeric in nature, then for each decimal place, find the
// respective string in the 'romans' matrix. So a 7 in the tens is "LXX".
// If the input is roman in nature, then it starts adding up from the right the
// respective numeric value (1 for I, 5 for V, 10 for X, etc) but if it finds
// a lower roman value than the past one, instead of adding up, it substracts.

string romans[4][9] = {
    {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
    {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
    {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
    {"M", "MM", "MMM", "--", "-", "--", "---", "----", "--"}
};
// Roman value for each number from 1 to 9 depending on decimal place

map<char, int> alphabet;
void initAlphabet() {
    alphabet['I'] =    1;
    alphabet['V'] =    5;
    alphabet['X'] =   10;
    alphabet['L'] =   50;
    alphabet['C'] =  100;
    alphabet['D'] =  500;
    alphabet['M'] = 1000;
}
// Numeric value for each roman symbol

int main() {
    string s;
    initAlphabet();
    while(cin >> s) {
        bool numeric;
        if(s[0] >= '0' && s[0] <= '9') {
            numeric = true;
        }
        else {
            numeric = false;
        }
        if(numeric == true) {
        // If the read number is numeric in nature
            int d;
            stringstream ss(s);
            ss >> d;
            string res;
            for(int pos = 0; pos < s.length(); pos++) {
                int num = d % 10;
                d /= 10;
                if(num == 0) {
                    continue;
                }
                res = romans[pos][num - 1] + res;
            }
            cout << res << endl;
        }
        else {
        // If the read number is roman in nature
            int prev = 0;
            int res = 0;
            for(int pos = s.length() - 1; pos >= 0; pos--) {
            // Start adding up the respective numeric value for each symbol
            // from the right. If a lower symbol is found, substracts instead
                int num = alphabet[s[pos]];
                if(num >= prev) {
                    res += num;
                }
                else {
                    res -= num;
                }
                prev = num;
            }
            cout << res << endl;
        }
    }
}