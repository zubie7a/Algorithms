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
    int n;
	scanf("%d",&n);
	while(n!=0){
		   int casos[n];
		   int i;
		for(i=0;i<n;++i) {
			scanf("%d",&casos[i]);
		}
		for(i=0;i<n;++i) {
			if(casos[i]!=(i+1)&&casos[casos[i]-1]!=(i+1)){
				printf("%s\n","not ambiguous");
				break;
			}
		}
		if(i==n){
		printf("%s\n","ambiguous");
		}
		scanf("%d",&n);
	}
}