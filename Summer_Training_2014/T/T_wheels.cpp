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

#define MAXN 10005

using namespace std;

vector <int> graph[MAXN];
bool forbidden[MAXN];
int dist[MAXN];

void bfs(int start) {
    for(int k = 0; k < MAXN; k++) {
        dist[k] = -1;
    }
    queue <int> q;
    q.push(start);
    dist[start] = 0;
    // Distance to itself is 0
    if(forbidden[start] == true) {
        dist[start] = -1;
        return;
    }
    while(q.size() > 0) {
        int cur = q.front();
        q.pop();
        for(int k = 0; k < graph[cur].size(); k++) {
            int to = graph[cur][k];
            if(forbidden[to] == false && dist[to] == -1) {
            // If its not a forbidden node, and it hasn't been visited yet.
            // Also, since the distance between nodes is 1, and BFS is breadth
            // first, it will check every level completely, so the first occur-
            // ence of the target node will be also the closest one. If there
            // was an additional weight other than 1 (which in this case is the
            // cost for moving one number) there are other algorithms which ta-
            // ke into account the current cumulative weigth until that node,
            // and then only if the new cumulative weight is lower than the old
            // one, its taken into account as the shortest weight, otherwise no
                dist[to] = dist[cur] + 1;
                q.push(to);
            }
        }
    }
}

int findneighbor(int num, int pos, int dir) {
    int n[4];
    // Array representation of the current combination
    for(int k = 0; k < 4; k++) {
    // Decompose the number to store it into the array
        n[k] = num % 10;
        num /= 10;
    }
    n[pos] = (n[pos] + dir + 10) % 10;
    // Move the desired position in the given direction, add 10 so that subs-
    // tracting 1 from 9 doesn't give a negative number, and do modulo 10 so
    // that if adding 1 to 10 or 10 to anything gives a big number, get only
    // the number in its last decimal place
    for(int k = 3; k >= 0; k--) {
    // Convert the number back into the integer representarion
        num *= 10;
        num += n[k];
    }
    return num;
}

void initGraph() {
    for(int i = 0; i <= 9999; ++i) {
    // For every combination possible, put into the graph the neighbours that
    // the given combination has, which are found by moving to the right or the
    // left each of the decimal places of the original combination.
        for(int j = 0; j < 4; ++j) {
            graph[i].push_back(findneighbor(i, j,  1));
            graph[i].push_back(findneighbor(i, j, -1));
        }
    }
}

int readnum() {
    int ans = 0;
    int d;
    // Each of the digits of the number to be read
    for(int k = 0; k < 4; ++k) {
        cin >> d;
        ans = ans * 10 + d;
    }
    return ans;
}

int main(){
    int T;
    // Number of Test Cases to be read
    cin >> T;
    initGraph();
    for(int i = 0; i < T; i++) {
        int start = readnum();
        // Starting Combination
        int end = readnum();
        // Ending Combination
        int forbiddenNumber;
        // Number of Forbidden Combinations
        cin >> forbiddenNumber;
        for(int k = 0; k < MAXN; k++){
        // At the beginning, there were no forbidden combinations
            forbidden[k] = false;
        }
        for(int k = 0; k < forbiddenNumber; k++){
        // And then there were some
            int n = readnum();
            forbidden[n] = true;
        }
        bfs(start);
        // Do a BFS, this will allow us to calculate the distance from the beg-
        // inning to every other possible position. At the end, print the dist-
        // ance calculated to the ending position which the BFS will have found
        // as the lowest distance up to that point.
        cout << dist[end] << endl;
    }
}