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

int divsum[500002];

int main(){
	for (int i=1;i*2<=500000;++i){
		for (int j=i*2;j<=500000;j+=i){
			divsum[j]+=i;
		}
	}
	int nCasos,num;
	scanf("%d",&nCasos);
	for (int i=0;i<nCasos;++i){
		scanf("%d",&num);
		printf("%d\n",divsum[num]);
	}
}
