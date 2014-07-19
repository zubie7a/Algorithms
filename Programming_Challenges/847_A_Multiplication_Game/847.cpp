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
// Stan and Ollie play a game. Stan begins with number 1, then Ollie multiplies
// that number by a number between 2 and 9. Then Stan multiplies Ollie's new nu
// mber by a number again between 2 and 9. They do this until they exceed a lim
// mit value called n. Assuming both play perfectly, given a n limit, who wins?
    unsigned long long int n;
    // The limit to exceed or equal in successive multiplications
    while(cin >> n) {
        unsigned long long int p = 1;
        // The base number starts as 1
        int turn = 0;
        // The base player starts as Stan
        // 0: Stan
        // 1: Ollie
        while(true) {
        // The game goes on while p < n. Whoever makes p >= n, wins the game
            // 0: Stan
            // 1: Ollie
            if(!turn) {
                p *= 9;
            }
            else {
                p *= 2;
            }
            if(p >= n) break;
            turn = !turn;
            // I completely not understand why is this the optimal way of play
            // I mean, what the hell is optimal about this? If they can choose
            // a value between 2 and 9 (or 2|9 if the problem statement is bo-
            // gus) then Ollie could've perfectly chosen a 9 after Stan's first
            // 9 and have an incredible winning range (from 18 to 81). For me,
            // the perfect way of play must involve at least choosing a number
            // such that it won't allow the opponent to win the next round in
            // case the current player can't win this round.
        }
        if(turn) {
            cout << "Ollie wins." << endl;
        }
        else {
            cout << "Stan wins." << endl;
        }
    }
}