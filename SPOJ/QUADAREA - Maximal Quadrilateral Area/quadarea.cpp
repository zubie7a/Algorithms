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
	double w,x,y,z,s;
	int nCasos;
	scanf("%d",&nCasos);
	for(int i=0;i<nCasos;++i){
		scanf("%lf%lf%lf%lf",&w,&x,&y,&z);
		s = 0.5*(w+x+y+z);
		printf("%lf\n",sqrt((s-w)*(s-x)*(s-y)*(s-z)));
	}
}