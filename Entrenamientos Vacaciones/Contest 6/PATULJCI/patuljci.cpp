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
	int total=0;
	int enanos[9];
	for(int z=0;z<9;++z){
		cin >> enanos[z];
		total += enanos[z];
	}
	for(int s=0;s<8;++s){
		for(int m=s+1;m<9;++m){
			if(total-enanos[s]-enanos[m]==100){
				enanos[s]=-1;
				enanos[m]=-1;
			}
		}
	}
	for(int z=0;z<9;++z){
		if(enanos[z]!=-1){
			cout << enanos[z] << endl;
		}
	}
}