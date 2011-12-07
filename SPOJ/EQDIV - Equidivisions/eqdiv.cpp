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

int map1[102][102];
bool map2[102][102];
int cont;

void posit(int n, int y, int x){
	map2[y][x]=true;
	
	if(y<n-1 && map1[y+1][x]==map1[y][x] && map2[y+1][x]==false){
		posit(n,y+1,x);
		cont++;
	}
	if(y>0 && map1[y-1][x]==map1[y][x] && map2[y-1][x]==false){
		posit(n,y-1,x);
		cont++;
	}
	if(x<n-1 && map1[y][x+1]==map1[y][x] && map2[y][x+1]==false){
		posit(n,y,x+1);
		cont++;
	}
	if(x>0 && map1[y][x-1]==map1[y][x] && map2[y][x-1]==false){
		posit(n,y,x-1);
		cont++;
	}
}

int main(){
	int ncase,y,x;
	bool nom;
	scanf("%d",&ncase);
	while(ncase){
		nom=true;
		int pos[2][ncase];
		for(int a=0;a<ncase-1;++a){
            for(int b=0;b<ncase;++b){
					  scanf("%d%d",&y,&x);
					  map1[y-1][x-1]=a+1;
					  if(nom){
						pos[0][a]=y-1;
						pos[1][a]=x-1;
						nom=false;
					  }
				if(ncase==b+1){while(getchar()!='\n');} 
            }
            nom=true;
		}
		for(int a=0;a<ncase && nom;++a){
            for(int b=0;b<ncase && nom;++b){
				if(map1[a][b]==0){
					pos[0][ncase-1]=a;
					pos[1][ncase-1]=b;
					nom = false;
				}
            }
		}
		for(int m=0;m<ncase;++m){
            cont = 1;
            posit(ncase, pos[0][m],pos[1][m]);
            if(cont!=ncase){
				printf("wrong\n");
				break;
            }
		}
		if(cont==ncase) {
            printf("good\n");
		}
		for(int a=0;a<ncase;++a){
            for(int b=0;b<ncase;++b){
				if(map1[a][b]!=0){map1[a][b]=0;}
				if(map2[a][b]==true){map2[a][b]=false;}
            }
		}
		scanf("%d",&ncase);
	}
}
