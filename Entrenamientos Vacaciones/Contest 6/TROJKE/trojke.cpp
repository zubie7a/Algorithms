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

bool linea(int x1, int x2, int x3, int y1, int y2, int y3){
	return (x2-x1)*(y3-y2) == (y2-y1)*(x3-x2) && (x3-x1)*(y3-y2) == (y3-y1)*(x3-x2);
}
int main(){
	int n;
	cin >> n;
	char tab[n][n];
	int x[27],y[27]; //pos de cada letra
	int iter=0;
	int res=0;
	for(int i=0;i<n;++i){
		for(int j=0;j<n;++j){
			cin >> tab[i][j];
			if(tab[i][j]!='.'){
				x[iter]=j;
				y[iter]=i;
				iter++;
			}
		}
	}
	for(int s=0;s<iter-2;++s){
		for(int m=s+1;m<iter-1;++m){
			for(int z=m+1;z<iter;++z){
				if(linea(x[s],x[m],x[z],y[s],y[m],y[z])){
					res++;
				}
			}
		}
	}
	cout << res << endl;
}
	
