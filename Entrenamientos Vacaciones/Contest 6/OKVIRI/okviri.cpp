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
	char bordado[5][82];
	string nombre;
	cin >> nombre;
	int n = nombre.length();
	int x=0;
	int c=2;
	for(int s=0;s<5;++s){
		for(int z=0;z<4*n+1;++z){
			bordado[s][z]='.';
		}
	}
	
	for(int j=0;j<n;++j){
		bordado[2][c]=nombre[x];
		x++;
		c+=4;
	}	
	//primera y ultima fila
	int primf = 2;
	int secf = 1;
	int tref = 0;
	for(int i=0;i<4*n+1;++i){
		if(i==primf){
			bordado[0][primf]='#';
			bordado[4][primf]='#';
			primf+=4;
		}
		if(i==secf){
			bordado[1][secf]='#';
			bordado[3][secf]='#';
			secf+=2;
		}
		if(i==tref){
			bordado[2][tref]='#';
			tref+=4;
		}
	}
	
	int cont = 0;
	for(int i=0;i<4*n+1;++i){
		if(bordado[0][i]=='#'){
			cont++;
		}
		if(cont==3){
			cont = 0;
			for(int s=0;s<5;++s){
				for(int z=i-2;z<=i+2;++z){
					if(bordado[s][z]=='#'){
						bordado[s][z]='*';
					}
				}
			}
		}
	}
	for(int i=0;i<5;++i){
		for(int j=0;j<4*n+1;++j){
			cout << bordado[i][j];
		}
		cout << endl;
	}

	
}