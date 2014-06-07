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
    int x;
	long long int y;
	long long int res;
	scanf("%d",&x);
	while(x--){
		scanf("%lld",&y);
		res=(y*(y+2)*(2*y+1))/8;
		printf("%lld\n",res);
	}
}

