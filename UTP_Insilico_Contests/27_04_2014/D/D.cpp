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
	/*
	 Tobby is a dog who loves cute sequences.
	 A cute sequence is one such that:
	 >. It has size N (3 <= N <= 1000)
	 >. Every number is unique
	 >. Every number is 0 < Ai < 10^9
	 >. Each Ai (0 < i < n) must satisfy:
	      |Ai-1 - Ai| > |Ai - Ai+1|
	 >. Tobby is such a nice dog :)
	*/

	/*
	 The solution is easy: Compute a list which
	 starts at 1, then increments 1 to 2, then
	 increments 2 to 4, then increments 3 to 7,
	 etc. This way, the absolute difference be-
	 tween a pair of numbers will be always bi-
	 gger than the absolute difference of the
	 next pair. So the numbers will go like:

	 1 (+1) 2 (+2) 4 (+3) 7 (+4) 11 (+5) 16

	 Also, reverse the list, because the numbers
	 have to be in a decreasing order.

	*/
	int N;
	vector<int> nums;
	int cur = 1;
	int inc = 1;
	for(int i = 0; i < 1000; i++){
		nums.push_back(cur);
		cur += inc;
		inc++;
	}
	reverse(nums.begin(), nums.end());
	while(scanf("%d", &N) != EOF){
		for(int i = 0; i < N; i++){
			printf("%d", nums[i]);
			if(i + 1 < N){
				printf(" ");
			}
		}
		printf("\n");
	}	
}