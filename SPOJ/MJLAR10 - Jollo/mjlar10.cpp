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
    int a[5];
    int z=0;
    int b=0;
    bool final;
    while((cin>>a[0]>>a[1]>>a[2]>>a[3]>>a[4])&&(a[0]!=0)&&(a[1]!=0)&&(a[2]!=0)&&(a[3]!=0)&&(a[4]!=0)){
             final=false;
             for(int i=1; i<=52; ++i){
                    z=0;
                    if(a[0]<a[3]){b++;}
                    if(a[1]<a[4]){b++;}
                    if(a[2]<i){b++;}
                    
                    if(b>=2){z++;}
                    b=0;
                    
                    if(a[0]<a[3]){b++;}
                    if(a[1]<i){b++;}
                    if(a[2]<a[4]){b++;}
                    
                    if(b>=2){z++;}
                    b=0;
                    
                    if(a[0]<a[4]){b++;}
                    if(a[1]<a[3]){b++;}
                    if(a[2]<i){b++;}
                    
                    if(b>=2){z++;}
                    b=0;
                    
                    if(a[0]<a[4]){b++;}
                    if(a[1]<i){b++;}
                    if(a[2]<a[3]){b++;}
                    
                    if(b>=2){z++;}
                    b=0;
                    
                    if(a[0]<i){b++;}
                    if(a[1]<a[3]){b++;}
                    if(a[2]<a[4]){b++;}
                    
                    if(b>=2){z++;}
                    b=0;
                    
                    if(a[0]<i){b++;}
                    if(a[1]<a[4]){b++;}
                    if(a[2]<a[3]){b++;}
                    
                    if(b>=2){z++;}
                    b=0;
                   
                    if((z==6)&&(i!=a[0])&&(i!=a[1])&&(i!=a[2])&&(i!=a[3])&&(i!=a[4])){
                        cout << i << endl;
                        final=true;
                        break;
                   }
          }
          if(final==false){ 
                    cout << -1 << endl;
          }    
    }                     
}




