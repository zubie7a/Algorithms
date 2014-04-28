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
#define llu unsigned long long
using namespace std;

int main(){
	llu n;
	bool divTods;
	bool divDiv;
	vector<llu> tot;
	vector<llu> tat;
	while(cin >> n){
		tot.clear();
		tat.clear();
		llu plate[n];
		for(llu x=0; x<n; ++x){
			cin >> plate[x];
		}
		sort(plate,plate+n);
		for(llu y=1; y<n; ++y){
			plate[y]-=plate[0];
		}
		plate[0]=0;
		for(llu x=0; x<n; ++x){
			for(llu dv=1; dv*dv<plate[x]; ++dv){
				if(plate[x]%dv==0){
					divTods=true;
					for(llu y=0; y<n && divTods; ++y){
						if(plate[y]%dv!=0){
							divTods=false;
						}
					}
					if(divTods){
						tot.push_back(dv);
					}
					divDiv=true;
					for(llu y=0; y<n && divDiv; ++y){
						if(plate[y]%(plate[x]/dv)!=0){
							divDiv=false;
						}
					}
					if(divDiv){
						tot.push_back(plate[x]/dv);
					}
				}
			}
		}
		for(llu z=0;z<tot.size();++z){
			if(tot[z]!=1){
				cout << tot[z];
				if(z+1!=tot.size()){
					cout << " ";
				}
				for(llu s=0;s<tot.size();++s){
					if(tot[s]!=tot[z]){
						tat.push_back(tot[s]);
					}
				}
				tot.clear();
				for(llu s=0;s<tat.size();++s){
					tot.push_back(tat[s]);
				}
				tat.clear();
				z=0;
			}
		}
		cout << endl;
	}
}