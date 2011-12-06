#include<cstdio>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>

using namespace std;
int main(){
	int cuts;
	while(cin>>cuts){
		cuts+=2;
		cout << (cuts*cuts)/4 << endl;
	}
}