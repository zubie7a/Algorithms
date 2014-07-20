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

map<string, int> nameToIndex;
// Convert from an authors name to an index between 0 and n - 1 (# of authors)
map<int, string> indexToName;
// Convert from an index between 0 and n - 1 (# of authors) to an authors name

vector< set<int> > authors;
// A graph for keeping track of authors relationships in papers. Lets use a set
// to avoid repeated relationships since there may be more than 1 paper where
// two authors may meet so this allows us to have unique pairings.
vector<bool> visited;
// A visited list for keeping track of already visited authors in graph traver-
// sal. We will do a BFS which will allow to know the shortest distance (if any
// at all) between two authors, specifically, between any author and Paul Erdos
// to find the so called 'Erdos Distance'.
set<string> authorsSet;
// A set containing all the possible authors, to know their unique occurrences
// and give them an index for easy identification and graph traversal. Be care-
// ful that maybe the program may be queried for an author that isn't in any
// paper, therefore it doesn't have an index to search in the graph, so first
// check in this set, and if it isn't here, skip doing the graph search.

string substring(string s, int l, int r) {
// substring of a string s, from index l (inclusive) to index r (exclusive)
    string res = "";
    while(l < r) {
        res += s[l];
        l++;
    }
    return res;
}

int bfs(int start, int end) {
    queue< pair<int, int> > q;
    // The queue will contain several pairs, each one has:
    // first: the current position
    // second: the cost until current position
    q.push(make_pair(start, 0));
    // BFS will start at the original given position, with 0 cost
    while(q.size()) {
        pair<int, int> now = q.front();
        q.pop();
        int actual = now.first;
        int weight = now.second;
        if(visited[actual]) {
        // This node has been previously reach, ignore it
            continue;
        }
        if(actual == end) {
        // If this node is the target node, return the weight up to this point.
        // The BFS ensures that this weight is the minimal distance possible 
        // between the start node and end node.
            return weight;
        }
        visited[actual] = true;
        set<int>::iterator it;
        for(it = authors[actual].begin(); it != authors[actual].end(); it++) {
            int next = *it;
            q.push(make_pair(next, weight + 1));
        }
    }
    return -1;
}

void resetVisited() {
// Every instance of the BFS requires the list of visited nodes to be resetted
    for(int k = 0; k < visited.size(); k++) {
        visited[k] = false;
    }
}

void initGraph() {
// Lets initialize the graph of authors with empty positions for every author
// available, and a visited list also as false, for easy graph traversal later.
    for(int k = 0; k < authorsSet.size(); k++) {
        set<int> coauthors;
        authors.push_back(coauthors);
        visited.push_back(false);
    }
}

string readName() {
// This function reads a single name, until a second comma is found, the line
// breaks, or a ':' is found. Whitespaces are ignored.
    char c;
    string name = "";
    bool firstComma = true;
    // A name has only one comma the second one means there is at least another
    // author ahead in the list of authors of the paper
    while((c = getchar()) != EOF) {
        // Read the character
        if(c != ' ') {
        // White spaces are ignored
            if(c == ',') {
                // If a comma is found
                if(firstComma) {
                // If its the first, add it to the name and then mark that it
                // was found so the second one isn't added
                    name += ", ";
                    firstComma = false;
                }
                else {
                // If its the second, it means the name ends here
                    return name;
                }
            }
            else {
            // If its not a comma
                if(c == ':') {
                // If its a colon add it to the name, it will tell the external
                // routine that this is the last name, there won't be any more.
                    name += c;
                    return name;
                }
                else if(c == '\n'){
                // This is useful when reading just one name in a line, it will
                // end with the \n character, or line break.
                    return name;
                }
                else {
                // If it isn't a space, nor a :, nor a \n, nor a comma, add it.
                    name += c;
                }
            }
        }
    }
}

