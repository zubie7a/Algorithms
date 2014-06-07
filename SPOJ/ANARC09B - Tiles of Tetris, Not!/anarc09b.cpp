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

int gcd(unsigned long long a,unsigned long long b){
	if(b==0){
		return a;
	}
	else{
		return gcd(b,a%b);
	}
}
int main(){
	unsigned long long w,h,r;
	scanf("%llu%llu",&w,&h);
	while(w && h){
		if(w!=h){
			r = w/gcd(w,h)*h;
			r = r/w * r/h;
			printf("%llu\n",r);
		}
		else{
			printf("1\n");
		}
		scanf("%llu%llu",&w,&h);
	}
}