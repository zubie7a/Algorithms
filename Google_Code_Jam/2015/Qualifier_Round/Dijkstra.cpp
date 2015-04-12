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

#define ull unsigned long long
using namespace std;

// 0:  1, 1:  i, 2:  j, 3:  k
// 4: -1, 5: -i, 6: -j, 7: -k

int neg(int quat) {
    return (quat + 4) % 8;
}

int mult(int quat1, int quat2) {
    // First, the basic * 1 or * -1 operations.
    if(quat2 == 0) return quat1;
    // X * 1 == X
    if(quat1 == 0) return quat2;
    // 1 * Y == Y
    if(quat2 > 3) return neg(mult(quat1, neg(quat2)));
    // If the second value is negative, make it positive and neg the result.
    if(quat1 > 3) return neg(mult(neg(quat1), quat2));
    // If the first value is negative, make it positive and neg the result.

    // From here on we ideally want to deal only with positive things. If some-
    // thing negative was received, the previous conditions will change their
    // sign and then revert the sign change.

    if(quat1 == quat2) return 4;
    // Equal quaternions will result in a -1.

    if((quat1 + 1) % 3 != quat2 % 3) {
    // We'll make a swap so that they have a  i -> j -> k -> i ordering, if a
    // pair was changed to create that order, then multiply the swap and then
    // negate the result.
        return neg(mult(quat2, quat1));
    }

    int res = quat1 + quat2;
    if(res == 3) return 3;
    // 1(i) + 2(j) == 3(k)
    if(res == 5) return 1;
    // 2(j) + 3(k) == 5(i)
    if(res == 4) return 2;
    // 3(k) + 1(i) == 4(j)
}

int convert(char quatChar) {
    switch(quatChar) {
        case '1' : return 0;
        // '1' is binded to 0.
        case 'i' : return 1;
        // 'i' is binded to 1.
        case 'j' : return 2;
        // 'j' is binded to 2.
        case 'k' : return 3;
        // 'k' is binded to 3.
    }
}

int pow(int quaternion, ull exponent) {
    int mod = exponent % 4;
    if(quaternion == convert('1')) {
    // Exponents of 1 will always give as a result 1.
        return quaternion;
    }
    if(quaternion == neg(convert('1'))) {
    // Exponents of -1 alternate just by 2.
        if(exponent % 2 == 0) {
        // Even exponents will make -1 positive.
            return neg(quaternion);
        }
        else {
        // Odd exponents will keep -1 negative.
            return quaternion;
        }
    }
    // Whereas exponents of quaternions alternate by 4.
    if(mod == 1) {
        return quaternion;
    }
    if(mod == 2) {
        return neg(convert('1'));
    }
    if(mod == 3) {
        return neg(quaternion);
    }
    if(mod == 0) {
        return convert('1');
    }
}

bool validateQuaternion(string quat, ull repeats) {
    int lookFor = convert('i');
    // Initially we'll look for an i.
    int acum    = convert('1');
    // The base multiplier will always be 1.
    while(lookFor && repeats--) {
    // While we have repetitions left...
        for(ull z = 0; lookFor && z < quat.length(); z++) {
        // ... Iterate repeatedly over the same string, keeping the results of
        // the previous iteration (in the 'acum' variable).
            int value = convert(quat[z]);
            // Convert the quaternion symbol at the current position to our in-
            // ternal integer representation of such numbers.
            acum = mult(acum, value);
            // Keep multiplying the accumulated multiplied quaternion symbols
            // and the incoming quaternion symbols of the string.
            if(acum == lookFor && lookFor == convert('i')) {
            // If we've finally reduced an 'i'...
                lookFor = convert('j');
                // Start looking to reduce a 'j'.
                acum   = convert('1');
                // Reset the accumulator variable.
                continue;
            }
            if(acum == lookFor && lookFor == convert('j')) {
            // If we've finally reduced a 'j'... (lookFor can only be 'j'
            // after having first found an 'i')...
                lookFor = convert('k');
                // Start looking to reduce a 'k' (with ALL the text rem-
                // aining in all the string repetitions).
                acum   = convert('1');
                // Reset the accumulator variable.
            }
            if(lookFor == convert('k') && z + 1 == quat.length()) {
            // Now, we'll only accumulate symbol multiplications for the
            // remainder of the string not used by the accumulation of 'j',
            // since from there on there will only be multiplications of the
            // whole string over and over again, and we can find the result
            // of that with exponentiation. After we've finally exhausted
            // the string, reset the lookFor variable to exit all loops.
                lookFor = 0;
            }
        }
    }
    // It means it exited all the iterations and it isn't even looking for a 'k',
    // so it either didn't find the 'j', or even the 'i'.
    if(lookFor != 0) {
        return false;
    }
    int reducedString = convert('1');
    for(ull z = 0; z < quat.length(); z++) {
    // Lets find the total reduction of an independent string.
        int value = convert(quat[z]);
        reducedString = mult(reducedString, value);
    }
    reducedString = pow(reducedString, repeats);
    // Lets exponentiate the remaining whole repetitions of the string.
    acum = mult(acum, reducedString);
    // Now lets see if the reduction of the tail-end of the last accumulated
    // string, times the exponentiation of the whole string to the amount of
    // all remaining iterations (so we don't have to actually iterate them)
    // equals 'k' (because its expected that the 'k' takes all the symbols
    // that are left in all the expected repetitions).
    return (acum == convert('k'));
}

int main() {
    int T;
    scanf("%d", &T);
    // Read the amount of test cases.
    for(int z = 0; z < T; z++){
        string quaternion;
        // The string full of quaternion symbols..
        ull chars, repeats;
        // The amount of characters in the string, and the expected repetitions
        // of it (but we'll not concatenate it, instead, iterate over the same
        // string while keeping the results of the previous one over and over!)
        cin >> chars >> repeats;
        cin >> quaternion;
        bool result = validateQuaternion(quaternion, repeats);
        printf("Case #%d: %s", z + 1, (result)? "YES" : "NO");
        if(z + 1 < T){
            puts("");
        }
    }
}