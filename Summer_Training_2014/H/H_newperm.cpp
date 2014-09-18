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

string integerToString(int k);
string substring(string s, int l, int r);
string largeSub(string n1, string n2);
string largeSum(string n1, string n2);
string largeMul(string n1, string n2);
int largeCmp(string n1, string n2);

string integerToString(int k){
    stringstream ss;
    ss << k;
    return ss.str();
}

string substring(string s, int l, int r) {
// For finding the substring of a given string between l (inclusive) and r
    string res = "";
    for(int k = l; k < r; k++) {
        res += s[k];
    }
    return res;
}

int largeCmp(string n1, string n2){
// Determines if the first given number (stored in a string) is bigger, smaller
// or equal when compared agaisnt the second number (also stored in a string).
// -1: n1 <  n2
//  0: n1 == n2
// +1: n1  > n2
    if(n1[0] == '-' && n2[0] != '-') {
    // if n1 is negative and n2 is not, n1 is lower than n2
        return -1;
    }
    if(n2[0] == '-' && n1[0] != '-') {
    // if n2 is negative and n1 is not, n1 is bigger than n2
        return 1;
    }
    if(n1[0] == '-' && n2[0] == '-') {
    // If both n1 and n2 are negative, strip them of their signs
    // Then compare them in reverse, and the invert the result too
    // since comparing -100 and -121 is like comparing 100 and 121
    // but reverse since bigger magnitudes of negative are lower.
        n1 = substring(n1, 1, n1.length());
        n2 = substring(n2, 1, n2.length());
        return -1 * largeCmp(n2, n1);
    }
    if(n1.length() < n2.length()) {
    // n1 is lower in length, must be also lower in value/orders of 10
        return -1;
    }
    if(n1.length() > n2.length()) {
    // n1 is bigger in length, must be also bigger in value/orders of 10
        return 1;
    }
    if(n1 == n2) {
    // Both are equal in contents, also equal in value then
        return 0;
    }
    // If it has reached this point, it means both are equal in length, but not
    // in their contents. To make things easier, put both in a list, sort the 
    // list, and check if n1 is the first element.
    vector<string> nums;
    nums.push_back(n1);
    nums.push_back(n2);
    sort(nums.begin(), nums.end());
    return ((n1 == nums[0])? -1 : 1);
}

string largeSub(string n1, string n2) {
// To substract VERY LARGE NUMBERS using strings
    if(n1[0] == '-' && n2[0] != '-') {
    // If the first number is negative and the second isn't, then simply add
    // both numbers and return that result as negative. 
    // (-a) - (b) = -1 * ((a) + (b))
        n1 = substring(n1, 1, n1.length());
        // strip n1 of the sign
        return '-' + largeSum(n1, n2);
    }
    if(n1[0] != '-' && n2[0] == '-') {
    // If the first number isn't negative and the second is, then simply add
    // both numbers ignoring the sign on the second one.
    // (a) - (-b) = (a) + (b)
        n2 = substring(n2, 1, n2.length());
        // strip n2 of the sign
        return largeSum(n1, n2);
    }
    if(n1[0] == '-' && n2[0] == '-') {
    // If both are negative, subtract a from b ignoring the old signs.
    // (-a) - (-b) = (-a) + (b) = (b) - (a)
        n1 = substring(n1, 1, n1.length());
        // strip n1 of the sign
        n2 = substring(n2, 1, n2.length());
        // strip n2 of the sign
        return largeSub(n2, n1);
    }
    // If both are positive it survives up to this point, so proceed to work
    if(largeCmp(n1, n2) == -1) {
    // If n1 is lower than n2, then swap them so we can assume from now on that
    // n1 > n2. If it enters this IF, it means that the result will be negative
    // since to reach this point both n1 and n2 must've been positive, and when
    // you substract n2 from n1, where n2 > n1, the result must be negative.
        return '-' + largeSub(n2, n1);
    }
    // When substracting, we must ideally always have the biggest number first,
    // and the lower second. If there was a swap, it means that originally the
    // first was lower than the second, and this ensures a negative result.
    // a - b = -1 * (b - a)  and if a < b, then b - a will always be positive.
    vector<int> d1;
    // digits of the n1 numerical string, but in separate integer form
    vector<int> d2;
    // digits of the n2 numerical string, but in separate integer form
    for(int k = 0; k < n1.length(); k++) {
        d1.push_back(n1[k] - '0');
    }
    for(int k = 0; k < n2.length(); k++) {
        d2.push_back(n2[k] - '0');
    }
    for(int k = 0; k < d2.size(); k++) {
        int curN1 = d1[d1.size() - 1 - k];
        // Current value at the decimal place of n1 we are inspecting
        int curN2 = d2[d2.size() - 1 - k];
        // Current value at the decimal place of n2 we are inspecting
        int res = curN1 - curN2;
        d1[d1.size() - 1 - k] = res;
    }
    string result = "";
    for(int k = d1.size() - 1; k >= 0; k--) {
        if(d1[k] < 0) {
            d1[k] = 10 + d1[k];
            d1[k - 1]--;
        }
        result = (char)(d1[k] + '0') + result;
    }
    int iter = 0;
    while(d1[iter] == 0 && iter < d1.size()) {
        iter++;
    }
    if(iter == d1.size()) {
        return "0";
    }
    result = substring(result, iter, result.length());
    return result;
}

