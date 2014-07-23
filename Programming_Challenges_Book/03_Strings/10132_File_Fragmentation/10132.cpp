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
// We have several fragments of several files. We know that the original files
// were all identical, and that all files were split in two, but in separate
// places. Knowing this, it is possible to group all the 2N fragments into N
// identical files. How does the original file look?
    int n;
    // The number of cases to be read
    cin >> n;
    string line;
    getchar();
    getline(cin, line);
    for(int z = 0; z < n; z++) {
        vector<string> fragments;
        while(getline(cin, line)) {
        // 2N fragments will be read, but we don't know what N is, so lets just
        // read until reaching an empty line or the end of the file
            if(line == "" || line == " ") {
            // Input is terminated by an empty line
                break;
            }
            string fragment;
            stringstream ss(line);
            ss >> fragment;
            fragments.push_back(fragment);
        }
        map<string, int> files;
        for(int k = 0; k < fragments.size() - 1; k++) {
            for(int l = k + 1; l < fragments.size(); l++) {
            // Lets create all possible combinations of pairs of fragments!
                string fragment1 = fragments[k];
                string fragment2 = fragments[l];
                string file1 = fragment1 + fragment2;
                string file2 = fragment2 + fragment1;
                files[file1]++;
                files[file2]++;
            }
        }
        // Now that the files map has the amount of unique files created by the
        // combination of all pairs of fragments, lets check which has the big-
        // est amount of occurences. There's a minimum of N occurrences for the
        // one that's the solution, some extra occurrences may happen, we make
        // sure that a solution is the one with the most occurences.
        map<string, int>::iterator it;
        int maxOccurrences = 0;
        string res = "";
        for(it = files.begin(); it != files.end(); it++) {
            if(it->second > maxOccurrences) {
                maxOccurrences = it->second;
                res = it->first;
            }
        }
        cout << res << endl;
        if(z + 1 < n) {
            puts("");
        }
    }
}