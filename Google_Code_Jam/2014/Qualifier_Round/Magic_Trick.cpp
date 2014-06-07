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

int main(){
    int T, row[2], grid[2][4][4];
    scanf("%d", &T);
    for(int z = 0;z < T;z++){
        // First, read the input
        for(int k = 0;k < 2;k++){
            // Two times..
            scanf("%d", &row[k]);
            // The chosen row the card is in will be read
            row[k]--;
            // And now the position of all cards is read
            for(int i = 0;i < 4;i++){
                for(int j = 0;j < 4;j++){
                    scanf("%d", &grid[k][i][j]);
                }
            }
        }
        // A set is used to have unique occurrences in it
        set<int> das_set;
        /*
         No matter whats the deal with the magician and its
         shuffling, the point is that he tries to rearrange
         the cards in a way that each card in the new grid
         doesnt share a row with any card it shared a row
         in the previous grid. The easiest way to do this is
         transposing the card grid/matrix, but the magician
         could've thought of another way to shuffling them,
         perhaps a flawed one.
        */
        int res[17];
        for(int i = 1;i <= 16;i++){
            res[i] = 0;
            // The number of occurrences of each card is 0
        }
        /*
         The magician will then compare the two rows where the
         volunteer said his card were in. If both rows have just
         one card in common, then the magician will be able to 
         tell that was the card the volunteer had chosen. If the
         rows don't share any card, then the volunteer has told
         a lie to the magician, he is cheating. And if the rows
         share more than two cards, the magician was a bad one
         because he did a sucky job at rearranging the cards,
         meaning that there is more than one possible card the
         volunteer could've possibly chosen
        */
        for(int k = 0;k < 2;k++){
            for(int i = 0;i < 4;i++){
                int num = grid[k][row[k]][i];
                // num is a card belonging to either of the rows
                das_set.insert(num);
                // num is put into the set which allows to know
                // the amount of unique occurrences of some values
                res[num]++;
                // Increment the number of occurences for number in
                // case we need to know which number had multiple
                // occurrences, to determine which was the card.
            }
        }
        int setSize = das_set.size();
        // Set will have a max size of 8 cards, given that all the
        // cards in the two given rows are different.
        printf("Case #%d: ", z + 1);
        if(setSize == 8){
            // If the size is 8, all cards are different
            printf("Volunteer cheated!");
        }
        if(setSize < 7){
            // If the size is less than 7, there were at least two
            // cards which had more than one occurrence.
            printf("Bad magician!");
        }
        if(setSize == 7){
            // If the set size is exactly 7, there was a single card
            // with two occurences, so we look for which card was it.
            for(int i = 1;i <= 16;i++){
                if(res[i] == 2){
                    printf("%d", i);
                }
            }
        }
        if(z + 1 < T){
            puts("");
        }
    }
}