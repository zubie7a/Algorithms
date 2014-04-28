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
	int N,W,H;
	int x;
	cin >> N >> W >> H;
	for(int i=0; i<N; ++i){
		cin >> x;
		if(x*x <= W*W + H*H){
			cout << "DA" << endl;
		}
		else{
			cout << "NE" << endl;
		}
	}
}