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

char grid[50][50];
// The grid of words, like a wordseach board. 50 are the max dimensions either
// horizontally or vertical, it can actually be lower

int m, n;
// The place to store the dimensions of the actual test case's grid
// m: amount of lines (vertical direction)
// n: amount of characters per line (horizontal direction)

bool lowerCase(char x) {
    return 'a' <= x && x <= 'z';
}

bool upperCase(char x) {
    return 'A' <= x && x <= 'Z';
}

char toLower(char x) {
    if(upperCase(x)) {
    // If its uppercase, first obtain the index of the letter by substracting
    // 'A' and then add that index to 'a' to get the lowercase version of x
        return (x - 'A') + 'a';
    }
    else {
    // If its not uppercase, or alphabetical for that matter, simply return x
        return x;
    }
}

void findMatch(string str) {
    int pVer = m, pHor = n;
    // Variables to store the index where the word has been found in the grid,
    // there's preference to uppermost stuff, and then to leftmost stuff. Lets
    // give these a value thats impossible to get (and high) so that anything
    // found will evaluate at first as always lower. It is certain (as per the
    // problem statement) that the queried word is in the grid.
    int movs[8][2] = {
    // Directions of movement to check for
        { 0,  1}, // Vertical: none, Horizontal: right
        { 1,  1}, // Vertical: down, Horizontal: right
        { 1,  0}, // Vertical: down, Horizontal: none
        { 1, -1}, // Vertical: down, Horizontal: left
        { 0, -1}, // Vertical: none, Horizontal: left
        {-1, -1}, // Vertical: up,   Horizontal: left
        {-1,  0}, // Vertical: up,   Horizontal: none
        {-1,  1}, // Vertical: up,   Horizontal: right
    };
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            char c = grid[i][j];
            // Variables to store the found position (if its found!)
            for(int k = 0; k < 8; k++) {
                int dy = movs[k][0];
                int dx = movs[k][1];
                // Now, check that boundaries won't be exceeded
                int len = str.length();
                int horizontal = j + ((len - 1) * dx);
                // The HORIZONTAL ending index of the queried string given that
                // its found from this starting point (i,j). If its outside the
                // boundaries, then ignore this search for it
                int vertical = i + ((len - 1) * dy);
                // The VERTICAL ending index of the queried string given that
                // its found from this starting point (i,j). If its outside the
                // boundaries, then ignore this search for it
                if(horizontal < 0 || horizontal >= n) {
                // It means that either the horizontal bounds will be exceeded
                    continue;
                }
                if(vertical < 0 || vertical >= m) {
                // It means that either the vertical bounds will be exceeded
                    continue;
                }
                int matches;
                for(matches = 0; matches < len; matches++) {
                // The count of matching characters starts as 0. Then, for eve-
                // ry matching character, the count increases. As soon as a ch-
                // aracter doesn't match, this counting is finished. The posit-
                // ions are changed based on the amount of matches and the dir-
                // ectional changes (dx, dy) based on the current direction.
                    int posY = i + (matches * dy);
                    int posX = j + (matches * dx);
                    if(grid[posY][posX] != str[matches]) {
                        break;
                    }
                }
                if(matches == len) {
                // If the amount of matches is equal to the length of the word,
                // it means it was found! Lets see if the current index has be-
                // tter relevance than the previously found one if any.
                    if(i <= pVer) {
                    // There's a relevance for uppermost starting occurrences
                        if(j <= pHor) {
                        // If there's a tie, then take the leftmost one. I gue-
                        // ss that ties here don't matter. I mean, there can be
                        // ties here if the same uppermost and leftmost positi-
                        // on has a vertical, horizontal and diagonal starting
                        // strings that match (downwards, rightwards and down-
                        // and-rightwards).
                            pVer = i;
                            pHor = j;
                        }
                    }
                }
            }
        }
    }
    cout << pVer + 1 << " " << pHor + 1 << endl;
    // + 1 because the rows and cols are assumed in the output as 1..m 1..n
    // as per the problem statement (though all calculations are zero-based).
}

int main() {
    int t;
    // Number of test cases to be read
    cin >> t;
    for(int z = 0; z < t; z++) {
        cin >> m >> n;
        for(int i = 0; i < m; i++) {
            string line;
            cin >> line;
            for(int j = 0; j < n; j++) {
                grid[i][j] = toLower(line[j]);
            }
        }
        int w;
        // The number of word to search for in the grid
        cin >> w;
        while(w--) {
            string str;
            cin >> str;
            for(int k = 0; k < str.length(); k++) {
                str[k] = toLower(str[k]);
            }
            findMatch(str);
        }
        if(z + 1 < t) {
            puts("");
        }
    }
}