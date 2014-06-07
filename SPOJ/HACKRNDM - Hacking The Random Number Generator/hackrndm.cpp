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
	long long n,k,c=0;
	scanf("%lld %lld",&n,&k);
	long long nums[n];
	for(int i=0;i<n;++i){
		scanf("%lld",&nums[i]);
	}
	sort(nums,nums+n);
	for(int i=0;i<n-1;++i){
		for(int j=i+1;j<n && nums[j]-nums[i]<=k;++j){
			if(nums[j]-nums[i]==k){
				c++;
			}
		}
	}
	printf("%lld\n",c);
}