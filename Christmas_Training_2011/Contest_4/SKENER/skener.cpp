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
	int R,C,ZR,ZC;
	cin >> R >> C >> ZR >> ZC;
	char x[R*ZR][C*ZC];
	char m;
	for(int i=0,f=0; i<R; i++,f+=ZR){
		for(int j=0,n=0; j<C; j++,n+=ZC){
			cin >> m;
			for(int k=0; k<ZR; ++k){
				for(int l=0; l<ZC; ++l){
					x[k+f][l+n] = m;
				}
			}
		}
		getchar();
	}
	for(int i=0; i<R*ZR; ++i){
		for(int j=0; j<C*ZC; ++j){
			cout << x[i][j];
		}
		cout << endl;
	}
}