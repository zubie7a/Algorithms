#include<cstdio>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<cmath>

using namespace std;


int main(){
	int x;
	while(cin>>x){
		cout << ((x-3)*(x-2)*(x-1)*x)/4<<endl;
	}
}