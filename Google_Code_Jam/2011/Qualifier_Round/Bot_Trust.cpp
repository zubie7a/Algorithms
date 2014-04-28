#include <iostream>
using namespace std;

int main(){
	int T,N,secs;
	int poso,posb;
	int count,press;
	cin >> T;
	int b2,o2;
	bool oxiste,bxiste;
	int entrab,entrao;
	for(int f=0; f<T; ++f){
		oxiste = false;
		bxiste = false;
		b2=0;
		o2=0;
		entrab=0;
		entrao=0;
		poso=1;
		posb=1;
		secs=0;
		count=0;
		press=0;
		cin >> N;
		char y[N];
		int x[N];
		int o[N];
		int b[N];
		for(int k=0; k<N; ++k){
			cin >> y[k] >> x[k];
			if(y[k]=='O'){     
				o[o2]=x[k];		 
				o2++;			 
				oxiste = true;   
				entrao++;      
			}
			if(y[k]=='B'){
				b[b2]=x[k];    
				b2++;
				bxiste = true;
				entrab++;
			}
		}
		o2=0;
		b2=0;
		for(secs=0;press!=N;++secs){
			if(y[count]=='O'){					 
				if(poso!=x[count]){		   
					if(poso>x[count]){poso--;}    
					else{poso++;}				  
				}
				else{
					if(poso==x[count]){
						count++;		 
						o2++;		  
						press++;     						
						if(o2==entrao){oxiste=false;}
					}
				}
				if(bxiste){
					if(posb!=b[b2]){			 
						if(posb>b[b2]){posb--;} 
						else{posb++;}	
					}				 
				}
			}
			else {
				if(y[count]=='B') {        
					if(posb!=x[count]){
						if(posb>x[count]){posb--;}
						else{posb++;}
					}
					else{
						if(posb==x[count]){
							count++;
							b2++;
							press++;
							if(b2==entrab){bxiste=false;}
						}
					}
					if(oxiste){
						if(poso!=o[o2]){
							if(poso>o[o2]){poso--;}   
							else{poso++;}
						}
					}
				}
			}
		}
		cout << "Case #" << f+1 << ": " << secs << endl;
	}
}