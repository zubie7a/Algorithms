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
	int nCasos,elPropio,acum=0,i=0,lim=0,a,b;
	cin >> nCasos;
	for(;nCasos>0;--nCasos){
		cin >> elPropio;
		acum=0;
		for(i=0; acum < elPropio; ++i){
			acum+=i;
		}
		--i;
		int num[i];
		int den[i];
		lim=i;
		for(int z=0; z<lim ;){
			num[z]=z+1;
			den[z]=i;
			--i;
			++z;
		}
		if(lim%2==0){
			a=num[lim-(acum-elPropio)-1];
			b=den[lim-(acum-elPropio)-1];
		}
		else {
			a=num[acum-elPropio];
			b=den[acum-elPropio];
		}
		cout << "TERM "<< elPropio <<" IS " << a << "/" << b << endl;
	}
}