string largeSum(string n1, string n2) {
// To add VERY LARGE NUMBERS using strings
    if(n1[0] == '-' && n2[0] != '-') {
    // If the first number is negative and the second isn't, then simply
    // subs tract the first number from the second.
    // (-a) + (b) = (b) - (a)
        n1 = substring(n1, 1, n1.length());
        // strip n1 of the sign
        return largeSub(n2, n1);
    }
    if(n1[0] != '-' && n2[0] == '-') {
    // If the first number isn't negative and the second is, then simply
    // substract the second number from the first.
    // (a) + (-b) = (a) - (b)
        n2 = substring(n2, 1, n2.length());
        // strip n2 of the sign
        return largeSub(n1, n2);
    }
    if(n1[0] == '-' && n2[0] == '-') {
    // If both are negative, ignore the signs and add as usual, and in the
    // end the negative symbol will be appended back into the result.
    // (-a) + (-b) = -1 * (a + b)
        n1 = substring(n1, 1, n1.length());
        // strip n1 of the sign
        n2 = substring(n2, 1, n2.length());
        // strip n2 of the sign
        return "-" + largeSum(n1, n2);
    }
    // If both are positive it survives up to this point, so proceed to work
    if(largeCmp(n1, n2) == -1) {
    // If n1 is lower than n2, then swap them so we can assume from now on that
    // n1 > n2. We want to assume from now on that the first number is bigger!!
        return largeSum(n2, n1);
    }
    vector<int> d1;
    // digits of the n1 numerical string, but in separate integer form
    vector<int> d2;
    // digits of the n2 numerical string, but in separate integer form
    for(int k = 0; k < n1.length(); k++) {
        d1.push_back(n1[k] - '0');
    }
    for(int k = 0; k < n2.length(); k++) {
        d2.push_back(n2[k] - '0');
    }
    for(int k = 0; k < d2.size(); k++) {
        int curN1 = d1[d1.size() - 1 - k];
        // Current value at the decimal place of n1 we are inspecting
        int curN2 = d2[d2.size() - 1 - k];
        // Current value at the decimal place of n2 we are inspecting
        int res = curN1 + curN2;
        d1[d1.size() - 1 - k] = res;
    }
    string result = "";
    for(int k = d1.size() - 1; k >= 0; k--) {
        if(d1[k] > 9) {
            d1[k] %= 10;
            if(k > 0) {
                d1[k - 1]++;
            }
            else {
                result += "1";
            }
        }
    }
    for(int k = 0; k < d1.size(); k++) {
        result += (char)(d1[k] + '0');
    }
    return result;
}

