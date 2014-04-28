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
	char given[4][4];
	char desired[4][4];
	int c=0;
	char t;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			desired[i][j]='A'+c;
			c++;
		}
	}
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			scanf("%c",&given[i][j]);
			if(!(given[i][j]>='A' && given[i][j]<='Z')){
				t = given[i][j];
			}
		}
		getchar();
	}
	desired[3][3]=t;
	c=0;
	for(int sa=0;sa<4;++sa){
		for(int sb=0;sb<4;++sb){
			for(int za=0;za<4;++za){
				for(int zb=0;zb<4;++zb){
					if(given[sa][sb]==desired[za][zb] && given[sa][sb]!='.'){
						c+=abs(za-sa)+abs(zb-sb);
					}
				}
			}
		}
	}
	cout << c << endl;
}
	
