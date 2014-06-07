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
	unsigned long long int n,m,z,k,g;
	char x[21];
	double j;
	for(m=0;m<21;++m){
		x[m]=0;
	}
	while(scanf("%s",&x)!=EOF){
		for(m=0,n=1;m<21;++m){
			if(x[m]=='0')
				x[m]++;
			if(x[m])
				n*=x[m]-'0';
		}		
		vector<int>s;
		m=(n<4)?n:sqrt(n);
		for(k=0,z=0;k<m&&n;++k){
			j=sqrt(n-k*k);
			for(g=0;g<z;++g)
				if(s[g]==k)
					n=0;
			if((int)j==j&&n){
				z++;
				s.push_back((int)j);
			}
		}
		printf("%llu\n",z);
		for(m=0;m<21;++m){
			x[m]=0;
		}
	}
}

