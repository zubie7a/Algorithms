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
	long double nCasos,a,b,c;
	scanf("%Lf",&nCasos);
	while(nCasos--){
		scanf("%Lf%Lf%Lf",&a,&b,&c);
		printf("%.2Lf\n",0.5*((a*a)/4*sqrt(3)+(b*b)/4*sqrt(3)+(c*c)/4*sqrt(3)+3*sqrt((a+b+c)/2*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))));
	}
}
