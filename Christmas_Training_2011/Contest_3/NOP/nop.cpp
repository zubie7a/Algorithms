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
	int c=0;
	int x;
	int y=0;
	string s;
	cin >> s;
	for(x=1;x<s.length();++x){
		if(s[x]-96>0){c++;}
		else{y+=((c+4)/4)*4-1-c;c=0;}
	}
	cout << y << endl;
}
