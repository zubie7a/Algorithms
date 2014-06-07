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
	int nCasos;
	int numC;
	int base;
	int temp;
	int num1;
	int num2;
	int may;
	int men;
	int acum;
	cin >> nCasos;
	for(int i=0;i<nCasos;++i){
		acum = 0;
		cin >> numC;
		cin >> base;
		cin >> num1;
		cin >> num2;
		if(num1>num2){
			may=num1;
			men=num2;
		}
		else{
			may=num2;
			men=num1;
		}
		vector<int> mayor;
		vector<int> menor;
		for(int k=0;may!=0;++k){
			temp = may%base;
			mayor.push_back(temp);
			may /= base;
		}
		for(int k=0;men!=0;++k){
			temp = men%base;
			menor.push_back(temp);
			men /= base;
		}
		for(int z=0; z<menor.size(); ++z){
			mayor.at(z) += menor.at(z);
			if(mayor.at(z) >= base){
				mayor.at(z) %= base;
			}
		}
		for(int m=0;m<mayor.size();++m){
			acum += mayor.at(m)*(int)(pow((double)base,double(m)));
		}
		cout << numC << " " << acum << endl;
	}
}
