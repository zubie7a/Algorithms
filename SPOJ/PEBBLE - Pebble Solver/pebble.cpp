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
     string a;
     int c;
     int num;
     int s=0;
     while(cin>>a){
          num=1;
          c=0;
          for(int z=0;z<a.size();++z){
              if(a[z]==num+'0'){
                  c++;
                  if(num==0)num=1;
                  else num=0;
              }
          }
          s++;
          cout << "Game #"<<s<<": "<<c<<endl;
     }
}