string largeMul(string n1, string n2) {
// To repeatedly add VERY LARGE NUMBERS using strings
    if(n1 == "0" || n2 == "0") {
    // If either number is 0, the immediate result is 0, this is to avoid is-
    // sues with the negative number, because -a * 0 would give -0 as result.
        return "0";
    }
    if(n1[0] == '-' && n2[0] != '-') {
    // If the first number is negative and the other not, result is negative
        n1 = substring(n1, 1, n1.length());
        return '-' + largeMul(n1, n2);
    }
    if(n1[0] != '-' && n2[0] == '-') {
    // If the second number is negative and the other not, result is negative
        n2 = substring(n2, 1, n2.length());
        return '-' + largeMul(n1, n2);
    }
    if(n1[0] == '-' && n2[0] == '-') {
    // If both the numbers are negative, the result is positive
        n1 = substring(n1, 1, n1.length());
        n2 = substring(n2, 1, n2.length());
        return largeMul(n1, n2);
    }
    if(largeCmp(n1, n2) == -1) {
    // So that we minimize the number of additions. Its way more expensive to
    // add up 2 by 2147483648 times that adding up 2147483658 by 2 times.
        largeMul(n2, n1);
    }
    string res = "0";
    for(int k = 0; ; k++) {
        string sk = integerToString(k);
        if(largeCmp(sk, n2) != -1) {
           break;
       }
        res = largeSum(res, n1);
    }
    return res;
}

//-- END OF THE SPECIAL FUNCTIONS DEFINED FOR OPERATIONS ON LARGE INTEGERS --//

string factorials[22];

void initFactorials() {
    // Precomputed list of factorial numbers. Since they are WAY TOO BIG,
    // I've preferred to calculate them using strings to add up or multiply
    // VERY LARGE NUMBERS.
    factorials[0] = "1";
    for(int k = 1; k < 22; k++) {
        string n1 = factorials[k - 1];
        string n2 = integerToString(k);
        factorials[k] = largeMul(n1, n2);
    }
}

string findPartLength(int stringLength) {
    // The dividing part length:
    // A string has s_l! permutations, where s_l is the length of the string.
    // When ordering these permutations lexicographically, one notices that
    // each every (s_l - 1)! steps, the first letter changes, and also in a
    // lexicographically increasing manner, so for the string "abcde", which
    // has length 5 and 5!->120 permutations, one notices that every (5-1)!
    // or 24 permutations, the first letter changes between:
    //
    //  0-23  -> a    We are interested in this number because when given a
    // 24-47  -> b    n-th permutation to find, it allows to know the first
    // 48-71  -> c    letter of that permutation, then substract the first
    // 72-95  -> d    possible occurrence of this letter from the desired
    // 96-119 -> e    amount of permutations, and then repeat with the rest
    //                of the string, and the remaining permutations.
    return factorials[stringLength - 1];
}

int findPartNumber(string partLength, string targetPerm) {
    // After finding the length of the parts that the set of permutations is
    // divided into (each part having a different leading letter, lexicogra-
    // phically increasing) now we want to know exactly in which part of the
    // set is the desired target permutation so we can know for certain what
    // the leading character is.
    for(int k = 0; ; k++) {
        string sk = integerToString(k + 1);
        string part = largeMul(partLength, sk);
        int res = largeCmp(part, targetPerm);
        if(res == 1) {
            return k;
        }
    }
}

