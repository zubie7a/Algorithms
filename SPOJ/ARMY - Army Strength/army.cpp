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
	int nCasos,x,y,a,b,tempa,tempb;
	scanf("%d\n",&nCasos);
	for(int z=0;z<nCasos;++z){
		printf("\n");
		tempa=0;
		tempb=0;
		scanf("%d%d\n",&x,&y);
		for(int i=0;i<x;++i){
			scanf("%d",&a);
			if(a>tempa){
				tempa=a;
			}
		}
		for(int j=0;j<y;++j){
			scanf("%d",&b);
			if(b>tempb){
				tempb=b;
			}
		}
		if(tempa>=tempb){
			printf("%s\n","Godzilla");
		}
		else {
			printf("%s\n","MechaGodzilla");
		}
	}
}

