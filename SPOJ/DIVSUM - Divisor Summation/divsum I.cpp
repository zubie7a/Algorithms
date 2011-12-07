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
	int nCasos,num,x,squara;
	long long int c;
	scanf("%d",&nCasos);
	while(nCasos--){
		scanf("%d",&num);
		if(num==1){c=0;}else{c=1;}
		squara=(int)(sqrt(num));
		for(x=2;x<=squara;++x){
			if(!(num%x)){
				c+=x;
				if(num/x!=x){c+=num/x;}
			}
		}
		printf("%lld\n",c);
	}
}