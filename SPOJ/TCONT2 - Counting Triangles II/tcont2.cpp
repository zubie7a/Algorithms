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
	long double t,n;
	scanf("%Lf",&t);
	while(t--){
		scanf("%Lf",&n);
		printf("%.0Lf\n",(7*n*n*n)/2+(9*n*n)/4+n/2);
	}
}


