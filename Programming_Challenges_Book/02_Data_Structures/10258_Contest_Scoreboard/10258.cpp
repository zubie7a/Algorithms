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


struct Problem {
// Each problem has the amount of submissions, the time of the last submission
// and the accepted status. When its accepted, the time of the last submission
// will be added to the amount of previous submissions * 20min of penalty time.
    bool accepted;
    int submissions;
    int lastSubmissionTime;
};

struct Contestant {
// A Contestant will have a status regarding 9 problems, and a total time.
    Problem problems[10];
    bool submitted;
    int contestantIndex;
    int problemsSolved;
    int totalTime;
};

Contestant contestants[101];
vector<Contestant> finalRanking;

void initContestants() {
    for(int k = 0; k < 101; k++) {
        Contestant c;
        c.totalTime = 0;
        // Each contestant has an original time of 0
        c.problemsSolved = 0;
        // Each contestant has 0 problems solved at start
        c.contestantIndex = k;
        // The index of the contestant. Originally will be its position in the
        // array, but then as the array will be sorted, its better to remember
        // what its original position was.
        c.submitted = false;
        // Not all 100 possible contestants are participating, we'll know a te-
        // am with a certain number has participated if they've sent at least
        // a submission, no matter what kind is it.
        for(int l = 0; l < 10; l++) {
            Problem p;
            p.accepted = false;
            // Each problem hasn't originally been accepted
            p.submissions = 0;
            // It also has 0 submissions
            p.lastSubmissionTime = -1;
            // And has no last submission time
            c.problems[l] = p;
        }
        contestants[k] = c;
    }
}

void getTotalTimes() {
    for(int k = 0; k < 101; k++) {
        Contestant c = contestants[k];
        for(int l = 0; l < 10; l++) {
            Problem p = c.problems[l];
            if(!p.accepted) {
                continue;
            }
            c.totalTime += p.lastSubmissionTime + ((p.submissions - 1) * 20);
            // If the problem was accepted, add to the total running time of
            // the contestant the time of the last submission time, plus 20
            // minutes of penalty for every previous submission (total - 1).
            c.problemsSolved++;
        }
        if(!c.submitted) continue;
        finalRanking.push_back(c);
    }
}
bool sortByProblems(const Contestant &lhs, const Contestant &rhs) {
// We want the people with most problems solved to be at the beginning of
// the list, so reverse the comparisson operator, since the usual sort will
// assume < for sorting increasingly.
    return lhs.problemsSolved > rhs.problemsSolved;
}

bool sortByTime(const Contestant &lhs, const Contestant &rhs) {
// If there's a tie from the amount of problems solved, we want to do a sort
// by putting the ones with the least total running time at first
    return lhs.totalTime < rhs.totalTime;
}

void sortContestantsByProblemsSolved() {
// This will sort the whole list of contestants decreasingly by problems solved
    int start = 0;
    int end = finalRanking.size();
    sort(finalRanking.begin() + start, 
         finalRanking.begin() + end, 
         sortByProblems
    );
}

void sortContestantsByRunningTime() {
// This will sort the contestants increasingly by running time, but not the who
// le list, just the sublists of it that share the same amount of problems sol-
// ved, this as a way of breaking ties
    int start = 0;
    int end = 0;
    int problemsSolved = finalRanking[0].problemsSolved;
    // As an initial value, the problems that the first contestant in this list
    // solved. Since at this point its already sorted by problems solved, all
    // the following contestants will have the same amount of problems solved
    // upto a certain point. When we reach that point of a new contestant with
    // less problems solved, or no more contestants, we define this as the end
    // point of the sorting, sort the sublist, and create a new start point at
    // this place, until emcompassing again all the contestants with the new
    // amount of problems solved to be sorted by total running time.
    for(int k = 0; k < finalRanking.size(); k++) {
        Contestant c = finalRanking[k];
        if(c.problemsSolved == problemsSolved) {
            end++;
            continue;
        }
        sort(finalRanking.begin() + start,
             finalRanking.begin() + end,
             sortByTime
        );
        start = k;
        end = k + 1;
        problemsSolved = c.problemsSolved;
    }
    sort(finalRanking.begin() + start,
         finalRanking.begin() + end,
         sortByTime
    );
    // One more sort since it may have reached the end of the list and not done
    // the last sort, because there's no more elements to find with a new value
}

