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

map<char, double> table;

void initMap() {
// Mapping between chemical symbols and their molar weights
    table['H'] = 1.008;
    table['C'] = 12.01;
    table['N'] = 14.01;
    table['O'] = 16.00;
}

bool isNumeric(char c) {
// Return if the representation of a character is that of a number
    return '0' <= c  && c <= '9';
}

int main() {
    int T;
    // Number of Test Cases
    string s;
    // String containing the read element chain
    initMap();
    cin >> T;
    while(T--) {
        cin >> s;
        // USE DOUBLE PRECISION SERIOUSLY, WITH FLOAT IT LOSES PRECISION WAY
        // TOO FAST, and I can confirm it costed me a submission ;-)
        double total = 0;
        // Total molar weight of a given molecule
        double num = 0;
        // The value of the last read element, to apply multipliers into
        int mult = 0;
        // The multiplier to apply to the chemical element right before it
        for(int k = 0; k < s.length(); k++) {
            if(isNumeric(s[k])) {
            // If we're reading a indice value
                if(mult != 0) {
                // If we had just read one, it means the previous one is a
                // decimal place bigger than the current one, but both are
                // part of the same number. I think this allows to exceed
                // the bound of two decimal places that the problem has.
                    mult *= 10;
                }
                mult += s[k] - '0';
            }
            else {
            // If a chemical symbol is read
                if(mult != 0) {
                // Check if we had a previously computed index, and apply it to
                // the previously found chemical element, if any.
                    num *= mult;
                }
                mult = 0;
                // Reset the chemical element multiplier
                total += num;
                // Add the previously found number to the running count of mass
                num = table[s[k]];
                // Set a new value to possibly apply a multiplying factor later
            }
        }
        // Do the last step again in case we ran out of the string and never
        // got to find a new element that would cause the previously found mult
        // liplier to apply to the previously found element and add it into the
        // running total of mole mass for the given molecule.
        if(mult != 0) {
            num *= mult;
        }
        total += num;
        printf("%.3lf\n", total);
        // Print with 3 decimal places
    }
}