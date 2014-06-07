#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstdlib>
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
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>
#define ull unsigned long long
#define EPS 1e-9
using namespace std;

int main(){	
	int caso;
	int cont;
	int res;
	string nombre;
	while(cin >> caso){
		res = 0;
		map <string,int> mapa;
		vector<string> vector;
		for(int j=0; j<caso; ++j){
			cont = 0;
			cin >> nombre;
			if(!mapa[nombre]){
				mapa[nombre]=1;
			}
			else{
				mapa[nombre] = mapa[nombre] + 1;
			}
			vector.push_back(nombre);
			for(int x=0;x<vector.size();++x){
				if(vector[x]!=nombre){
					cont++;
				}
			}
			if(cont+1<mapa[nombre]){
				res++;
			}
		}
		cout << res << endl;
	}
}	

