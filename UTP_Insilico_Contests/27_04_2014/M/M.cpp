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

pair<int, int> arr[1000001];

int main(){
    /*
     Which is the number with the most divisors
     that is less or equal than N? NOW WITH A HUGE LIMIT
    */
    int T, N;
    scanf("%d", &T); // Number of Test Cases

    /*
     This time it wont suffice to go around finding the
     divisors for each number, but instead, in a list of 
     numbers all with 2 divisors (except 1), start from
     the low numbers, increasing by 1 the amount of divi-
     sors of their multiples. I actually thought of this
     for the previous problem but was too lazy to do it 
     so I resorted for using the modulo operation for fin-
     ding the divisors of each number.
    */
    int divs[1000001];
    divs[1] = 1; // 1 is the special case
    for(int i = 2; i <= 1000000; i++){
        divs[i] = 2; // All other numbers will have 2 divs
    }

    for(int base = 2; base <= 500000; base++){
        /*
         The starting base number is 2. This means that up
         to 1000000, the number of divisors of all the mul-
         tiples of 2 will be increased.
        */
        for(int i = 2 * base; i <= 1000000; i += base){
            /*
             All the multiples of the current base number
             will be 'increased', as in their number of
             divisors being increasingly bigger.
            */
            divs[i]++;
        }
    }
    arr[1] = make_pair(1,1);
    // Now, Ye Olde Record Holder algorithm!
    for(int i = 2; i <= 1000000; i++){
        int old_num = arr[i-1].first;  // The previously record holder
        int old_div = arr[i-1].second; // The divisors of the record holder
        /*
         Record Holder: the smallest number upto a certain place, which has
         the mosts divisors. At each place the number that would be the rec-
         ord holder until there is storaged.
        */
        int new_num = i; 
        int new_div = divs[i];
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

