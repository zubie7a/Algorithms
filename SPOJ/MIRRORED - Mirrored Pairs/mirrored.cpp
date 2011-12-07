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
	string m;
	getline(cin,m);
	cout << "Ready" << endl;
	while(m[0]!=' ' && m[1]!=' '){
		if(m[0]=='d' && m[1]=='b' || m[0]=='q' && m[1]=='p' || m[0]=='b' && m[1]=='d' || m[0]=='p' && m[1]=='q'){
			cout << "Mirrored pair" << endl;
		}
		else {
			cout << "Ordinary pair" << endl;
		}
		getline(cin,m);
	}
}



