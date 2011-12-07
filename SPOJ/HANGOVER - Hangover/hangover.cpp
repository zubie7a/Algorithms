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
    float n=1.00,m=0.00;
    float ix=1;
    while ((cin >> n)&&(n!=0.00)){
          ix=1;
          while (n>0){
            n-=1/(ix+1);
            ++ix;          
          }
       cout << ix-1 <<" card(s)" << endl;   
    }
}

