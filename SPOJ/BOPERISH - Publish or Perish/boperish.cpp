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

int compare (const void * a, const void * b){
	return ( *(int*)a - *(int*)b );
}

int main(){
	int caso,n,m;
	scanf("%d",&caso);
	while(caso){
		int cits[caso];
		bool xzek;
		for(n=0;n<caso;n++){	
			scanf("%d",&cits[n]);
		}
		qsort(cits,caso,sizeof(int),compare);
		for(n=0;n<caso;n++){
			xzek=true;
			for(m=0;m<caso && xzek;++m){
				if(m<caso-n){
					if(cits[m]<=n){xzek=true;}
					else {xzek=false;}
				}
				else {
					if(cits[m]>=n){xzek=true;}
					else {xzek=false;}
				}
			}
			if(xzek)break;
		}
		printf("%d\n",n);
		scanf("%d",&caso);
	}
}
