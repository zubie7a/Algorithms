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

string ttt[3];

int checkWins(char winner) {
    int _ttt[3][3];
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(ttt[i][j] == winner) {
                _ttt[i][j] = 1;
            }
            else {
                _ttt[i][j] = 0;
            }
        }
    }
    // This will have created a matrix where the positions occupied by the
    // winner-to-check value are 1, otherwise, 0 so they don't add up.
    int wins = 0;
    // Total amount of wins for the 'winner' symbol to be checked
    int d1 = 0, d2 = 0;
    // Count of occurrences of the 'winner' symbol in each of the diagonals
    for(int k = 0; k < 3; k++) {
        if((_ttt[k][0] + _ttt[k][1] + _ttt[k][2]) == 3) {
        // Check if there are 3 consecutive 'winner' symbols in each column
            wins++;
        }
        if((_ttt[0][k] + _ttt[1][k] + _ttt[2][k]) == 3) {
        // Check if there are 3 consecutive 'winner' symbols in each row
            wins++;
        }
        d1 += _ttt[k][k];
        d2 += _ttt[k][3 - k - 1];
    }
    if(d1 == 3) {
    // If there are 3 'winner' symbols in this diagonal, its a win
        wins++;
    }
    if(d2 == 3) {
    // If there are 3 'winner' symbols in this diagonal, its a win
        wins++;
    }
    // If a board is completely full of a single symbol, there will be 8 wins
    return wins;
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        cin >> ttt[0];
        cin >> ttt[1];
        cin >> ttt[2];
        int cX = 0, cO = 0;
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                if(ttt[i][j] == 'X') {
                // Count the number of X positions
                    cX++;
                }
                if(ttt[i][j] == 'O') {
                // Count the number of O positions
                    cO++;
                }
            }
        }
        int winX = checkWins('X');
        // Check the amount of times X shows up as winner
        int winO = checkWins('O');
        // Check the amount of times O shows up as winner
        if(cO != cX && cX != cO + 1) {
        // At no given moment cO can be greater than cX, or cX be >= cO + 2
            cout << "no" << endl;
            continue;
        }
        if(winX >= 1 && winO >= 1) {
        // At no given moment can both O and X win
            cout << "no" << endl;
            continue;
        }
        if(winO >= 1 && cO != cX) {
        // At no given moment can O win and be different than cX
            cout << "no" << endl;
            continue;
        }
        if(winX >= 1 && cO + 1 != cX) {
            // At no given moment can X win and not be greater than cO
            cout << "no" << endl;
            continue;
        }
        cout << "yes" << endl;
    }
}