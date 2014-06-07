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

int main () {
	int a,b,z;
	cin >> a >> b;
	while(a||b){
		int ap[a];
		int dp[b];
		for(z=0;z<a;++z){
			cin >> ap[z];
		}
		for(z=0;z<b;++z){
			cin >> dp[z];
		}
		sort(ap,ap+a);
		sort(dp,dp+b);
		if(ap[0]<dp[1]){
			cout << "Y" << endl;
		}
		else {
			cout << "N" << endl;
		}
		cin >> a >> b;
	}
}

