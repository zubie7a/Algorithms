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
	 For a number up to 400, which is the amount of different pairs of prime numbers
	 that can be added that will result in the given number? Like goldbach conjecture.
	*/
	int primes[78] = {  2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
		               59, 61, 67, 71, 73, 79, 83, 89, 97,101,103,107,109,113,127,131,
		              137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,
		              227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,
		              313,317,331,337,347,349,353,359,367,373,379,383,389,397};
    // Precomputed list of primes up to 400, given in the problem statement. 
    int nums[401];
    for(int i = 0; i < 401; i++){
    	nums[i] = 0;
    }
    for(int i = 0; i < 78; i++){
    	int prime = primes[i];
    	nums[prime] = prime;
    }
    // The 'nums' array will contain the primes at their positions, others are just 0.
    int T, N;
    scanf("%d", &T);
    while(T--){
    	scanf("%d", &N);
    	int total = 0;
    	for(int i = 1; i <= N/2; i++){
    		// If the currently iterated number is not a prime, its array value is 0.
    		if(nums[i] == 0) continue;
    		int p1 = nums[i];
    		// Now, the number at the current position is the first prime.
    		int p2 = nums[N - p1];
    		// And the other is at N - p1, which hopefully will be prime. 
    		if(p1 + p2 == N){
    			/*
    			 If its not prime, then its 0, and this sum will not yield N.
    			 But if there is a prime there, then p1 + p2 MUST give N since
    			 p2 was found with N - p1.
    			*/
    			total++;
    		}
    	}
    	printf("%d\n", total);
    }
}