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
	long long a,b,c,d,g,h;
	int e,T,f;
	cin >> T;
	long long pot[8];
	for(int b=0,n=1;b<8;++b){
		pot[b]=n;
		n*=10;
	}
	set < pair < long long, long long > > seti;
	for(int z=1; z<=T; ++z){
		seti.clear();
		cin >> a >> b;
		d = a;
		e = 0; 
		while(d){
			d/=10;
			e++;
		}
		for(int s=a; s<=b; ++s){
			f = e-1;
			while(f){
				g = s% pot[e-f];
				g *= pot[f];
				h = s/pot[e-f];
				f--;
				g = g+h;
				if(a<=g && g<=b && s<g){
					seti.insert(make_pair(s,g));
				}
			}
		}
		cout << "Case #" << z << ": " << seti.size() << endl;
	}
}