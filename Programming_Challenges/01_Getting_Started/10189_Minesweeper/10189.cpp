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

int grid[107][107];

void markSurrounding(int i, int j, int r, int c) {
// Increase mark the places surrounding a mine as having a mine surrounding
// them, or increase the currently held value of mines surrounding that place
    int directions[8][2] = {
        { 0,  1}, // Right
        {-1,  1}, // Upper-Right
        {-1,  0}, // Up
        {-1, -1}, // Upper-Left
        { 0, -1}, // Left
        { 1, -1}, // Lower-left
        { 1,  0}, // Below
        { 1,  1}, // Lower-Right
    };
    // This will be helpful for finding the new positions, which are shifted to
    // in either horizontal or vertical positions, or even in both, by one unit
    // in positive or negative direction.
    for(int k = 0; k < 8; k++) {
        int hShift = j + directions[k][1];
        // Horizontal shift to check out
        int vShift = i + directions[k][0];
        // Vertical shift to check out
        if(hShift >= 0 && vShift >= 0 &&
           hShift <  c && vShift <  r ) {
            if(grid[vShift][hShift] != -1) {
                grid[vShift][hShift]++;
            }
        }
    }
}

int main() {
// This program will take a originally given board of Minesweeper with nothing
// marked on it but the mines positions, and return a board that fills the emp-
// ty spaces with the number of mines that surround that space in the eight pos
// sible directions. We'll use a integer matrix to store the counters of mines,
// and in the place where there is a mine, simply putting a -1 value so it wont
// add anything up in that place.
    int r, c;
    // Number of rows and columns to be read
    int fields = 0;
    // To keep track of the number of fields already outputted
    while(scanf("%d %d", &r, &c)) {
        if(!r && !c) {
            break;
        }
        if(fields) {
            puts("");
        }
        string row;
        vector< pair<int, int> > mines;
        for(int i = 0; i < r; i++) {
            cin >> row;
            for(int j = 0; j < c; j++) {
                grid[i][j] = (row[j] == '*') ? -1 : 0;
                if(grid[i][j] == -1) {
                    pair<int, int> p;
                    p.first = i;
                    p.second = j;
                    mines.push_back(p);
                }
            }    
        }
        for(int k = 0; k < mines.size(); k++) {
            pair<int, int> p = mines[k];
            int i = p.first;
            int j = p.second;
            markSurrounding(i, j, r, c);
        }
        printf("Field #%d:\n", ++fields);
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                char c = (grid[i][j] >= 0)? grid[i][j] + '0' : '*';
                printf("%c", c);
            }
            puts("");
        }
    }
}