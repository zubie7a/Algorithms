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

vector< vector<int> > graph;

int main() {
    int N, M;
    int numCase = 1;
    while(cin >> N >> M) {
        if(!N && !M) {
        // Input terminates with 0 0
            break;
        }
        graph.clear();
        for(int k = 0; k <= N; k++) {
        // We'll have a graph, which will be a list of list of integers. Each
        // list will have the numbers each position goes to, including itself.
            vector<int> v;
            graph.push_back(v);
        }
        for(int k = 1; k <= M; k++) {
        // Read the graph, define bidirectional relations, as in, p1 and p2 are
        // a couple persons that belong to the same religion.
            int p1, p2;
            cin >> p1 >> p2;
            graph[p1].push_back(p2);
            graph[p2].push_back(p1);
        }
        for(int k = 0; k <= N; k++) {
        // Then, we'll mark each number as having its own religion
            graph[k].push_back(k);
        }
        int religions = 0;
        for(int i = 1; i <= N; i++) {
        // At each i (each person), the list of relations that person has is
        // also the list of persons belonging to its same religion. So, all the
        // persons found in this list will be 'cleared', since we don't have
        // to re-check for this same religion. A person that hasn't been cle-
        // ared this far belongs to a yet un-checked religion. If we didn't add
        // a person to its own list of religions, the size of that person's own
        // list would be 0, which would coincide with an already cleared person
        // and we want this person whom we don't know anything about to count 
        // as its own possible religion, for finding the upper bounding limit. 
            if(graph[i].size() > 0) {
                religions++;
            }
            else {
                continue;
            }
            queue<int> q;
            q.push(i);
            // We'll clear the lists of the persons related to the current per-
            // son, and also the lists of the persons related to those persons,
            // and so on, until all people from a same religion is cleared so
            // we don't check them anymore in the future.
            while(q.size() > 0) {
                int p1 = q.front();
                q.pop();
                for(int j = 0; j < graph[p1].size(); j++) {
                    int p2 = graph[p1][j];
                    q.push(p2);
                }
                graph[p1].clear();
            } 
        }
        cout << "Case " << numCase << ": " << religions << endl;
        numCase++;
    }
}