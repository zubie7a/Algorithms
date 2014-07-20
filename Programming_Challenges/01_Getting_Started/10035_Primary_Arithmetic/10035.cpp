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
// Given two numbers, we want to know the amount of carry operations when
// adding those two numbers up to assess the difficulty they may pose to
// younger children learning to add up numbers involving carry operations.
    string a, b;
    // The two numbers to be read
    while(cin >> a >> b) {
        if(a == "0" && b == "0") {
        // Input is terminated by 0 0
            break;
        }
        if(a.length() < b.length()) {
        // Swap numbers so the first one is always larger or equal in length
        // than the second number...
            string temp;
            temp = b;
            b = a;
            a = temp;
        }
        while(b.length() < a.length()) {
        // ...so that the second number is padded to match the first's length
            b = "0" + b;
        }
        vector<int> num;
        for(int k = b.length() - 1; k >= 0; k--) {
            int na = a[k] - '0';
            int nb = b[k] - '0';
            num.push_back(na + nb);
        }
        int carryNum = 0;
        for(int k = 0; k < num.size(); k++) {
            if(num[k] >= 10) {
                carryNum++;
                num[k + 1]++;
            }
        }
        if(carryNum == 0) {
            cout << "No carry operation." << endl;
        }
        else if(carryNum == 1) {
            cout << "1 carry operation." << endl; 
        }
        else {
            cout << carryNum << " carry operations." << endl;
        }
    }
}