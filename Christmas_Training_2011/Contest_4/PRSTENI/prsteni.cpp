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

int gcd(int x, int y){
	if(y==0){
		return x;
	}
	else{
		return gcd(y, x%y);
	}
}
int main(){
	int z,p,s;
	cin >> z >> p;
	for(int i=0; i<z-1; ++i){
		cin >> s;
		cout << p/gcd(p,s) << '/' << s/gcd(p,s) << endl;
	}
}