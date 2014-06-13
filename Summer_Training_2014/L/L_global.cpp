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
    // Amount of test cases
    string s;
    // String to read with geographical representation of 2D world
    cin >> T;
    while(T--) {
        cin >> s;
        vector<int> dist;
        // This vector will store the distance that has been traversed since
        // the last downwards slope, because it will help determining the 
        // amount of water that its filled when we find a upwards slope.
        int total = 0;
        for(int k = 0; k < s.length(); k++) {
            if(s[k] == '\\') {
            // Start counting a distance when finding downwards slope
                dist.push_back(0);
            }
            if(s[k] == '_' && dist.size()) {
            // A no-slope terrain adds up a whole square of water
                dist[dist.size() - 1]++;
            }
            if(s[k] == '/') {
            // If an upwards slope is found
                if(dist.size()) {
                // And we've been keeping track of at least one distance since
                // a downwards slope (which makes / not matter otherwise) 
                    int lastDist = dist[dist.size() - 1] + 1;
                    // Add to the total distance a square, because both the
                    // downwards and upwards slopes add up to just one square
                    dist.pop_back();
                    // Stop keeping track of this distance because we have al-
                    // ready found the companion of the downwards slope, succe-
                    // ssfully completing a 'hole' to be filled with water
                    if(dist.size()) {
                    // If there are still other distances that are being
                    // kept tracked, it means that this whole hole we have
                    // found is really a sub-hole of a bigger hole, so it 
                    // will add up to the bigger hole the amount of water
                    // it has plus 1, which is all the water above of it.
                        dist[dist.size() - 1] += lastDist + 1;
                    }
                    total += lastDist;
                    // Add to the running total the dist of the last hole found
                }
            }
        }
        cout << total << endl;
    }
}