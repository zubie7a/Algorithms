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
	int nCasos,HHH=0,HHT=0,HTT=0,TTT=0,HTH=0,THT=0,TTH=0,THH=0;
	cin >> nCasos;
	string y[nCasos];
	string x;
	int z[nCasos];
	for(int j=0;j<nCasos;++j){
		cin >> z[j];
		cin >> y[j];
	}
	for(int k=0;k<nCasos;++k){
		HHH=0;
		HHT=0;
		HTT=0;
		TTT=0;
		HTH=0;
		THT=0;
		TTH=0;
		THH=0;
		cout << z[k] << " ";
		x = y[k];
		for (int i=0;i<38;++i){
			if(x[i]=='H'&&x[i+1]=='H'&&x[i+2]=='H'){HHH++;}
			if(x[i]=='H'&&x[i+1]=='H'&&x[i+2]=='T'){HHT++;}
			if(x[i]=='H'&&x[i+1]=='T'&&x[i+2]=='T'){HTT++;}
			if(x[i]=='T'&&x[i+1]=='T'&&x[i+2]=='T'){TTT++;}			
			if(x[i]=='H'&&x[i+1]=='T'&&x[i+2]=='H'){HTH++;}
			if(x[i]=='T'&&x[i+1]=='H'&&x[i+2]=='T'){THT++;}
			if(x[i]=='T'&&x[i+1]=='T'&&x[i+2]=='H'){TTH++;}
			if(x[i]=='T'&&x[i+1]=='H'&&x[i+2]=='H'){THH++;}
		}
		cout << TTT << " " << TTH << " " << THT << " " << THH << " " << HTT << " " << HTH << " " << HHT << " " << HHH << endl;
	}

}