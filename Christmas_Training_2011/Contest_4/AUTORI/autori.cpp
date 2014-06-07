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
	string a;
	cin >> a;
	for(int i=0; i<a.size(); ++i){
		if(a[i]<=90 && 65<=a[i){
			cout << a[i];
		}
	}
	cout << endl;
}