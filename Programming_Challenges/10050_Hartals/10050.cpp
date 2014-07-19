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
	int t;
	// The number of test cases
	int n;
	// The number of days evaluated, it always starts on a Sunday
	int p;
	// The number of political parties
	cin >> t;
	while(t--) {
		cin >> n >> p;
		set<int> daysLost;
		// We'll use a set since this data structure won't allow for repeated
		// values. Its useful because with only a hartal, no matter from which
		// political party is it, it is already a lost day for everyone. Many
		// hartals coming from several parties the same day has the same effect
		// on the economy so it only matters to know if there is at least one.
		int hartalParam;
		for(int k = 0; k < p; k++) {
			cin >> hartalParam;
			for(int day = hartalParam; day <= n; day += hartalParam) {
				if(day % 7 != 0 && (day + 1) % 7 != 0) {
				// This checks that the day isn't a friday or saturday, because
				// there are no hartals on these days.
					daysLost.insert(day);
				}
			}
		}
		cout << daysLost.size() << endl;
		// The size of the set, since it doesn't allow for repeated occurrences
	}
}