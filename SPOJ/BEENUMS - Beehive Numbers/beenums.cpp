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

int main () {
    int num;
	int acumz;
	scanf("%d\n",&num);
	while (num!=-1&&num>=0){
	    acumz = 0;
	    for(int z=0;z<num;z++){
	    	acumz = acumz + z;
		    if(6*acumz+1==num){
				printf("%s\n","Y");
				break;
		   	}
		    if(6*acumz+1>num){
	            printf("%s\n","N");
        	    break; 
	        }
        }
		scanf("%d\n",&num);
    }
}
