#include<cstdio>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>

using namespace std;
int main(){
	int k,q,r,b,c,p;
	int K=1,Q=1,R=2,B=2,C=2,P=8;
	while(cin>>k>>q>>r>>b>>c>>p){
		cout << K-k << " " << Q-q << " " << R-r << " " << B-b << " " << C-c << " " << P-p << endl; 
	}
}