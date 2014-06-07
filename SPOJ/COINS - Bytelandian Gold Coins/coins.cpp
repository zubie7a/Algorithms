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

map<unsigned long long,unsigned long long> mapa;

unsigned long long partirMonedas(unsigned long long n){
	if(n<12){ 
		return n;
	}
	else{
		if(mapa[n]){ 
			return mapa[n];
		}
		mapa[n] = partirMonedas(n/2) + partirMonedas(n/3) + partirMonedas(n/4);
		return mapa[n];
	}
}
int main(){
	unsigned long long n;
    while(scanf("%llu",&n)!=EOF){
		n = partirMonedas(n);
		printf("%llu\n",n);
	}
}

