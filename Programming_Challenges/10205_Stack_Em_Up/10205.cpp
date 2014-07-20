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

struct Card {
    string suit;
    int value;
    string name;
};

Card deck[52];
// The place to store the deck
Card alt[52];
// The place to store alterations to the deck, and then moved to the original

map<int, string> mapNames;
// A map that links a value with a card name

vector< vector<int> > shuffles;
// The several shuffles that the dealer knows

void initDeck() {
    string suits[4] = {
        "Clubs",
        "Diamonds",
        "Hearts",
        "Spades"
    };
    for(int i = 0; i < 4; i++) {
        string suit = suits[i];
        for(int j = 0; j < 13; j++) {
            Card card;
            card.suit = suit;
            card.value = j;
            card.name = mapNames[j] + " of " + suit;
            deck[(i * 13) + j] = card;
        }
    }
}

void initMap() {
    mapNames[0] = "2";
    mapNames[1] = "3";
    mapNames[2] = "4";
    mapNames[3] = "5";
    mapNames[4] = "6";
    mapNames[5] = "7";
    mapNames[6] = "8";
    mapNames[7] = "9";
    mapNames[8] = "10";
    mapNames[9] = "Jack";
    mapNames[10] = "Queen";
    mapNames[11] = "King";
    mapNames[12] = "Ace";
}

void applyShuffle(int index) {
    vector<int> shuffle = shuffles[index];
    for(int k = 0; k < shuffle.size(); k++) {
        int from = shuffle[k] - 1;
        // The current value tells the position of the card to move
        int to = k;
        // The current position tells the target position of the movement
        alt[to] = deck[from];
        // All these changes are done into an alternate deck for now
    }
    for(int k = 0; k < 52; k++) {
    // When all the movements are done, move the result back into the main deck
        deck[k] = alt[k];
    }
}

int main() {
    initMap();
    int t;
    // Number of test cases
    cin >> t;
    int shuffleNum;
    // Number of shuffles that the dealer knows
    string line;
    getchar();
    getline(cin, line);
    while(t--) {
        initDeck();
        // For every test case, the deck is initialized to suit-numeric order
        shuffles.clear();
        cin >> shuffleNum;
        for(int k = 0; k < shuffleNum; k++) {
            vector<int> shuffle;
            // A list that will contain a specific shuffle the dealer knows. A
            // shuffle is composed of a order of numbers, each number (i) in
            // position (j) means that the shuffle will move the i-th card of
            // the deck to the j-th position.
            for(int l = 0; l < 52; l++) {
                int num;
                cin >> num;
                shuffle.push_back(num);
            }
            shuffles.push_back(shuffle);
        }
        getchar();
        while(getline(cin, line)) {
        // Get a undeterminate amount of numbers, which will be the indices of
        // the shuffles that the person will apply to the deck several times.
        // Each index will be in a single line, and the end of this reading
        // will come after a blank line is read (or EOF is reached).
            if(line == "") {
                break;
            }
            stringstream ss(line);
            int index;
            ss >> index;
            applyShuffle(index - 1);
        }
        for(int k = 0; k < 52; k++) {
            cout << deck[k].name << endl;
        }
        if(t > 0) {
        // Consecutive test cases are separated by a blank line
            puts("");
        }
    }
}