#include<cstdio>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<cmath>

using namespace std;


string strCompare(string a,string b){
	int x=min(a.size(),b.size());
	for(int y=0;y<x;++y){
		if(a[y]<b[y]){
			return a;
		}
		if(b[y]<a[y]){
			return b;
		}
	}
	if(a.size()<b.size()){
		return a;
	}
	else {
		return b;
	}

}

int main(){
	int R,C;
	while(cin>>R>>C){
		string res="";
		string temp="";
		string temp2="";
		
		char m[R][C];
		for(int r=0;r<R;++r){
			for(int c=0;c<C;++c){
				cin >> m[r][c];
			}
			getchar();
		}

		
		for(int r=0;r<R;++r){
			res="";
			for(int c=0;c<C;++c){
				if(m[r][c]!='#'){
					res += m[r][c];
				}
				else {
					if(res.size()>=2){
						if(temp==""){
							temp=res;
						}
						else{
							temp = strCompare(temp,res);
						}
					}
					res="";
				}
			}
			if(res.size()>=2){
				if(temp==""){
					temp=res;
				}
				else{
					temp = strCompare(temp,res);
				}
			}
		}
		for(int c=0;c<C;++c){
			res="";
			for(int r=0;r<R;++r){
				if(m[r][c]!='#'){
					res += m[r][c];
				}
				else {
					if(res.size()>=2){
						if(temp2==""){
							temp2=res;
						}
						else{
							temp2 = strCompare(temp2,res);
						}
					}
					res="";
				}
			}
			if(res.size()>=2){
				if(temp2==""){
					temp2=res;
				}
				else{
					temp2 = strCompare(temp2,res);
				}
			}
		}
		cout << strCompare(temp,temp2) << endl;
	}
}


