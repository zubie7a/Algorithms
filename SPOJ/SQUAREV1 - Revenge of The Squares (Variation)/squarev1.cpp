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
	int n,m,z,k,g;
	double j;
	while(scanf("%d",&n)!=EOF){
		vector<int>s;
		(n<4)?m=n:
		m=sqrt(n);
		for(k=0,z=0;k<m&&n;++k){
			j=sqrt(n-k*k);
			for(g=0;g<z;++g){
				if(s[g]==k){
					n=0;
				}
			}
			if((int)j==j&&n){
				z++;
				s.push_back((int)j);
			}
		}
		printf("%d\n",z);
	}
}



