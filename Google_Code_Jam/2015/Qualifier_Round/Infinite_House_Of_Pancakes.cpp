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

int resolvePancakes(int pancakeDistribution[], int maxPancake, int dishes) {
    int finalCost = 1<<30;
    for(int limit = 1; limit <= maxPancake; limit++) {
    // We'll attempt distributing a lot of pancakes until all the dishes have
    // a limit value of pancakes they are holding, to proceed to let everyone
    // eat them from there on.
        int cost = 0;
        for(int j = 0; j < dishes; j++) {
        // For all dishes
            int pancakeValue = pancakeDistribution[j];
            cost += pancakeValue / limit;
            // Cost of distributing the current dish until reaching the limit
            if(pancakeValue % limit == 0) {
            // If it divides evenly, remove one minute from the cost because
            // the initial dish can't be included in the division, if it has
            // a remainder then the initial dish will hold that remainder.
                cost--;
            }
        }
        cost += limit;
        finalCost = min(finalCost, cost);
    }
    // At the end, finalCost will contain the cost that was achieved with a
    // certain limit of pancakes for all dishes that minimizes such cost.
    return finalCost;
}


int main() {
    int T;
    scanf("%d", &T);
    for(int z = 0; z < T; z++){
        int dishes;
        cin >> dishes;
        // Read the initial amount of dishes that have pancakes on them.
        int pancakeDistribution[dishes];
        // Store the value of pancakes in dishes in so that the dish with the
        // biggest number of pancakes always remains on top.
        int maxPancake = 0;
        for(int k = 0; k < dishes; k++) {
        // Read the amount of pancakes on each of the given dishes, and then
        // push it to the priority queue.
            int pancakeNumber;
            cin >> pancakeNumber;
            pancakeDistribution[k] = pancakeNumber;
            maxPancake = max(pancakeNumber, maxPancake);
        }
        int minutes = 0;
        // Initialize the current amount of elapsed minutes at 0.
        minutes = resolvePancakes(pancakeDistribution, maxPancake, dishes);
        printf("Case #%d: %d", z + 1, minutes);
        if(z + 1 < T){
            puts("");
        }
    }
}