#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int nCasos;
	int nCreate;
	int nOppose;
	int strLeng;
	int pos;
	int pos1;
	int pos2;
	int loca;
	int locb;
	string stringa;
	string a;
	string b;
	string c;
	string temp;
	string intemp;
	cin >> nCasos;
	for(int t=0;t<nCasos;++t){
		
		cin >> nCreate;
		
		string create[nCreate];
		string mixes1[nCreate];
		string mixes2[nCreate];
		string into[nCreate];
		for(int i=0;i<nCreate;++i){
			cin >> create[i];
			temp=create[i];
			a=temp[0];
			b=temp[1];
			c=temp[2];
			mixes1[i]=a+b;
			mixes2[i]=b+a;
			into[i]=c;
		}
		
		
		cin >> nOppose;
		string oppose[nOppose];
		string opBegin[nOppose];
		string opEnd[nOppose];
		for(int i=0;i<nOppose;++i){
			cin >> oppose[i];
			temp = oppose[i];
			opBegin[i]=temp[0];
			opEnd[i]=temp[1];
		} 
		
		
		cin >> strLeng;
		cin >> stringa;
		temp = "";
		for(int j=0;j<strLeng;++j){
			temp = temp + stringa[j];
			
			pos = 10000;
			for(int l=0;l<nCreate;++l){
				if(temp.find(mixes1[l]) != -1){
					pos = temp.find(mixes1[l]);
					intemp = into[l];
				}
				if(temp.find(mixes2[l]) != -1){
					pos = temp.find(mixes2[l]);
					intemp = into[l];
				}
			}
			if(pos!=10000){
				temp.replace(temp.length()-2,2,intemp);
			}
			
			pos2=-10000;
			pos1=10000;
			
			for(int l=0;l<nOppose;++l){
				a = opBegin[l];
				b = opEnd[l];
				loca=temp.find(a);
				locb=temp.find(b);
				if((loca<locb)&&loca!=-1&&locb!=-1){
					pos1=loca;
					pos2=locb;
				}
				else {
					if((locb<loca)&&loca!=-1&&locb!=-1){
						pos1=locb;
						pos2=loca;
					}
				}
			}
			if(pos1!=10000&&pos2!=-10000&&pos1!=-1&&pos2!=-1){
				temp.replace(0,temp.length(),"");
			}
		}
		cout << "Case #" << t+1 << ": [";
		for(int i=0;i<temp.length();++i){
			cout << temp[i];
			if(i<temp.length()-1){
				cout <<", ";
			}
		}
		cout << "]" << endl;
	}
}