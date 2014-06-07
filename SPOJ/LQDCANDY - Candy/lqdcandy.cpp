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
	unsigned long long nCasos,acum,barra,cont,corte,orig;
	scanf("%llu",&nCasos);
	while(nCasos--){
		acum=1;
		cont=0;
		corte=0;
		scanf("%llu",&barra);
		while(acum<barra){
			acum*=2;
		}
		orig=acum;
		if(acum!=barra)
			while(cont<barra){
				acum/=2;
				if(cont+acum<=barra){
					cont+=acum;
				}
				corte++;
			}
		printf("%llu %llu\n",orig,corte);
	}
}
