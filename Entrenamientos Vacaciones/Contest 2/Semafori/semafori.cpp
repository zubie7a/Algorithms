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
	int n,l;
	int pos;
	int iter;
	int tiempo;
	while(cin >> n >> l){
		int d[n];
		int r[n];
		int g[n];
		int t[n];
		bool sem[n];
		pos = iter = tiempo = 0;
		for(int x=0; x<n; ++x){
			cin >> d[x] >> r[x] >> g[x];
			sem[x]=false;
			t[x]=0;
		}
		while(pos<l){
			tiempo++;
			if(pos<d[iter]){
				pos++;
				for(int x=iter;x<n;++x){
					t[x]++;
					if(sem[x]==false){
						if(t[x]==r[x]){
							sem[x]=true;
							t[x]=0;
						}
					}
					else{
						if(t[x]==g[x]){
							sem[x]=false;
							t[x]=0;
						}
					}
				}
			}
			else{
				if(sem[iter]==true){
					pos++;
					iter++;
				}
				for(int x=iter;x<n;++x){
					t[x]++;
					if(sem[x]==false){
						if(t[x]==r[x]){
							sem[x]=true;
							t[x]=0;
						}
					}
					else{
						if(t[x]==g[x]){
							sem[x]=false;
							t[x]=0;
						}
					}
				}
			}
		}
		cout << tiempo << endl;
	}
}