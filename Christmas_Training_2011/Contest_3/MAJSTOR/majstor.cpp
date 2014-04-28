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


int resRonda(char letra, int ronda, string nv[], int N){
	int puntaje = 0;
	for(int i=0; i<N; ++i){
		if(letra==nv[i][ronda]){
			puntaje += 1;
			continue;
		}
		if(letra=='S' && nv[i][ronda]=='P'){
			puntaje += 2;
			continue;
		}
		if(letra=='P' && nv[i][ronda]=='R'){
			puntaje += 2;
			continue;
		}
		if(letra=='R' && nv[i][ronda]=='S'){
			puntaje += 2;
			continue;
		}
	}
	return puntaje;
}


int main(){
	int R;
	string sv;
	int N;
	cin >> R;
	cin >> sv;
	cin >> N;
	string nv[N];
	int ascor, lscor;
	ascor = lscor = 0;
	for(int i=0; i<N; ++i){
		cin >> nv[i];
	}
	for(int j=0; j<R; ++j){
		ascor += resRonda(sv[j],j,nv,N);
		lscor += max(resRonda('S',j,nv,N),max(resRonda('P',j,nv,N),resRonda('R',j,nv,N)));
	}
	cout << ascor << endl << lscor << endl;
}