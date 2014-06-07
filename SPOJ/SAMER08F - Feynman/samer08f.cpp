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
    int n=1,acum=0;
    while ((cin >> n)&&(n!=0)){
          acum=0;
          for (float i=0; i<=n; ++i){
              acum=acum+i*i;
          }
     cout << acum << endl;     
    }
    return 0;
}
