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
	int n,mayor=0,j;
	int cont;
	scanf("%d",&n);
	while(n!=-1){
		int m[n+1];
		for(int x=0;x<n+1;++x){
			scanf("%d",&m[x]);
			if(x&&(m[x]+m[x-1]>mayor)){
				mayor=m[x]+m[x-1];
			}
		}
		int pos[n];
		for(int z=0;z<n;++z)pos[z]=0;
		while(mayor+1){
			cont=0;
			for(int z=1;z<n+1;++z){
				if((m[z]+m[z-1]==mayor||(m[z]+m[z-1]==mayor-1&&m[z]==m[z-1]))&&!pos[z-1]){
					cont++;
				}
			}
			j=cont;
			for(int x=1;x<n+1 && j;++x){
				if(m[x]+m[x-1]==mayor||(m[x]+m[x-1]==mayor-1&&m[x]==m[x-1])){
					if(!pos[x-1]){
						if(m[x]>m[x-1])printf("/");
						if(m[x]<m[x-1])printf("\\");
						if(m[x]==m[x-1])printf("_");
						pos[x-1]=1;
					}
					j--;
				}
				else printf(" ");
			}
			if(cont)printf("\n");
			mayor--;
		}
		printf("***\n");
		scanf("%d",&n);
	}
}



