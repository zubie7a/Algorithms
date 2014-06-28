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
// This program is an interpreter of instructions. A certain computer has ten
// registers, and 1000 words of RAM. Each register or RAM location holds a 3
// digit integer between 0 and 999. Instructions are encoded as 3 digit inte-
// gers and stored in RAM. The encodings are as follows:
//
// 100 - halts execution
// 2dn - r[d] = n ... sets reg_d to n (between 0 and 9)
// 3dn - r[d] += n ... add n to reg_d
// 4dn - r[d] *= n ... multiply reg_d by n
// 5ds - r[d] = r[s] ... set reg_d to reg_s
// 6ds - r[d] += r[s] ... add reg_s to reg_d
// 7ds - r[d] *= r[s] ... multiply reg_d by reg_s
// 8da - r[d] = ram[r[a]] ... set reg_d to the val of RAM's address in reg_a
// 9sa - ram[r[a]] = r[s] ... set the val of RAM's address in reg_a to reg_s
// 0ds - iter = r[d] ... go to the location in reg_d unless reg_s contains 0
// ... Otherwise the instruction iterator changes incrementally.
//
// All registers initially contain 000. The initial content of RAM is read from
// standard input. The first instruction to be executed is at RAM address 0 and
// all results are reduced modulo 1000.
    int n;
    // Number of test cases to be read
    cin >> n;
    int RAM[1000];
    int REG[10];
    for(int z = 0; z < n; z++) {
        for(int k = 0; k < 10; k++) {
        // Reset the values of all 10 registers, which by default are all in 0
            REG[k] = 0;
        }
        for(int k = 0; k < 1000; k++) {
        // Reset the value of all 1000 RAM words. The initial contents of RAM
        // are given via standard input, all unspecified positions are in 0.
            RAM[k] = 0;
        }
        string line;
        int count = 0;
        // Not all RAM words are read, so we want to know how many have we read
        while(getline(cin, line)) {
            if(line == "") {
            // Empty line marks the end of RAM word content in standard input
                break;
            }
            stringstream ss(line);
            int value;
            ss >> value;
            RAM[count++] = value;
        }
        if(count == 0) {
        // This means a blank line was read, which is useful to distinguish
        // between cases read via standard input. Diminish the case number iter
        // ator so that a blank line isn't counted as a case. 
            z--;
            continue;
        }
        int index = 0;
        int operationCount = 0;
        bool finish = false;
        while(!finish) {
        // Execute operations stored in RAM until we reach a halt operation
        // Instruction/RAM Word: ABC
        // A: desired operation
        // B: target register
        // C: origin register/value
            operationCount++;
            int A = (RAM[index] / 100) % 10;
            int B = (RAM[index] /  10) % 10;
            int C = (RAM[index] /   1) % 10;
            index++;
            switch(A) {
            case 1: {
                finish = true;
                break;
            }
            case 2: {
            // Set target register B to a determined value C
                REG[B] = C;
                break;
            }
            case 3: {
            // Add to target register B a determined value C
                REG[B] = (REG[B] + C) % 1000;
                break;
            }
            case 4: {
            // Multiply target register B by a determined value C
                REG[B] = (REG[B] * C) % 1000;
                break;
            }
            case 5: {
            // Set target register B to the value of a origin register C
                REG[B] = REG[C];
                break;
            }
            case 6: {
            // Add to target register B the value of a origin register C
                REG[B] = (REG[B] + REG[C]) % 1000;
                break;
            }
            case 7: {
            // Multiply target register B by the value of a origin register C
                REG[B] = (REG[B] * REG[C]) % 1000;
                break;
            }
            case 8: {
            // Set target register B to the value in RAM whose address is in the
            // origin register B... a bit confusing, lets try it.
                REG[B] = RAM[REG[C]];
                break;
            }
            case 9: {
            // Set the value in RAM whose address is in origin register to that
            // value of target register... a bit confusing, lets try it.
                RAM[REG[C]] = REG[B];
                break;
            }
            case 0: {
            // Go to the address in target register B unless the origin regis-
            // ter C contains an address pointing to 0.
                if(REG[C] != 0) {
                    index = REG[B];
                }
                break;
            }
            default: {
                break;
            }
            }
        }
        cout << operationCount << endl;
        if(z + 1 < n) {
        // But a blank line between consecutive cases. IGNORING LEADS TO WA!
            puts("");
        }
    }
}