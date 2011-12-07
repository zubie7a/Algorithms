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
	long double a,b;
	scanf("%Lf%Lf",&a,&b);
	while(a+b>=0){
		if(a/b==(long double)1000.0/(long double)37.0){
            printf("Y\n");
   		}
		else{
			printf("N\n");
		}
	    scanf("%Lf%Lf",&a,&b);
	}       
}
