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
	int r;
	int b;
	bool nom = true;
	int total=0;
	scanf("%d%d",&r,&b);
	total = r+b;
	for(int i=3;i<=total/3 && nom;++i){
		for(int j=3;j<total && nom;++j){
			if(i*j==total && (i-2)*(j-2)==b){
				if(i>j){ printf("%d %d",i,j);}
				else {
					printf("%d %d",j,i);
				}
				nom=false;
			}
			if(i*j>total){
				break;
			}
		}
	}
}

