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
    char z[100][100];
	char y[100][100];
    int nCasos;
	int a,b,c,UP,RIGHT,DOWN,LEFT;
    cin>>nCasos;
    for(int i=0;i<nCasos;++i){
        cin>>a>>b>>c;
        for(int q=0;q<a;++q){
			for(int p=0;p<b;++p){
				cin>>z[q][p];
				y[q][p]=z[q][p];
			}
		}
		for(int dias=0;dias<c;++dias){
            for(int m=0;m<a;++m){
				for(int n=0;n<b;++n){
					UP=m-1;
					RIGHT=n+1;
					DOWN=m+1;
					LEFT=n-1;
					if(UP<0){UP=0;}
					if(RIGHT>b){RIGHT=b;}
					if(DOWN>a){DOWN=a;}
					if(LEFT<0){LEFT=0;}
					if(z[m][n]=='W'){
						if(y[UP][n]=='G'||y[m][RIGHT]=='G'||y[DOWN][n]=='G'||y[m][LEFT]=='G'){
							z[m][n]='G';
						}
					}
					else{ 
						if(z[m][n]=='A'){
							if(y[UP][n]=='W'||y[m][RIGHT]=='W'||y[DOWN][n]=='W'||y[m][LEFT]=='W'){
								z[m][n]='W';
							}
						}
						else{ 
							if(z[m][n]=='G'){
								if(y[UP][n]=='A'||y[m][RIGHT]=='A'||y[DOWN][n]=='A'||y[m][LEFT]=='A'){
									z[m][n]='A';
								}
							}
						}
					}
				}
			}	
            for(int q=0;q<a;++q){
				for(int p=0;p<b;++p){
					y[q][p]=z[q][p];
				}
			}
		}
        for(int q=0;q<a;++q){
            for(int p=0;p<b;++p){
				cout<<z[q][p];
			}
            cout<<endl;
        }
    }
}
