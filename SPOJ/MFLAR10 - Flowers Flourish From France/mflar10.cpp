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
    bool worda=true,meg=false;
    char mega;
    int j;
    string word="";
    while(word!="*"){
        worda=true;
        meg=false;
        getline(cin,word);
        if (word=="*"){
			break;
		}
    	for(int i=0; i < word.size(); ++i){
			word[i] = tolower(word[i]);
		}
        for(j=0;(j<word.size())&&(meg==false);++j){
                if(word[j]!=' '){
					mega=word[j];
                    meg=true;
				}
        }            
        for(int i=j;(i<word.size())&&(worda==true);++i){
                if((mega==word[i])&&(word[i-1]==' ')){
					worda=true;
				}
                if((mega!=word[i])&&(word[i-1]==' ')){
					worda=false;
				}
        }
        if(worda==true){
			cout<<"Y"<<endl;
		}
        else{
			cout<<"N"<<endl;
		}
    }
}


