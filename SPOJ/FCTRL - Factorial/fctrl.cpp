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
	int l,i,n,u,x;
	cin >> i;
	for(l=0;l<i;l++){
		cin >> n;
	    u = 0;
	    x=n/5;
        u+=x;
	    while(x>=5){
		x/=5;
		u+=x;
		}
	    cout << u << endl;
	}
}
