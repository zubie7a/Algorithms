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
	long long int a,c=0,b;
	while((cin>>a)&&(a!=0)){
		c=0;
		b=a;
		c= floor(log((double)b)/log((double)2));
		cout << c << endl;
	}
}
