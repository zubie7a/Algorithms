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
	string in = "yhesocvxduiglbkrztnwjpfmaq";
	string wt;
	string out;
	int T;
	cin >> T;
	for(int z=0; z<=T; ++z){
		getline(cin,wt);
		if(z==0){continue;}
		out = "";
		for(int s=0; s<wt.length(); ++s){
			if(wt[s]==' '){
				out+=' ';
			}
			else{
			    out+=in[wt[s]-'a'];
			}
		}
		cout << "Case #" << z << ": " << out << endl;
	}
}
