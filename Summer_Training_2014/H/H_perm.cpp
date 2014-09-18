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
    int T;
    // Number of test cases
    cin >> T;
    while(T--){
        string s;
        // String to read
        int n;
        // n-th permutation to find
        cin >> s >> n;
        sort(s.begin(), s.end());
        // Sort the string so all possible permutations can be found
        for(int k = 0; k < n; k++){
            // Go up to the n-th permutation
            next_permutation(s.begin(), s.end());
        }
        // THIS IS VERY EXPENSIVE IN COMPUTATIONS BECAUSE IT CALCULATES EVERY
        // LEXICOGRAPHICALLY INCREASING PERMUTATION OF THE ORIGINAL STRING UP
        // TO THE DESIRED TARGED PERMUTATION, WHICH COULD BE 20! PERMUTATIONS
        // LATER! For that check out H_newperm.cpp, which lays out how to more
        // or less in much more less computations calculate the target permut-
        // tation directly, without going over all its previous ones.
        cout << s << endl;
    }
}