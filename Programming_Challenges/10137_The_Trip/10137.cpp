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
    double acum;
    // Total of money spent in a trip
    vector<double> spentList;
    // List to store what everyone has spent
    int n;
    // Number of people in each trip to be read
    double a, z;
    // Amount of money that should change hands
    while(scanf("%d", &n) && n) {
        acum = 0;
        a = z = 0;
        spentList.clear();
        for(int k = 0; k < n; k++) {
            double moneySpent;
            scanf("%lf", &moneySpent);
            spentList.push_back(moneySpent);
            acum += moneySpent;
        }
        acum /= n;
        // This lets us find the average of money that everyone should've paid
        for(int k = 0; k < n; k++) {
            // Difference between what a people paid and what it should've paid
            if(spentList[k] < acum) {
            // The k-th person spent less than it should have
               double diff = acum - spentList[k];
               a += (double)(int)(diff * 100) / 100;
            }                
            if(spentList[k] > acum){
            // The k-th person spent more than it should have
               double diff = spentList[k] - acum;
               z += (double)(int)(diff * 100) / 100;
            }    
        }   
        if(a > z){
            printf("$%.2lf\n", a);
        }
        else{
            printf("$%.2lf\n", z);
        }
    }
}