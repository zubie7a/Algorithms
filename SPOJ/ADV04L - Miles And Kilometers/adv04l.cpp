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
typedef unsigned long long ul64;

int main(){
	int nCasos;
	ul64 mile,x,kame,z;
	scanf("%d",&nCasos);
	while(nCasos--){
		scanf("%llu",&mile);
		kame=0;
		ul64 fibs[102];
		fibs[0]=1;
		fibs[1]=1;
		for(x=2; x<102; ++x) {
			fibs[x]=fibs[x-1]+fibs[x-2]; 
			if(fibs[x]>mile)break;
		}
		for(z=0;mile>0;++z){
			if(fibs[z]>mile){
				mile-=fibs[z-1];
				kame+=fibs[z];
				z=0;
			}
		}
		printf("%llu\n",kame);
	}
}
