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

int main() {
    int N, M, C;
    // N: number of devices, <= 20
    // M: operations performed on these devices
    // C: capacity of the fuse, in amperes
    int numCase = 1;
    while(cin >> N >> M >> C) {
        if(!N && !M && !C) {
        // Input is terminated with a case of 0 0 0
            break;
        }
        int consumptions[N + 1];
        for(int k = 1; k <= N; k++) {
        // The energy consumption in amperes for the k-th device
            cin >> consumptions[k];
        }
        bool toggles[N + 1];
        for(int k = 1; k <= N; k++) {
        // At the beginning, all the devices are turned off
            toggles[k] = false;
        }
        int maxConsumption = 0;
        int totalConsumption = 0;
        for(int k = 0; k < M; k++) {
            int toggledDevice;
            cin >> toggledDevice;
            // This will turn ON or OFF the k-th device.
            if(toggles[toggledDevice] == false) {
            // If the device was OFF, turn it ON and add its energy to the
            // running total of energy consumption.
                totalConsumption += consumptions[toggledDevice];
                toggles[toggledDevice] = true;
            }
            else{
            // If the device was ON, turn it OFF and remove its energy from the
            // running total of energy consumption.
                totalConsumption -= consumptions[toggledDevice];
                toggles[toggledDevice] = false;
            }
            maxConsumption = max(maxConsumption, totalConsumption);
            // Keep track of what the final max consumption is by comparing it
            // against the total consumption at each point in time.
        }
        cout << "Sequence " << numCase++ << endl;
        if(maxConsumption > C) {
        // If the max consumption exceed the fuse capacity, then it will have
        // blown at some given point, either the max capacity or some other
        // capacity lower than it, but if the max is bigger, then for sure it
        // will have blown off.
            cout << "Fuse was blown." << endl << endl;
            // an extra blank line at end of case, stupid PRESENTATION ERROR.
        }
        else {
        // If the max consumption of all the steps didn't exceed the fuse cap-
        // acity, then it can be said for sure that the fuse did never blown.
            cout << "Fuse was not blown." << endl;
            cout << "Maximal power consumption was " 
                 << maxConsumption << " amperes." << endl << endl;
                 // an extra blank line at end of case, stupid PRESENTATION ERROR.
        }
    }
}