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
    int nCasos,radio;
    double res;
    scanf("%d",&nCasos);
    for(int a=1;a<=nCasos;a++){
        scanf("%d",&radio);
        res=((double)radio*radio*4)+0.25;
        printf("Case %d: %.2f\n",a,res);
    }
}
