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
    string a,acum="";
	int b;
	char temp;
	bool primer = true;
	while((cin>>a)&&(a!=".")){
		cin >> b;
	    acum = "";
		for(int k=0;k<b;++k){
		    acum = acum+a;
		}
		for(int i=0;i<a.size();++i){
		    primer = true;
			cout << acum << endl;
			for(int j=0;j<acum.size();++j){
				if(primer == true){
					temp = acum[j];
					primer = false;
				}
				acum[j]=acum[j+1];
			}
			acum[acum.size()-1]=temp;
		}
	}
}

