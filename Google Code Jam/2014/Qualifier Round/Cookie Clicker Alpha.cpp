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

double C, F, X;
// C: cost to buy a new cookie factory >:O
// F: production factor that each factory increases :D
// X: total amount of cookies we want :3

double calculate(double rate){
    double total = 0;
    while(true){
        double t1 = X / rate; // Time until the amount of
        // ..cookies is reached without investing in any
        // ..new factory, waiting until the end from now
        double t2 = C / rate; // Time until the next fac-
        // ..tory can be purchased. If a new factory is 
        // ..purchased, the total production rate will be
        // ..increased, but also will take an extra iter-
        // ..ation of deciding whether to wait until the
        // ..end, or buying yet another factory.
        double _t1 = X / (rate + F); // Time it would take
        // ..to reach the amount of cookies without invest-
        // ..ing in any new factory if at this iteration we
        // ..decided to buy a factory, increasing the rate.
        double res = t2 + _t1; // Time it would take to buy
        // ..at least one more factory and possibly stopping
        // ..at the next iteration after buying this factory.
        if(t1 <= res){
            // If its better to stop now or buy a new facto-
            // ..ry and stop at the next iteration. 
            total += t1;
            break;
        }
        rate += F;
        total += t2;
    }
    return total;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int z = 0;z < T;z++){
        scanf("%lf %lf %lf", &C, &F, &X);
        double result = calculate(2);
        printf("Case #%d: ", z + 1);
        printf("%.7lf", result);
        if(z + 1 < T){
            printf("\n");
        }
    }
}