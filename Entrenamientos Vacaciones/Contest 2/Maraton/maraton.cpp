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
	int N;
	bool neh;
	while(cin >> N){
		neh = true;
		char t[N+4][N+4];
		string G;
		for(int x=0; x<N+4; ++x){
			for(int y=0; y<N+4; ++y){
				t[x][y] = '.';
			}
		}
		for(int x=0; x<N; ++x){
			cin >> G;
			for(int y=0; y<N; ++y){
				t[x+2][y+2] = G[y];
			}
		}
		for(int x=0; x<N+4 && neh; ++x){
		 		for(int y=0; y<N+4 && neh; ++y){
		 			if(t[x][y] == t[x+1][y] && t[x+1][y]==t[x+2][y] && t[x][y]!='.'){
		 				cout << t[x][y] << endl;
		 				neh = false;
		 			}
		 			if(t[x][y] == t[x][y+1] && t[x][y+1]==t[x][y+2] && t[x][y]!='.'){
		 				cout << t[x][y] << endl;
		 				neh = false;
		 			}
		 			if(t[x][y] == t[x+1][y+1] && t[x+1][y+1]==t[x+2][y+2] && t[x][y]!='.'){
		 				cout << t[x][y] << endl;
		 				neh = false;
		 			}
		 			if(t[x][y] == t[x-1][y+1] && t[x-1][y+1]==t[x-2][y+2] && t[x][y]!='.'){
		 				cout << t[x][y] << endl;
		 				neh = false;
		 			}
		 		}
		 	}
		 	if(neh){
		 		cout << "ongoing" << endl;
		 	}
	}
}