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
	int a,b;
	double c,d;
	string res;
	while((cin>>a>>b)&&(a!=-1&&b!=-1)){
		res = "";
		c=((double)a)*((double)100)/((double)b);
		d=((double)a)*((double)20)/((double)b);
		if(abs(((int)c+0)-c)>=abs(((int)c+1)-c)){
			c=c+1;
		}
		if(abs(((int)d+0)-d)>=abs(((int)d+1)-d)){
			d=d+1;
		}
		d=(int)d;
		c=(int)c;
		for(int q=0;q<20;++q){
			if(q<d){
				res+="*";
			}
			else{
				res+="-";
			}
		}
		cout << res.substr(0,9-(c==100)) << c << "%" << res.substr(11+(c>=10),19) << endl;
	}
}