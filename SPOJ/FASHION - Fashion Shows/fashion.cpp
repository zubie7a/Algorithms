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
    int n,s,p,t;
    cin >> n;
    for(;n;--n){
        s=0;
        cin >> p;
        int h[p];
        int m[p];
        int z[p];
       	for (int i=0; i<p;++i){
            cin >> h[i];                 
        }
        for (int i=0; i<p;++i){
            cin >> m[i];                 
        }
        sort(h,h+p);
        sort(m,m+p);   
        for(int i=0; i<p;++i){
            z[i] = h[i]*m[i];
        }
       	for (int i=0; i<p;++i){
        	s += z[i];    
        }
        cout << s << endl;
    }
}
