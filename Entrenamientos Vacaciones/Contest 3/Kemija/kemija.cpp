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
	string a;
	string b;
	getline(cin,a);
	for(int j=0; j<a.size()-2; ++j){
		if(a[j+1]=='p' && ( (a[j]=='a' && a[j+2]=='a') || (a[j]=='e' && a[j+2]=='e') || (a[j]=='i' && a[j+2]=='i') || (a[j]=='o' && a[j+2]=='o') || (a[j]=='u' && a[j+2]=='u') ) ){
		 	a[j+1] = a[j+2] = '.';
		}       
	}
	for(int i=0; i<a.size(); ++i){
		if(a[i]!='.'){
			cout << a[i];
		}
	}
	cout << endl;
}