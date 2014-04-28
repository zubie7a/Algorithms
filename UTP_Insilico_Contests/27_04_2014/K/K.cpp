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

pair<int, int> arr[2501];

int main(){
	/*
	 Which is the number with the most divisors
	 that is less or equal than N?
	*/
	int T, N;
	scanf("%d", &T); // Number of Test Cases
	arr[1] = make_pair(1,1);
	/*
	 1 is a special case, only one divisor, all other numbers
	 have at least a couple divisors (1 and the number itself)
	*/
	for(int i = 2; i <= 2500; i++){
		// Hard Limit is 2500, so lets compute until that value
		int old_num = arr[i-1].first;  // The previously record holder
		int old_div = arr[i-1].second; // The divisors of the record holder
		/*
		 Record Holder: the smallest number upto a certain place, which has
		 the mosts divisors. At each place the number that would be the rec-
		 ord holder until there is storaged.
		*/
		int new_num = i; // New number
		int new_div = 2; // The base amount of divisors is 2
		for(int j = 2; j <= new_num / 2; j++){
			if(new_num % j == 0){
				new_div++; // Count how much other divisors the number has.
			}
		}
		pair<int, int> p;
		if(new_div > old_div){
			/*
		     If the number of divisors of this number is greater than the
		     ones of the previous record holder, then store this number.
		     Also, this will ensure only the first found record holder with
		     X divisors will be stored, any other number with the same num-
		     ber of divisors will be skipped since it only accepts greater
		     values, not the equal ones.
			*/
			p.first = new_num;
			p.second = new_div;
		}
		else{
			/*
			 If the previous record holder remains unbeaten, then store it
			 back, this way, querying a position will give the number that
			 is the record holder up to this position.
			*/
			p.first = old_num;
			p.second = old_div;
		}
		arr[i] = p;
	}
	while(T--){
		scanf("%d", &N);
		printf("%d\n", arr[N].first);
	}
}

