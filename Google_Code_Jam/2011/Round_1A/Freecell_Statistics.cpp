#include <iostream>

using namespace std;
int main(){
	int nCasos;
	cin >> nCasos;
	int N,Pd,Pg;
	bool valid;
	string caso = "Case #";
	string pos1 = ": Possible";
	string pos2 = ": Broken";
	double aux2;
	double percent;
	for(int i=0;i<nCasos;++i){
		valid = false;
		cin >> N >> Pd >> Pg; 
		for(int z=1;z<=N;++z){
			percent = (double)(Pd)/(double)(100);
			aux2 = (double)(z)*percent;
			if((int)aux2==aux2){
				valid = true;
				break;
			}
		}
		if(valid==true){
			if(Pg==100){
				if(Pd==100){
					cout << caso << i+1 << pos1 << endl;
				}
				else {
					cout << caso << i+1 << pos2 << endl;
				}
			}
			else {
				if(Pg==0){
					if(Pd==0){
						cout << caso << i+1 << pos1 << endl;
					}
					else {
						cout << caso << i+1 << pos2 << endl;
					}
				}
				else{
					cout << caso << i+1 << pos1 << endl;
				}
			}
			
		}
		else {
			cout << caso << i+1 << pos2 << endl;
		}
	}
	
}