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
	int a,b,acum;
	while((cin>>a>>b)&&a&&b){
		int xa[a],xb[b];
		acum=0;
		for(int i=0;i<a;++i){
			cin >> xa[i];
		}
		for(int i=0;i<b;++i){
			cin >> xb[i];
		}
		for(int j=0;j<a;++j){
			for(int z=0;z<b;++z){
				if(xa[j]==xb[z]){
					xb[z]=0;
					break;
				}
			}
		}
		for(int j=0;j<a;++j){
			acum+=xa[j];
		}
		for(int z=0;z<b;++z){
			acum+=xb[z];
		}
		cout << acum << endl;
	}
}