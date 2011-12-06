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

struct point{
	double x;
	double y;
	vector<linea>com;
};

bool comun(point a, point b){
	vector<linea>ac = a.com;
	vector<linea>bc = b.com;
	for(ull A=0; A<ac.size(); ++A){
		for(ull B=0; B<bc.size(); ++B){
			if(ac[A].a.x==bc[B].a.x && ac[A].a.y==bc[B].a.y  &&  ac[A].b.x==bc[B].b.x && ac[A].b.y==bc[B].b.y){
				return true;
			}
		}
	}
	return false;
}

bool noline(point a, point b, point c){
	vector<linea>ac = a.com;
	vector<linea>bc = b.com;
	vector<linea>cc = c.com;
	for(ull A=0; A<ac.size(); ++A){
		for(ull B=0; B<bc.size(); ++B){
			for(ull C=0; C<cc.size();++C){
				if(ac[A].a.x==bc[B].a.x && ac[A].a.y==bc[B].a.y  &&  ac[A].b.x==bc[B].b.x && ac[A].b.y==bc[B].b.y){
					if(bc[B].a.x==cc[C].a.x && bc[B].a.y==cc[C].a.y  &&  bc[B].b.x==cc[C].b.x && bc[B].b.y==cc[C].b.y){
						if(cc[C].a.x==ac[A].a.x && cc[C].a.y==ac[A].a.y  &&  cc[C].b.x==ac[A].b.x && cc[C].b.y==ac[A].b.y){
							return false;
						}
					}
				}
			}
		}
	}
	return true;
}