void sortContestants() {
// The rules are as follows:
// 1. Its better to have more problems solved
// 2. In case of a tie in problems solved, sort by time
// 3. In case of a sort by time, sort by contestant index.
    sortContestantsByProblemsSolved();
    sortContestantsByRunningTime();
    // Sorting by index isn't necessary because contestants were all originally
    // in numerical increasing order, so when doing a comparisson that evaluates
    // a tie, no changes will be made between their relative ordering and they
    // will keep their numerically increasing order
}

int main() {
// The problem consist of a ACM ICPC scoreboard. Every line of input has this
// format: C P T L
// C: Contestant Number
// P: Problem Index
// T: Time of Submission
// L: Type of Submission
// ... C: Correct
// ... I: Incorrect
// ... R: Request for Clarification
// ... U: Unjudged
// ... E: Erroneous Submission
// The last 3 types of submission have no effect on scoring. An user's score
// for a given problem is the time it took to send a correct submission, plus
// 20 minutes of penalty for every previous incorrect submission of that pro-
// blem. There's no penalty for problems not submitted, or for problems with
// incorrect submissions that never had a correct submission at the end. Then
// whats the scoreboard in the format C P T?
// C: Contestant Number
// P: Problems Solved
// T: Total Time (with Penalties)
    int n;
    // The number of test cases to be read
    cin >> n;
    getchar();
    // Get the linebreak that cin ignores after reading the test cases number
    string line;
    getline(cin, line);
    // Get the original empty line after test cases number and inputs
    for(int z = 0; z < n; z++) {
        finalRanking.clear();
        initContestants();
        while(getline(cin, line)) {
        // Read lines until EOF or...
            if(line == "" || line == " ") {
            // ..until a newline is read which marks the end of the test case
                break;
            }
            stringstream submission(line);
            int cNumber;
            // The number of the contestant
            int pIndex;
            // The index of the problem
            int sTime;
            // The time of submission
            string sType;
            // The type of submission
            submission >> cNumber >> pIndex >> sTime >> sType;
            Contestant c = contestants[cNumber];
            c.submitted = true;
            // Mark this contestant/team as having submitted anything. Having
            // submitted anything is important because it lets us know that the
            // contestant exists, so even if they don't have any accepted sub-
            // mission, they'll show up at the final scoreboard.
            if(sType == "R" || sType == "U" || sType == "E") {
            // We don't care about these kind of submissions for the scoreboard
                contestants[cNumber] = c;
                continue;
            }
            Problem p = c.problems[pIndex];
            if(!p.accepted) {
            // Submissions after the first accepted one won't have any effect
            // on the scoreboard, so leave that thing alone!
                p.lastSubmissionTime = sTime;
                // Renew the last submission time
                p.submissions++;
                // Increase the number of submissions for this problem
                if(sType == "C") {
                // If the problem was correct, change its status to accepted
                    p.accepted = true;
                }
            }
            c.problems[pIndex] = p;
            contestants[cNumber] = c;
        }
        // After this, all the scoreboard has been read, now lets get ready to
        // compute the total time for everyone!
        getTotalTimes();
        // Now that we have for every contestant their total running times and
        // amount of problems solved...
        sortContestants();
        // ... lets sort them using the explained sorting rules!
        for(int k = 0; k < finalRanking.size(); k++) {
        // Now, lets print the scoreboard!
            Contestant c = finalRanking[k];
            printf("%d %d %d\n", c.contestantIndex, 
                                 c.problemsSolved, 
                                 c.totalTime
            );
        }
        if(z + 1 < n) {
            puts("");
        }
    }
}