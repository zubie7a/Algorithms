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
	long long int a,c=0,b,x;
	while((cin>>a)&&(a!=0)){
		c=0;
		b=a;
		for(x=1;b>0;){
			if(b-x>0){
				c++;
			}
			b -= x;
			x *=2;
		}
		cout << c << endl;
	}
}
