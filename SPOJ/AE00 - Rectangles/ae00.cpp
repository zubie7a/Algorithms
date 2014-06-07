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
    int n,rectangulos=0;
    scanf("%d\n",&n);
    for (int i=1;i<=n;++i){
        for (int j=1;j*j<=i;++j){
            if (i%j==0){
                rectangulos++;
            }
        }
    }
    printf("%d\n",rectangulos);
}