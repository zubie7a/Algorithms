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
	int a,b,c;
	scanf("%d%d%d",&a,&b,&c);
	while(a!=0||b!=0||c!=0){
		    if (c-b==b-a||a-b==b-c){
				    printf("%s%d\n","AP ",c+c-b);
			}
		    else{
				if (c/b==b/a||a/b==b/c){
					printf("%s%d\n","GP ",c*c/b);
				}
			}
		scanf("%d%d%d",&a,&b,&c);
	  }
}
