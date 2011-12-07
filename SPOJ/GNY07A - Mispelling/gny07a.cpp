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
    int casos;
    cin >> casos;
    string arreglo[casos];
    string acum ="";
    int numlug[casos];
    for (int i=0; i<casos; ++i){
        cin >> numlug[i];
        cin >> arreglo[i]; 
    }   
    
    for (int j=0; j<casos; ++j){
        acum = "";
        for (int i=0; i<numlug[j]-1; ++i){
        	acum = acum+arreglo[j].at(i);
        }
        for (int i=numlug[j]; i<arreglo[j].length(); ++i){
        	acum = acum+arreglo[j].at(i);
        }
        arreglo[j]=acum;
    }
    
    for (int j=0; j<casos; ++j){
    	cout << j+1 << " " << arreglo[j] << endl;    
    }
    return 0;
}