int main() {
    int T;
    // Number of Test Cases to be read
    cin >> T;
    initFactorials();
    // Init all the factorials from 0 to 21
    string s;
    // String to permutate n times
    string n;
    // Holder of the target permutation. May be a REALLY LARGE NUMBER.
    while(T--) {
        cin >> s >> n;
        // Read the original string and the target permutation
        sort(s.begin(), s.end());
        // Sort the string so that all permutations found go lexicographically
        // increasing, which matters for finding the exact n-th permutation.
        vector<char> chars;
        for(int k = 0; k < s.length(); k++) {
        // Put the characters into a vector, makes it easier to go around del-
        // eting characters when we have put them into the resulting string.
            chars.push_back(s[k]);
        }
        string result = "";
        while(chars.size()) {
        // While there are still characters of the original string to place in
        // the Nth permutation that we want to find
            string partLength = findPartLength(chars.size());
            // The size of the subpermutation for every possible leading symbol
            int partNumber    = findPartNumber(partLength, n);
            // The part of the set of permutations where the target permutation
            // (in lexicographically increasing order) lies within! This will
            // also be the index of the leading character of the (sub)permuta-
            // tion in the original string, given that it was sorted.
            result += chars[partNumber % chars.size()];
            // Append this character to the resulting permutation, modulus size
            // because target permutation may cycle over the whole set.
            n = largeSub(n, largeMul(partLength, integerToString(partNumber)));
            // Substract from the target amount of permutations, the permuta-
            // tions that were consumed just to find the current leading symbol
            vector<char>::iterator position = chars.begin() + partNumber;
            chars.erase(position, position + 1);
            // Erase from the original string the symbol that was just placed
            // into the resulting permutation.
        }
        cout << result << endl;
    }
}

/*
    The logic is as follows:
    All the possible permutations of a string S are defined as all the possible
    ways to combine its symbols. Given that S_l is the length of the string,
    then the size of all possible permutations of S is (S_l)!. This is because
    At first, there are (S_l) possible elements to put at the lead. Then, there
    are (S_l - 1) possible elements to put at the second place. Then, there are
    (S_l - 2) possible elements to put at the third place. This goes all until
    the limit of positions is reached. This recursive amount of combinations
    defined as (S_l) * (S_l - 1) * (S_l - 2) * (S_l - 3) ... is (S_l)!

    For all the (S_l) possible characters that can lead in a permutation, there
    are (S_l - 1) characters remaining to be used and (S_l - 1)! ways to combi-
    ne them. Since we are asked to find P_N, which is, the Nth permutation in
    the set of all lexicographically ordered permutations of S, we can find
    some interesting properties:

    All the possible leading letters, occur every (S_l - 1)! permutations in
    the set. That is because if every leading letter can have (S_l - 1)! perm-
    utations of the substring following it, then when all those are exhausted
    is when a new leading symbol comes. The sum of the (S_l - 1)! permutations
    of all (S_l) possible leading symbols leads to (S_l) * (S_l - 1)! which is
    the (S_l)! total amount of permutations mentioned earlier. 

    Then, with the target Nth permutation, we can know which will be its lead-
    ing letter, checking every (S_l - 1)! steps until we reach the multiples
    (C), (C + 1) of (S_l - 1)! that tightly bound N, in such a way that:
    (C) * (S_l - 1)! <= N < (C + 1) * (S_l - 1)!
    The lower bound, is the lowest permutation that shares the leading symbol
    with the leading symbol of the Nth permutation. C will also be the index
    of this symbol in the original sorted string!

    Given that P_k is the k_th permutation in the set and (5 - 1)! is 24:
    0  <= k < 24   leading: 'a'
    24 <= k < 48   leading: 'b'
    48 <= k < 71   leading: 'c'
    71 <= k < 95   leading: 'd'
    96 <= k < 120  leading: 'e' then P_119 will have 'e' as the leading letter

    Now, remove 'e' from the originally sorted string, remove 96 (the lowest
    amount of permutations to find a permutation with 'e' as a leading letter)
    from 119 (this could be thought of permutations consumed to reach this) and
    then apply this same definition to the remaining original string to find
    the complete structure of the Nth targed permutation!
*/