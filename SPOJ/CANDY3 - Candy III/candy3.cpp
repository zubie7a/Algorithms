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
    long long int nCasos,nKids,sum,a;
    scanf("%lld",&nCasos);
    for (long long int k=0;k<nCasos;++k){
        sum=0;
        scanf("%lld",&nKids);
        a=0;
        for (long long int j=0; j<nKids; ++j){
            scanf("%lld",&a);    
            a %= nKids;
            sum += a;
        }
        printf("\n");        
        if(sum%nKids==0){
              printf("YES\n");        
        }
        else{
              printf("NO\n");        
        }  
    }
}