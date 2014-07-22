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

string keyboard[4] = {
// A array of strings, each string representing each line of the keyboard. When
// searching for the left neighbour, search for the given key and return the o-
// ne at its left.
    "1234567890-=",
    "QWERTYUIOP[]\\",
    "ASDFGHJKL;'",
    "ZXCVBNM,./"
};

char findLeft(char x) {
// Find the given key and return the key at its left. No keys at the leftmost
// position of the keyboard will be given as keys to find its left neighbour.
    for(int i = 0; i < 4; i++) {
        string line = keyboard[i];
        for(int j = 1; j < line.length(); j++) {
            if(line[j] == x) {
                return line[j - 1];
            }
        }
    }
}

int main() {
    string s;
    while(getline(cin, s)) {
    // Read lines until the end of the file
        for(int k = 0; k < s.length(); k++) {
            char c = s[k];
            if(c == ' ') {
            // Print empty spaces as usual
                cout << " ";
            }
            else {
            // Shift keys to the left
                cout << findLeft(c);
            }
        }
        cout << endl;
    }
}