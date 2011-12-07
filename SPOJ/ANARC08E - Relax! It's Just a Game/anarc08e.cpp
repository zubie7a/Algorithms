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
	int nCasos,a,b,c,sum;
	cin >> nCasos;
	for(int i=0;i<nCasos;++i){
		cin >> a >> b >> c;
		sum = 0;
		for (int j=0;j<a;++j){
		    sum = sum + b + c*j;
		}
	    cout << sum << endl;
	}
}
