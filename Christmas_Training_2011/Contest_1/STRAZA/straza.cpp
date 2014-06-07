#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstdlib>
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
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>
#define ull unsigned long long
#define EPS 1e-9
using namespace std;

struct punto{
	double x;
	double y;
};

struct linea{
	double slope;
	punto a;
	punto b;
};

int cmp(double x, double y = 0, double tol = EPS) {
    return (x<=y+tol)?(x+tol<y)?-1:0:1;
}

punto comun(linea a, linea b, double x0, double x1, double x2, double x3, double y0, double y1, double y2, double y3, double t0, double t1, double det, double x, double y){
		punto z;
		z.x = 1e100;
		z.y = 1e100;
		if(a.slope != b.slope){
			x0 = a.a.x;
			y0 = a.a.y;
			x1 = a.b.x;
			y1 = a.b.y;
			x2 = b.a.x;
			y2 = b.a.y;
			x3 = b.b.x;
			y3 = b.b.y;
   	 		t0 = (y3-y2)*(x0-x2)-(x3-x2)*(y0-y2);
	    	t1 = (x1-x0)*(y2-y0)-(y1-y0)*(x2-x0);
	    	det = (y1-y0)*(x3-x2)-(y3-y2)*(x1-x0);
			if(cmp(det,0)==0){
				return z;
			}
	   		t0 /= det;
			t1 /= det;
			if(0.0<=t0 && t0<=1.0 && 0.0<=t1 && t1<=1.0){
		      	x = x0 + t0*(x1-x0);
				y = y0 + t0*(y1-y0);
				if((a.a.x<=x && x<=a.b.x) || (a.b.x<=x && x<=a.a.x)){ 
					if((a.a.y<=y && y<=a.b.y) || (a.b.y<=y && y<=a.a.y)){
						z.x=x;
						z.y=y;
						return z;
					}
				}
	       	}
		}
		return z;
}

bool coli(punto a, punto b, punto c ) {
    return cmp(0,(b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y))==0;
}


int main(){	
	vector<linea>p;
	int nCasos;
	double x1;
	double y1;
	double x2;
	double y2;
	double x0;
	double y0;
	double x3;
	double y3;
	double x;
	double y;
	double m;
	double t0;
	double t1;
	double det;
	double minx;
	double miny;
	double maxx;
	double maxy;
	int contador;
	bool col;
	while(cin>>nCasos){
		p.clear();
		contador = 0;
		for(int c=0;c<nCasos;++c){
			col = false;
			cin >> x1 >> y1 >> x2 >> y2;
			if(x1!=x2){					 
				m = (y2-y1)/(x2-x1);
			}
			else{
				m = 65536; 		
			}
			for(ull j=0; j<p.size() && !col; ++j){
				if(p[j].slope == m){
					if((y1-p[j].a.y == m*(x1-p[j].a.x) && y2-p[j].b.y == m*(x2-p[j].b.x)) || (x1==x2)){
						if((x1>=p[j].a.x && x1<=p[j].b.x) || (x1>=p[j].b.x && x1<=p[j].a.x) || (x2>=p[j].a.x && x2<=p[j].b.x) || (x2>=p[j].b.x && x2<=p[j].a.x)){ 
							if((y1>=p[j].a.y && y1<=p[j].b.y) || (y1>=p[j].b.y && y1<=p[j].a.y) || (y2>=p[j].a.y && y2<=p[j].b.y) || (y2>=p[j].b.y && y2<=p[j].a.y)){ 
								col = true; 
								minx = min(min(x1,p[j].a.x),min(x2,p[j].b.x));
							    miny = min(min(y1,p[j].a.y),min(y2,p[j].b.y));
	 						  	maxx = max(max(x1,p[j].a.x),max(x2,p[j].b.x));
								maxy = max(max(y1,p[j].a.y),max(y2,p[j].b.y));
								if(m<0){
									p[j].a.x = minx;
									p[j].a.y = maxy;
									p[j].b.x = maxx;
									p[j].b.y = miny;
								}
								else{
									p[j].a.x = minx;
									p[j].a.y = miny;
									p[j].b.x = maxx;
									p[j].b.y = maxy;
								}
							}
						}
					}
				}				
			}
			if(!col){
				linea s;
				s.slope = m;
				s.a.x = x1;
				s.a.y = y1;
				s.b.x = x2;
				s.b.y = y2;
				p.push_back(s);
			}
		}
		
		for(ull j=0; j<p.size()-2; ++j){
			for(ull s=j+1; s<p.size()-1; ++s){
				for(ull q=s+1; q<p.size(); ++q){
					punto a = comun(p[s],p[q],x0,x1,x2,x3,y0,y1,y2,y3,t0,t1,det,x,y);
					punto b = comun(p[q],p[j],x0,x1,x2,x3,y0,y1,y2,y3,t0,t1,det,x,y);
					punto c = comun(p[j],p[s],x0,x1,x2,x3,y0,y1,y2,y3,t0,t1,det,x,y);
					if(a.x!=1e100 && b.x!=1e100 && c.x!=1e100 && a.y!=1e100 && b.y!=1e100 && c.y!=1e100 && !coli(a,b,c)){
							contador++;
					}
				}
			}
		}
		cout << contador << endl;
	}		
}