vector<string> readNames() {
// This will read a list of names in a given paper, terminating when a name co-
// mes up with a ':' at the end, marking the end of the authors and the begin-
// ning of the paper's title. Remove that ':' and store all names in a list.
    vector<string> res;
    while(true) {
        string name = readName();
        if(name[name.length() - 1] == ':') {
        // If this is the last name down the road
            name = substring(name, 0, name.length() - 1);
            res.push_back(name);
            break;
        }
        res.push_back(name);
    }
    while('\n' != getchar());
    // After the names have been read, lets read characters without storing
    // them until reaching the end of the line, since all other characters are
    // part of the paper's name, in which we aren't interested at all for this.
    return res;
}

int main() {
    int s;
    // The number of scenarios
    int p, n;
    // p: the number of papers
    // n: the number of authors to query for their Erdos Number
    cin >> s;
    for(int z = 0; z < s; z++) {
        authors.clear();
        visited.clear();
        authorsSet.clear();
        cin >> p >> n;
        vector< vector<string> > allPapers;
        // A list of the lists of authors contained in each paper, this is like
        // a graph in string form, which will be converted into a graph in num-
        // erical form for easy and fast traversal.
        getchar();
        for(int k = 0; k < p; k++) {
            // Each read line will be a paper, first with the authors then the
            // paper's title, which will really be irrelevant for this program.
            vector<string> paperAuthors = readNames();
            for(int l = 0; l < paperAuthors.size(); l++) {
                string name = paperAuthors[l];
                authorsSet.insert(name);
            }
            allPapers.push_back(paperAuthors);
        }
        // Now that we have the list of authors in every paper, and a set that
        // contains the unique occurrences, lets iterate over the set to assign
        // each author an iterator so its easy to make a graph with them.
        set<string>::iterator it;
        int index = 0;
        for(it = authorsSet.begin(); it != authorsSet.end(); it++) {
        // Starting from 0, lets assign every unique author its own number, and
        // also keep a record of this in two maps, one that lets retrieve the
        // author's name from the number, and other that lets retrieve the num-
        // ber by using the author's name, helpful for making a graph using on-
        // ly numbers as indices and then getting the names back again
            string name = *it;
            nameToIndex[name] = index;
            indexToName[index] = name;
            index++;
        }
        initGraph();
         for(int i = 0; i < allPapers.size(); i++) {
         // After this, the graph using only indices will be completed
            vector<string> paperAuthors = allPapers[i];
            for(int j = 0; j < paperAuthors.size() - 1; j++) {
                string name1 = paperAuthors[j];
                int index1 = nameToIndex[name1];
                for(int k = j + 1; k < paperAuthors.size(); k++) {
                    string name2 = paperAuthors[k];
                    int index2 = nameToIndex[name2];
                    authors[index1].insert(index2);
                    authors[index2].insert(index1);
                }
            }
        }
        // Now, proceed to read a list of authors to inquire for their Erdos
        // Distance, and then do a BFS to see what is their shortest distance
        // to Paul Erdos (Erdos, P.) if any (infinity in case of none found).
        cout << "Scenario " << z + 1 << endl;
        for(int k = 0; k < n; k++) {
            resetVisited();
            string completeName = readName();
            int res;
            if(authorsSet.find(completeName) != authorsSet.end()) {
            // This is VERY important. Since the idea of making a graph invol-
            // ves giving an index to all the authors, present in the papers,
            // it may be possible that afterwards, there's a query for an au-
            // thor's Erdos Number and that author isn't in any of the availa-
            // ble paper, which would result in a nasty error since that aut-
            // hor isn't available in the map, possibly returning a bogus in-
            // dex. If the author isn't among the authors we know to be pres-
            // ent in the previously read papers, immediately print that its
            // Erdos Distance is infinity.
                int start = nameToIndex[completeName];
                int end = nameToIndex["Erdos, P."];
                res = bfs(start, end);
            }
            else {
            // The queried author isn't even in any of the given papers so the
            // immediate response is that it has infinity as its Erdos Distance
                res = -1;
            }
            if(res == -1) {
                cout << completeName << " infinity" << endl;
            }
            else {
                cout << completeName << " " << res << endl;
            }
        }
    }
}