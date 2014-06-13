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
    int N, M;
    // N: number of heads the dragon has
    // M: number of knights the kingdom has
    while(cin >> N >> M) {
        if(!N && !M) {
            break;
        }
        vector<int> headsDiameters;
        vector<int> knightsHeights;
        for(int k = 0; k < N; k++) {
        // Read the diameters of each of the dragon's heads
            int n;
            cin >> n;
            headsDiameters.push_back(n);
        }
        for(int k = 0; k < M; k++) {
        // Read the heighs of each of the kingdom's knights
            int m;
            cin >> m;
            knightsHeights.push_back(m);
        }
        sort(headsDiameters.begin(), headsDiameters.end());
        sort(knightsHeights.begin(), knightsHeights.end());
        // Sort both the head diameters and the knights heads
        // This helps to know which knight will face which head. If a knight
        // can't deal with a head, it can't deal with any other bigger head,
        // so we proceed to check the head diameter against a taller knight.
        // Also, once a knight deals with a head, it will go away since they
        // can only fight one head.
        int headsIter = 0;
        // Current dragon head we are fighting against
        int knightIter = 0;
        // Current knight we are comparing against the dragon head
        int totalPrice = 0;
        // The total price to pay the knights involved in dragon slaying
        while(headsIter < N && knightIter < M) {
        // A cycle while the amount of heads or knights have not been exhausted
            if(headsDiameters[headsIter] <= knightsHeights[knightIter]) {
            // If the current knight can deal with the current head
                totalPrice += knightsHeights[knightIter];
                // Add the height of the current knight to the total payout
                headsIter++;
                // Advance to the next head since we have slayed the current
            }
            knightIter++;
            // Regardless if a knight could slay a head or not, proceed to the
            // next head, because if it couldn't, since they are sorted, the
            // knight won't be able to deal with any further head, whereas if
            // it could slay it, still the knight can only fight one head ever.
        }
        if(headsIter < N) {
            // If it exited the previous loop and there are still heads left,
            // it means it exhausted all knights and some heads were not slain.
            cout << "Loowater is doomed!" << endl;
        }
        else {
            // Otherwise, either there were equal amount of knights needed for
            // all heads, or there was a surplus of knights even after all the
            // heads were slain so print the total payout for the involved ones
            cout << totalPrice << endl;
        }
    }
}