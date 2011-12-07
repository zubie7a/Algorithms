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

int posx[10002];
bool visita[10002];

int nadyiet(int g, vector <int> graph[]){
	visita[g]=true;
	for(int k=0;k<graph[g].size();++k){
		if(!visita[graph[g][k]]){
			posx[g]+= nadyiet(graph[g][k],graph)+1;
		}
	}
	return ++posx[g];
}

int main(){
	int nCasos;
	int nodos;
	int a,b;
	scanf("%d",&nCasos);
	for(int z=0;z<nCasos;++z){
		scanf("%d",&nodos);
		vector <int> node[nodos];
		for(int z=0;z<nodos-1;++z){
			scanf("%d%d",&a,&b);
			node[a].push_back(b);
			node[b].push_back(a);
		}
		a=nadyiet(0,node);
		for(int i=1;i<nodos;++i){
			posx[0]+=posx[i];
			posx[i]=0;
			visita[i]=false;
		}
		printf("%d\n",posx[0]);
		posx[0]=0;
		visita[0]=false;
	}
}

