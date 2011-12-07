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
    int p0,bet,pf;
    while((cin>>p0>>bet>>pf)&&((p0!=0)||(bet!=0)||(pf!=0))){
          if ((p0-pf)%bet!=0){
               cout << "No accounting tablet" << endl;
          }else{
                   if (abs(pf-p0)%(bet*3)==0){ 
                       cout << abs(pf-p0)/(bet*3) << endl;
                   }
                   else{
                       cout << abs(pf-p0)/(bet*3) + 1 << endl;         
                   }
              
               
          }           
     }
}