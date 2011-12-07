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
	int n,x,a,c;
	char z;
	while(scanf("%d",&n)!= EOF){
		a=1;
		c=1;
		for(x=1;x<n;x+=a){
			a++;
			c++;
		}
		z = c+64;
		cout << "TERM " << n << " IS " << z << endl;
	}
}
