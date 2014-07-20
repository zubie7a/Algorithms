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
// This program will convert decimal numbers into their LCD representation
    //   -0-
    //  |   |
    //  1   2   These are all the segments possible in a LCD number
    //  |   |   we'll define the segments that are turned on for all
    //   -3-    the 10 possible digits ranging from 0 to 9 in an array
    //  |   |   then we create the LCD number by checking with bits   
    //  4   5   are on for each number.
    //  |   |
    //   -6-
    int bits[10][7] = {
        {1, 1, 1, 0, 1, 1, 1}, // #0 has: 0, 1, 2, 4, 5, 6 bits on
        {0, 0, 1, 0, 0, 1, 0}, // #1 has: 2, 5 bits on
        {1, 0, 1, 1, 1, 0, 1}, // #2 has: 0, 2, 3, 4, 6 bits on
        {1, 0, 1, 1, 0, 1, 1}, // #3 has: 0, 2, 3, 5, 6 bits on
        {0, 1, 1, 1, 0, 1, 0}, // #4 has: 1, 2, 3, 5 bits on
        {1, 1, 0, 1, 0, 1, 1}, // #5 has: 0, 1, 3, 5, 6 bits on
        {1, 1, 0, 1, 1, 1, 1}, // #6 has: 0, 1, 3, 4, 5, 6 bits on
        {1, 0, 1, 0, 0, 1, 0}, // #7 has: 0, 2, 5 bits on
        {1, 1, 1, 1, 1, 1, 1}, // #8 has: 0, 1, 2, 3, 4, 5, 6 bits on
        {1, 1, 1, 1, 0, 1, 1}  // #9 has: 0, 1, 2, 3, 5, 6 bits on
    };
    int s;
    // Amount of segments for each number to be drawn
    string sn;
    // Number to be read to represent in LCD style
    while(cin >> s >> sn) {
        if(!s && sn == "0") {
            break;
        }
        vector<string> lines;
        int rows = (2 * s) + 3;
        int cols = s + 2;
        for(int k = 0; k < rows; k++) {
            lines.push_back("");
        }
        for(int k = 0; k < sn.length(); k++) {
            char number[rows][cols];
            // Each number has:
            // ((2 * s) + 3) rows
            // (s + 2) columns
            // ...in their LCD representation
            for(int i = 0; i < rows; i++) {
                for(int j = 0; j < cols; j++) {
                    number[i][j] = ' ';
                }
            }
            int digit = sn[k] - '0';
            // Each digit of the originally given number from left to right
            if(bits[digit][0] == 1) {
                for(int j = 1; j < cols - 1; j++) {
                    number[0][j] = '-';
                }
            }
            if(bits[digit][1] == 1) {
               for(int i = 1; i < rows / 2; i++) {
                    number[i][0] = '|';
                }
            }
            if(bits[digit][2] == 1) {
                for(int i = 1; i < rows / 2; i++) {
                    number[i][cols - 1] = '|';
                }
            }
            if(bits[digit][3] == 1) {
                for(int j = 1; j < cols - 1; j++) {
                    number[(rows / 2)][j] = '-';
                }
            }
            if(bits[digit][4] == 1) {
                for(int i = (rows / 2) + 1; i < rows - 1; i++) {
                    number[i][0] = '|';
                }
            }
            if(bits[digit][5] == 1) {
                for(int i = (rows / 2) + 1; i < rows - 1; i++) {
                    number[i][cols - 1] = '|';
                }
            }
            if(bits[digit][6] == 1) {
                for(int j = 1; j < cols - 1; j++) {
                    number[rows - 1][j] = '-';
                }
            }
            for(int i = 0; i < rows; i++) {
                string line = "";
                for(int j = 0; j < cols; j++) {
                    line += number[i][j];
                }
                lines[i] += line;
                if(k + 1 < sn.length()) {
                    lines[i] += " ";
                }
            }
        }
        for(int k = 0; k < rows; k++) {
            printf("%s\n", lines[k].c_str());
        }
        puts("");
    }
}