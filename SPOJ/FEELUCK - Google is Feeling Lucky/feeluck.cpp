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
    int nCasos;
	cin >> nCasos;
	string pags[10];
	int rating[10];
	int mayor;
	for (int s=1; s<=nCasos; ++s) {
		mayor = 0;
		for(int k=0; k<10; ++k){
			cin >> pags[k];
			cin >> rating[k];
			if(rating[k]>mayor){
				mayor = rating[k];
			}
		}
		cout << "Case #" << s << ":" << endl;
		for(int z=0; z<10; ++z){
			if(mayor == rating[z]){
				cout << pags[z] << endl;
			}
		}
	}
}