int main(){	
	vector<linea>p;
	vector<point>t;
	point z;
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
		t.clear();
		contador = 0;
		for(int c=0;c<nCasos;++c){//aqui empieza el ciclo que lee segmentos y fusiona los que se sobreponen
			col = false;
			cin >> x1 >> y1 >> x2 >> y2; //lectura de cada segmento
			if(x1!=x2){					 
				m = (y2-y1)/(x2-x1);	 //sacar la pendiente
			}
			else{
				m = 65536; 				 //pendiente grande ~ infinito?
			}
			for(ull j=0; j<p.size() && !col; ++j){
				if(p[j].slope == m){	//primero se fija si ya existe algun segmento de igual pendiente
					if((y1-p[j].a.y == m*(x1-p[j].a.x) && y2-p[j].b.y == m*(x2-p[j].b.x)) || (x1==x2)){ //y ese segmento resuelve perfecto para los x1,y1,x2,y2 actuales	
						if((x1>=p[j].a.x && x1<=p[j].b.x) || (x1>=p[j].b.x && x1<=p[j].a.x) || (x2>=p[j].a.x && x2<=p[j].b.x) || (x2>=p[j].b.x && x2<=p[j].a.x)){ // y el x1 o x2 del segmento actual esta entre los x del segmento del ciclo
							if((y1>=p[j].a.y && y1<=p[j].b.y) || (y1>=p[j].b.y && y1<=p[j].a.y) || (y2>=p[j].a.y && y2<=p[j].b.y) || (y2>=p[j].b.y && y2<=p[j].a.y)){ // y el y1 o y2 del segmento actual esta entre los y del segmento del ciclo
								col = true; //es que los segmentos son colineales y sobrepuestos
								//aqui se hallan los extremos del nuevo segmento
								minx = min(min(x1,p[j].a.x),min(x2,p[j].b.x));
							    miny = min(min(y1,p[j].a.y),min(y2,p[j].b.y));
	 						  	maxx = max(max(x1,p[j].a.x),max(x2,p[j].b.x));
								maxy = max(max(y1,p[j].a.y),max(y2,p[j].b.y));
								if(m<0){//para los segmentos descendientes, el extremo izquierdo es XminYmax y el derecho XmaxYmin
									p[j].a.x = minx;
									p[j].a.y = maxy;
									p[j].b.x = maxx;
									p[j].b.y = miny;
								}
								else{//para el resto de segmentos el extremo izquierdo es XminYmin y el derecho XmaxYmax
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
			if(!col){//Si el segmento actual no es colineal y sobrepuesto con ningun otro, lo agregaremos a la lista de segmentos
				linea s;
				s.slope = m;
				s.a.x = x1;
				s.a.y = y1;
				s.b.x = x2;
				s.b.y = y2;
				p.push_back(s);
			}
		}//aqui termina el ciclo que ingresa los segmentos y fusiona los que se sobreponen.
		for(ull j=0; j<p.size()-1; ++j){//aqui empieza el ciclo que haya intersecciones
			for(ull k=j+1; k<p.size(); ++k){//ciclo anidado para coger de a 2 rectas
				if(p[j].slope != p[k].slope){//como primera condicion, la pendiente debe ser distinta
					//empieza la brujeria de andres mejia para hallar la interseccion de rectas
					x = y = 1e100;
					x0 = p[j].a.x;
					y0 = p[j].a.y;
					x1 = p[j].b.x;
					y1 = p[j].b.y;
					x2 = p[k].a.x;
					y2 = p[k].a.y;
					x3 = p[k].b.x;
					y3 = p[k].b.y;
		   	 		t0 = (y3-y2)*(x0-x2)-(x3-x2)*(y0-y2);
			    	t1 = (x1-x0)*(y2-y0)-(y1-y0)*(x2-x0);
			    	det = (y1-y0)*(x3-x2)-(y3-y2)*(x1-x0);
			   		t0 /= det;
					t1 /= det;
					if(0.0<=t0 && t0<=1.0 && 0.0<=t1 && t1<=1.0){
				      	x = x0 + t0*(x1-x0);
						y = y0 + t0*(y1-y0);
						//hasta aqui llega la brujeria de andres mejia, para hayar la interseccion de rectas
						if((p[j].a.x<=x && x<=p[j].b.x) || (p[j].b.x<=x && x<=p[j].a.x)){ //estos if verifican que el punto hallado este en el rango
							if((p[j].a.y<=y && y<=p[j].b.y) || (p[j].b.y<=y && y<=p[j].a.y)){//de los dos segmentos que estamos trabajando
								z.com.clear();
								z.x = x;//porque puede que como rectas se intersecten, pero este punto este afuera del rango de los segmentos
								z.y = y;
								col = true;
								for(ull f=0;f<t.size() && col;++f){//vamos a revisar en un arreglo de puntos a ver si este punto no fue encontrado previamente
									if(t[f].x == z.x && t[f].y == z.y){//en caso de que si fue encontrado
										col = false;
										t[f].com.push_back(p[j]);//al punto le metemos los nuevos segmentos q estan pasando por el, de esta manera aunque
										t[f].com.push_back(p[k]);//cojamos de 2 en 2 segmentos, se pueden encontrar todos los segmentos que pasan por un punto
									}
								}
								if(col){//si el punto no fue encontrado previamente
									z.com.push_back(p[j]);//se le guarda al punto los 2 segmentos que pasan por el
									z.com.push_back(p[k]);
									t.push_back(z);//y se mete el punto a una lista de puntos
								}
							}
						}
			       	}
				}
			}
		}//aqui termina el ciclo que haya intersecciones
		for(ull j=0; j<t.size()-2; ++j){//aqui empieza el ciclo que halla triangulos
			for(ull s=j+1; s<t.size()-1; ++s){//ciclo triple anidado, de manera que no se repiten combinaciones
				for(ull q=s+1; q<t.size(); ++q){//y asi no toca marcar los visitados
					if(comun(t[s],t[q]) && comun(t[q],t[j]) && comun(t[j],t[s]) && noline(t[j],t[s],t[q])){
							//comun es que los dos puntos pasados como parametro, en su lista de segmentos que pasan por el
							//tengan al menos un segmento en comun. se forma un triangulo si el punto a tiene segmento comun
							//con b, b tiene segmento comun con c, y c tiene segmento comun con a.
							//a la ves hay una verificacion noline que se fija que los 3 puntos no pertenezcan al mismo segmento.
							contador++;
					}
				}
			}
		}//aqui termina el ciclo que haya triangulos
		cout << contador << endl;
	}		
}	

