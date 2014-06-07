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

char board[10][10];
bool wut[10][10][10];
int amf;
int posx;
int posy; 
struct punt{
	int val;
	int x;
	int y;
};

vector <punt> punts;


bool itshocksmeagain(int a, int b, int i){
	int res=0;
	for(int j=3*a; j<3*a+3; ++j){
		for(int k=3*b; k<3*b+3; ++k){
			if(wut[i][j][k]==true){
				res++;
			}
			if(board[j][k]-'0'-1==i){
				res=-20;
			}
		}
	}
	if(res==9){
		return false;
	}
	else{
		return true;
	}
}

bool checkforhorror(){
	for(int j=0; j<9; ++j){
		for(int k=0; k<3; ++k){
			for(int l=0; l<3; ++l){
				if(!itshocksmeagain(k,l,j)){
					return false;
				}
			}
		}
	}
	return true;
}

void itjoltsme(){
	for(int i=0; i<punts.size(); ++i){
		for(int l=0; l<9; ++l){
			for(int m=0; m<9; ++m){
				if(l==punts[i].y || m==punts[i].x){
					wut[punts[i].val][l][m]=true;
				}
				for(int k=0; k<9; ++k){
					wut[k][punts[i].y][punts[i].x]=true;
				}
			}
		}
	}
}

void itshocksme(int a, int b, int i){
	amf=0;
	for(int j=3*a; j<3*a+3; ++j){
		for(int k=3*b; k<3*b+3; ++k){
			if(wut[i][j][k]==false){amf++;posx=k;posy=j;}
			if(board[j][k]-1-'0'==i){
				amf=-10;
			}
		}
	}
	if(amf==1){
		board[posy][posx]=i+1+'0';
		punt m;
		m.val = i;
		m.x = posx;
		m.y = posy;
		punts.push_back(m);
		itjoltsme();
	}
}

void electrifying(){
	int j = punts.size();
	for(int i=0; i<9; ++i){
		itjoltsme();
		for(int k=0; k<3; ++k){
			for(int l=0; l<3; ++l){
				itshocksme(k,l,i);
			}
		}
		
	}
	if(j<punts.size()){
		electrifying();
	}
}

int main(){
	bool horror;
	for(int i=0; i<9; ++i){
		for(int j=0; j<9; ++j){
			for(int k=0; k<9; ++k){
				wut[i][j][k] = false;
			}
		}
	}
	for(int i=0; i<9; ++i){
		for(int j=0; j<9; ++j){
			cin >> board[i][j];
			if(board[i][j]!='.'){
				punt z;
				z.val = board[i][j]-'0'-1;
				z.y=i;
				z.x=j;
				punts.push_back(z);
			}
		}
		getchar();
	}
	electrifying();
	horror = checkforhorror();
	if(horror){
		for(int i=0; i<9; ++i){
			for(int j=0; j<9; ++j){
				cout << board[i][j];
			}
			cout << endl;
		}
	}
	else{
		cout << "ERROR" << endl;
	}
}