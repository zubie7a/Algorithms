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
	int x,y,posx,posy,xbol,ybol,nCasos,count;
	int dirx=1,diry=1;
	bool nocyc;
	scanf("%d\n",&nCasos);
	for(;nCasos>0;--nCasos){
		scanf("%d%d%d%d\n",&x,&y,&xbol,&ybol);
		count = 0;
		xbol--;
		ybol--;
		posx=xbol;
		posy=ybol;
		bool point[x][y];
		nocyc=true;
		for(int s=0;s<x;++s){
			for(int z=0;z<y;++z){
				point[s][z]=false;
			}
		}
		point[xbol][ybol]=true;
		while(point[xbol][ybol]==true){
			if( (posx==0 && posy==0)||(posx==x-1 && posy==0)||(posx==x-1 && posy==y-1)||(posx==0 && posy==y-1) ){
				nocyc=false;
				break;
			}
			posx+= dirx;
			posy+= diry;
			if(posy == y){diry *= -1; posy -= 2;}
			if(posy < 0){diry *= -1; posy += 2;}
			if(posx == x){dirx *= -1; posx -= 2;}
			if(posx < 0){dirx *= -1; posx += 2;}
			
			if(point[posx][posy]==false){
				point[posx][posy]=true;
			}
			else {
				point[posx][posy]=false;
			}
		}
		if(nocyc==false){
			printf("%d\n",2);
		}
		else{
			for(int s=0;s<x;++s){
				for(int z=0;z<y;++z){
					if(point[s][z]==true){
						count++;
					}
				}
			}
			count++;
			printf("%d\n",count);
		}
	}
	
}

