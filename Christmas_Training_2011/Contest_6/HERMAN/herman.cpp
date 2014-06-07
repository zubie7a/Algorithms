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
	double r;
	double pi = 4*atan(1.0);
	scanf("%lf",&r);
	printf("%.6f\n",r*r*pi);
	printf("%.6f\n",2.0*r*r);	
}