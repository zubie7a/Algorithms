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
	int a[10];
	for (int i=0;i<10;++i){
	    cin >> a[i];
	}
	int acum=0;
	for (int j=0;j<10;++j){
		acum += a[j];
		if (acum>=100){
			if (acum>100&&(acum-100>(100-(acum-a[j])))){
			    acum -= a[j];
			}
			break;
		}
	}
	cout << acum << endl;
}
