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

bool compareCards(string c1, string c2) {
    return (c1[1] == c2[1] || c1[0] == c2[0]);
}

int main(){
    string s;
    while(true) {
        cin >> s;
        if(s == "#") {
            break;
        }
        vector <string> cards;
        cards.push_back(s);
        for(int k = 0; k < 51; k++) {
            cin >> s;
            cards.push_back(s);
            // Put all read cards into a stack to start dealing them in the
            // order they came into the program in the input.
        }
        vector< stack<string> > deal;
        // Deal is a list of piles, each pile containing several cards
        for(int c = 0; c < cards.size(); c++) {
        // While there are still cards left to be dealt
            s = cards[c];
            stack<string> pile;
            // Create a new pile
            pile.push(s);
            // Put the card removed from the stack into this new pile
            deal.push_back(pile);
            // Put this pile into the list of dealt piles of cards
            int k = 0;
            while(k < deal.size()) {
                string card = deal[k].top();
                // The relevant card is the one at the top of the current pile
                bool move1 = false, move3 = false;
                if(k > 0) {
                    string card1 = deal[k - 1].top();
                    if(compareCards(card1, card)) {
                    // If either the rank/suit matches with 1 card to the left
                        move1 = true;
                    }
                }
                if(k > 2) {
                    string card3 = deal[k - 3].top();
                    if(compareCards(card3, card)) {
                    // If either the rank/suit matches with 3 cards to the left
                        move3 = true;
                    }
                }
                if(move3 == true) {
                // Available move 3 cards to the left. This move has priority
                // over moving just 1 card to the left.
                    deal[k - 3].push(card);
                    deal[k].pop();
                    if(deal[k].size() == 0) {
                    // If the pile we just took the card from is empty, then re
                    // move it from the list of piles!
                        deal.erase(deal.begin() + k, deal.begin() + k + 1);
                    }
                    k = k - 3;
                    // Reduce card counter since new moves may now be available
                    // and we want to always move the leftmost card possible.
                }
                else if(move1 == true) {
                // Available move 1 card to the left. Even if this move is pos-
                // sible, it will only be done if there is no moves available
                // at 3 cards to the left.
                    deal[k - 1].push(card);
                    deal[k].pop();
                    if(deal[k].size() == 0) {
                    // If the pile we just took the card from is empty, then re
                    // move it from the list of piles!
                        deal.erase(deal.begin() + k, deal.begin() + k + 1);
                    }
                    k = k - 1;
                    // Reduce card counter since new moves may now be available
                    // and we want to always move the leftmost card possible.
                }
                else {
                // No moves available
                    k++;
                    // Advance the current card iterator
                }
            }
        }
        cout << deal.size();
        if(deal.size() == 1) {
        // Problem statement doesn't say that for 1 one must use the singular
        // of piles, but I guess it must be common sense. IT COSTED 4 ATTEMPTS!
            cout << " pile remaining: ";
        }
        else {
            cout << " piles remaining: ";
        }
        for(int i = 0; i < deal.size(); i++) {
            cout << deal[i].size();
            if(i + 1 < deal.size()) {
                cout << " ";
            }
        }
        cout << endl;
    }
}

/*    
  Test Input:
  QD AD 8H 5S 3H 5H TC 4D JH KS 6H 8S JS AC AS 8D 2H QS TS 3S AH 4H TH TD 3C 6S
  8C 7D 4C 4S 7S 9H 7C 5D 2S KD 2D QH JD 6D 9D JC 2C KH 3D QC 6C 9S KC 7H 9C 5C

  Output:
  6 piles remaining: 40 8 1 1 1 1
*/