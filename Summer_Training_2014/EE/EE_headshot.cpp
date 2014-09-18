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
    string s;
    // String to be read according to each test case
    while(cin >> s) {
    // Read until end of file
        double total = s.length();
        double chamberHas = 0;
        // Counting occupied chambers
        double chamberNot = 0;
        // Counting empty chambers
        for(int k = 0; k < total; k++) {
            if(s[k] == '1') {
                chamberHas++;
            }
            else {
                chamberNot++;
            }
        }
        double probRoll = chamberHas / total;
        // The probability of dying after a reroll is the number of bullets in
        // the total amount of chambers. It can land anywhere in the gun.
        double probShoot = 0;
        // The probability of dying after immediately shooting. Since I just
        // survived the first 'click', it means the actual chamber was empty.
        // Lets find out in the total number of empty chambers that have a bull
        // et next to it to the right, which would mean death after shooting.
        for(int k = 0; k < total; k++) {
            int next = (k + 1) % (int)total;
            if(s[k] == '0' && s[next] == '1') {
                probShoot++;
            }
        }
        probShoot /= chamberNot;
        if(probShoot <  probRoll) {
            cout << "SHOOT" << endl;
        }
        if(probShoot == probRoll) {
            cout << "EQUAL" << endl;
        }
        if(probShoot  > probRoll) {
            cout << "ROTATE" << endl;
        }
    }

}