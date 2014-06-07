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
	int s=0,m;
	map<int,int> mod;
	for(int z=0;z<10;++z){
		cin >> m;
		if(!mod[m%42]){
			s++;
			mod[m%42]=1;
		}
	}
	cout << s << endl;
}