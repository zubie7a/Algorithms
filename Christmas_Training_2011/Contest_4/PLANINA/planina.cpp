#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <list>
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

int res[15];
void shine(int base, int pos){
	if(pos==15){return;}
	base = 2*base - 1;
	res[pos] = base*base;
	shine(base,pos+1);
}

int main(){
	int base = 2;
	shine(base,0);
	cin >> base;
	cout << res[base-1] << endl;
}