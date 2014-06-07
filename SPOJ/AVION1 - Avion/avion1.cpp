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
	string x;
	bool find = false;
	for(int k=0;k<5;++k){
		cin >> x;
		if(x.size()<3){
			continue;
		}
		for(int i=0;i<x.size();++i){
			if(x[i]=='F'&&x[i+1]=='B'&&x[i+2]=='I'){
				cout << k+1 << " ";
				find = true;
				break;
			}
			if(i==x.size()-3){
				break;
			}
		}
	}
	if(find==false){
		cout << "HE GOT AWAY!";
	}
}
