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
    int T;
    scanf("%d", &T);
    for(int z = 0; z < T; z++){
        int maxShy;
        string shyLevels;
        cin >> maxShy >> shyLevels;

        int needed = 0;
        // People needed to be invited
        int stands = 0;
        // People already standing
        for(int k = 0; k < shyLevels.length(); k++) {
        // shyLevels contains a list/array of these things:
        //    shyLevel -> key/index: a shyness level
        //    seated   -> value:     the people amount with that level
        // such amount of people won't stand up unless at least
        // (shyLevel) people have already stand up.
            int shyLevel = k;
            int seated   = shyLevels[k] - '0';
            if(seated == 0) {
            // If there isn't people in the current shy level, skip the level.
                continue;
            }
            if(shyLevel <= stands) {
            // If greater or equal people is already standing than the current
            // shy level's seated people, they will stand up now, add them up
            // to the amount of standing people.
                stands += seated;
            }
            else {
            // There isn't enough people standing to exceed the shy level and
            // make people stand so lets add up the difference amount of people
            // to be invited and then proceed to add up to standing people. The
            // newly invited people will add up to the total amount of people
            // required to be invited, and to the already standing amount.
                int newPeople = (shyLevel - stands);
                needed += newPeople;
                stands += seated + newPeople;
            }
        }
        printf("Case #%d: %d", z + 1, needed);
        if(z + 1 < T){
            puts("");
        }
    }
}