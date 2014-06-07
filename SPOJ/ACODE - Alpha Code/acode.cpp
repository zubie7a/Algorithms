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
	string digits;	
	cin>>digits;
    while(digits!="0"){
		long long int res[5002],val;
		int c=0;
		int siz=digits.size();
		res[siz]=0;
		res[siz+1]=0;
		if(digits[siz-1]!='0')
			res[siz-1]=1;
		else             
			res[siz-1]=0;
		for(int i=siz-2;i>=0;i--){
			res[i]=0;
			if(digits[i]>='1'&&digits[i]<='9'){
				res[i]=res[i+1];
			}
			val=(digits[i]-'0')*10+(digits[i+1]-'0');
			if(val<=26&&val>=10){
				res[i]+=res[i+2];
				if(i+2==siz)
					res[i]+=1;
			}
		}       
		cout<<res[0]<<endl;
		cin>>digits;
	}
}