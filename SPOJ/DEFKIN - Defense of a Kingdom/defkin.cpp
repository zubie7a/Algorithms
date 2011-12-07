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
	int nCasos,x,y,t,mayor=0;
	scanf("%d\n",&nCasos);
	for(;nCasos>0;--nCasos){
		scanf("%d%d%d\n",&x,&y,&t);
		int tx[t+2];
		int ty[t+2];
		tx[0]=0;
		ty[0]=0;
		t++;
		tx[t]=x;
		ty[t]=y;
		for(int k = 1; k <= t-1; ++k){
			scanf("%d\n",&tx[k]);
			scanf("%d\n",&ty[k]);
		}
		sort(tx,tx+t);
	    sort(ty,ty+t);
		int distx[t];
		int disty[t];
		for(int z=0;z<t;++z){
			distx[z]=tx[z+1]-tx[z]-1;
			disty[z]=ty[z+1]-ty[z]-1;
		}
		distx[t-1]++;
		disty[t-1]++;
		sort(distx,distx+t);
		sort(disty,disty+t);
		mayor = distx[t-1]*disty[t-1];
		printf("%d\n",mayor);
	}
}
