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
    int x,y,n;
    scanf("%d",&n);
    for(;n>0;--n){
        scanf("%d%d",&x,&y);
        if (x==y||x-y==2){
            printf("%d\n",x+y-x%2);                    
        }
        else{
            printf("%s\n","No Number");
        }
    }
}