#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstdlib>
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
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>
#define ull unsigned long long
#define EPS 1e-9
using namespace std;

int main(){	
	int x,y,a,b;
	string t;
	while(cin>>x>>y){
		char card[x][y];
		for(int X=0; X<x; X++){
			cin >> t;
			for(int Y=0; Y<y; Y++){
				card[X][Y]=t[Y];
			}
		}	
		char carta[2*x][2*y];
		for(int X=0; X<x; X++){
			for(int Y=0; Y<y; Y++){
				carta[X][Y] = card[X][Y];
				carta[2*x-1-X][Y] = card[X][Y];
				carta[X][2*y-1-Y] = card[X][Y];
				carta[2*x-1-X][2*y-1-Y] = card[X][Y];
			}
		}
		
		cin >> a >> b;
		if(carta[a-1][b-1]=='#'){
			carta[a-1][b-1]='.';
		}
		else{
			carta[a-1][b-1]='#';
		}
		for(int X=0; X<2*x; ++X){
			for(int Y=0; Y<2*y; ++Y){
				cout << carta[X][Y];
			}
			cout << endl;
		}
	}
}	

