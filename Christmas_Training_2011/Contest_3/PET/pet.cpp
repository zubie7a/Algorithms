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
	int p[5][4];
	int r=0;
	int q;
	int s=0;
	for(int i=0;i<5;++i){
		for(int j=0;j<4;++j){
			cin >> p[i][j];
			r += p[i][j];
		}
		if(r>s){
			s=r;
			q=i;
		}
		r=0;
	}
	cout << q+1 <<" "<< s << endl;
}