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
char board[30007][37];
int r,c;

bool tirar(int rc){
	
	for(int cr=0; cr<r;){
		if(board[cr+1][rc]=='X'){
			board[cr][rc]='O';
			return true;
		}
		if(board[cr+1][rc]=='O'){
			if(rc>0 && board[cr][rc-1]=='.' && board[cr+1][rc-1]=='.'){
				cr++;
				rc--;
			}
			else{
				if(board[cr][rc+1]=='.' && board[cr+1][rc+1]=='.'){
					cr++;
					rc++;
				}
				else{
					board[cr][rc]='O';
					return true;
				}
			}
		}
		else{
			cr++;
		}
	}
}
int main(){
	int num,rc;
	memset(board, 'X', sizeof board);
	scanf("%d%d",&r,&c);
	getchar();
	for(int y=0; y<r; ++y){
		for(int x=0; x<c; ++x){
			scanf("%c",&board[y][x]);
		}
		getchar();
	}
	scanf("%d",&num);
	for(int z=0; z<num; ++z){
		scanf("%d",&rc);
		tirar(rc-1);
	}
	for(int y=0; y<r; ++y){
		for(int x=0; x<c; ++x){
			printf("%c",board[y][x]);
		}
		puts("");
	}

}