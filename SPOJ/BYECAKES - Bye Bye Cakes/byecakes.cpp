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
	int e,f,s,m,ep,fp,sp,mp;
	int cte,ctf,cts,ctm;
	while((scanf("%d%d%d%d%d%d%d%d\n",&e,&f,&s,&m,&ep,&fp,&sp,&mp))&&e+f+s+m+ep+fp+sp+mp!=-8){
		cte=0;
		ctf=0;
		cts=0;
		ctm=0;
		while(e!=0||f!=0||s!=0||m!=0){
			e-=ep;
			if(e<0){cte+=abs(e);e=0;}
			f-=fp;
			if(f<0){ctf+=abs(f);f=0;}
			s-=sp;
			if(s<0){cts+=abs(s);s=0;}
			m-=mp;
			if(m<0){ctm+=abs(m);m=0;}
		}
		printf("%d %d %d %d\n",cte,ctf,cts,ctm);
	}
}

