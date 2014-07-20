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

struct Candidate {
    string name;
    // The name of the Candidate
    int votes;
    // The total votes this Candidate has
    bool running;
    // The candidate has not yet been eliminated.
};

struct Ballot {
    vector<int> candidateList;
    // A list containing the values of the Candidate ranking each ballot has.
    // These values are the Candidate's index which ranges from 1 to n.
};

int main() {
// This program will find the winner (or tied people) in a election done using
// a Ranked Voting System. 
    int n;
    // Number of test cases to be read;
    cin >> n;
    vector<Candidate> candidates;
    // A list containing the Candidates
    vector<Ballot> ballots;
    // A list containing the Ballots
    for(int z = 0; z < n; z++) {
        candidates.clear();
        ballots.clear();
        int candidateAmount;
        // The amount of Candidates in this elections
        int ballotAmount;
        // The amount of Ballots in this elections
        cin >> candidateAmount;
        string line;
        getline(cin, line);
        for(int k = 0; k < candidateAmount; k++) {
        // Create all the Candidates and read their names, and store them
            Candidate candidate;
            string name;
            // The name of the Cadidate
            getline(cin, name);
            candidate.name = name;
            candidate.votes = 0;
            candidate.running = true;
            // The index of the Candidate for finding it in the Candidate list
            candidates.push_back(candidate);
        }
        // After all the candidates have been read, read all the ballots, which
        // are 1000 at most, but we don't know how many, just read them until
        // the End of File, or until a blank line is read.
        while(getline(cin, line)) {
            if(line == "") {
            // Test cases are separated by an empty line in input file. Empty
            // line marks the end of Ballots read.
                break;
            }
            stringstream ss(line);
            Ballot ballot;
            for(int k = 0; k < candidateAmount; k++) {
            // Each line read contains the given ranking of Candidates indexes
            // so we proceed to decompose the line and start putting the numb-
            // ers separately into each Ballots own list of indexes (the rank).
                int candidateIndex;
                ss >> candidateIndex;
                ballot.candidateList.push_back(candidateIndex - 1);
            }
            ballots.push_back(ballot);
            // Then each Ballot is put into the total list of Ballots
        }
        ballotAmount = ballots.size();
        // Total registered Ballots
        candidateAmount = candidates.size();
        // Total registered Candidates
        int minVotes;
        int maxVotes;
        while(true) {
        // At each pass, the candidates with the least amount of votes will be
        // marked and reduced from the total of remaining Candidates. The win-
        // ner could be found early if it has > 50% of the votes or at the last
        // past given that there's a constant tie. If the group of people tied
        // at the bottom equals the amount of currently running Candidates, it
        // means they all tied.
            for(int k = 0; k < candidates.size(); k++) {
            // Reset the amount of votes of each Candidate. The votes are reco-
            // unted on every loop, and votes for an eliminated Candidate are
            // skipped and the next Candidate in each rank is checked then.
                candidates[k].votes = 0;
            }
            for(int k = 0; k < ballotAmount; k++) {
                // Now, proceed to count the votes
                Ballot ballot = ballots[k];
                // Get the current Ballot
                for(int l = 0; l < ballot.candidateList.size(); l++) {
                // Look for the highest, not yet eliminated Candidate in the ba
                // llots own rank to add votes for that Candidate.
                    int votedFor = ballot.candidateList[l];
                    if(candidates[votedFor].running) {
                        candidates[votedFor].votes++;
                        break;
                    }
                }
            }
            // Now that the votes for each Candidate have been counted, proceed
            // to look for the Candidate(s) with the least amount of votes and
            // mark them for removal.
            minVotes = 7777777;
            // Initialize the least amount of votes as a very large number
            maxVotes = -7777777;
            // Initialize the largest amount of votes as a very low number
            for(int k = 0; k < candidateAmount; k++) {
                Candidate candidate = candidates[k];
                if(!candidate.running) continue;
                minVotes = min(minVotes, candidate.votes);
                maxVotes = max(maxVotes, candidate.votes);
            }
            // If the max amount of votes exceeds the half of total votes, exit
            // the loop, also its only possible for this to happen for a single
            // Candidate, no 2 candidates can have > 50% votes.
            if(maxVotes > ballotAmount / 2) {
                break;
            }
            // The other condition for exiting the loop is that the minimum am-
            // ount of votes is also the max amount of votes, this means that
            // all the remainding running Candidates were drawn into a tie.
            if(minVotes == maxVotes) {
                break;
            }
            // If it reaches this point, it means that the Candidates with the
            // least amount of votes weren't all the possible remainding Candi-
            // dates, so proceed to mark them as not running anymore.
            for(int k = 0; k < candidates.size(); k++) {
                if(candidates[k].votes != minVotes) continue;
                candidates[k].running = false;
            }
        }
        for(int k = 0; k < candidates.size(); k++) {
        // In the end, the max amount of votes will represent the Winner or the
        // Candidates that were drawn into a tie, so we don't bother to know wh
        // ich of these two cases were what actually happened by just printing
        // all the Candidates that resulted with the most votes by the end.
            Candidate candidate = candidates[k];
            if(candidate.votes < maxVotes) continue;
            cout << candidate.name << endl;
        }
        if(z + 1 < n) {
        // Blank line between test cases!
            puts("");
        }
    }
}


