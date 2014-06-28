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

char board[8][8];
int caseNumber;
// To count the amount of cases given and solutions outputted

bool readBoard() {
// This will read a board, line by line, 8 rows and 8 columns
    string line;
    for(int i = 0; i < 8; i++) {
        cin >> line;
        for(int j = 0; j < 8; j++) {
            board[i][j] = line[j];
        }
    }
    return true;
}

bool isEmpty() {
// This will check whether a given board is empty, which will mark the end of
// the program input, as declared in the problem statement. A '.' represents
// an empty square in the program representation of a chess board.
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if(board[i][j] != '.') {
                return false;
            }
        }
    }
    return true;
}

bool validSquare(int y, int x) {
// For checking whether a square we want to move into is within the bounds
    return (0 <= y && y < 8) && (0 <= x && x < 8);
}

bool pawnAttacksKing(int y, int x, string type) {
// Pawns can only attack to the diagonal in front of them, so in this case the
// type of the piece matters. As white pieces are in the bottom, and the black
// pieces are in the top, then with the type we determine the attack direction
//    . . . . .
//    . W . W .  For a total of 4 possible moves (given that all of them does
//    . . O . .  not exceed the board's boundaries) but we'll check for every
//    . b . b .  ideally available move and then check if its inside the board.
//    . . . . .  Also the possible moves are limited depending on piece color.
//
    int possibleMoves[4][2] = {
        // FOR BLACK PIECE ONLY
        { 1,  1}, // Lower right diagonal
        { 1, -1}, // Lower left diagonal 
        // FOR WHITE PIECE ONLY
        {-1, -1}, // Upper left diagonal
        {-1,  1}  // Upper right diagonal
    };
    for(int k = 0; k < 4; k++) {
    // For all 4 possible moves, which are really 2 depending on the piece type
        if(type == "white" && k < 2) {
            continue;
        }
        if(type == "black" && k >= 2) {
            continue;
        }
        int newY = y + possibleMoves[k][0];
        int newX = x + possibleMoves[k][1];
        if(validSquare(newY, newX)) {
            char targetPiece = board[newY][newX];
            if(targetPiece == 'K' && type == "black") {
                return true;
            }
            if(targetPiece == 'k' && type == "white") {
                return true;
            }
        }
    }
    return false;
}

bool knightAttacksKing(int y, int x, string type) {
// Knights can attack in L movements and also are the only pieces that can jump
// over any obstacle pieces. Direction of movement is also unrestricted. These
// are the possible moves for a given Knight piece:
//
//    . 1 . 2 .
//    8 . . . 3  For a total of 8 possible moves (given that all of them does
//    . . O . .  not exceed the board's boundaries) but we'll check for every
//    7 . . . 4  ideally available move and then check if its inside the board.
//    . 6 . 5 .
//
    int possibleMoves[8][2] = {
    // These are the movements as marked in the above graphic
        {-2, -1}, // Movement 1
        {-2,  1}, // Movement 2
        {-1,  2}, // Movement 3
        { 1,  2}, // Movement 4
        { 2,  1}, // Movement 5
        { 2, -1}, // Movement 6
        { 1, -2}, // Movement 7
        {-1, -2}  // Movement 8
    };
    for(int k = 0; k < 8; k++) {
    // For all 8 possible moves
        int newY = y + possibleMoves[k][0];
        int newX = x + possibleMoves[k][1];
        if(validSquare(newY, newX)) {
            char targetPiece = board[newY][newX];
            if(targetPiece == 'K' && type == "black") {
                return true;
            }
            if(targetPiece == 'k' && type == "white") {
                return true;
            }
        }
    }
    return false;
}

bool bishopAttacksKing(int y, int x, string type) {
// Bishops attack diagonally, we'll assume that it can move 8 in every diagonal
// (its limit if it were in a corner) and simply stop processing that diagonal
// if it exceeds the board's bounds or if it finds an obstacle. These are the 
// possible moves for a given Bishop piece:
//
//    X . . . X
//    . X . X .  For a total of 4 possible diagonals (given that all of them
//    . . O . .  does not exceed the board's boundaries or meets an obstacle
//    . X . X .  piece) but we'll check for every ideally available move and
//    X . . . X  then check if its inside the board or doesn't have obstacles.
//
    int possibleDirections[4][2] = {
        { 1,  1}, // Lower-Right
        { 1, -1}, // Lower-Left
        {-1, -1}, // Upper-Left
        {-1,  1}  // Upper-Right
    };
    for(int k = 0; k < 4; k++) {
    // For all 4 possible directions
        for(int l = 1; l < 8; l++) {
        // For all max posible 8 moves in that direction
            int newY = y + (possibleDirections[k][0] * l);
            int newX = x + (possibleDirections[k][1] * l);
            if(!validSquare(newY, newX)) {
            // The bounds were exceeded in this direction, so stop checking the
            // other moves that go alongside this direction.
                break;
            }
            char targetPiece = board[newY][newX];
            if(targetPiece != '.'){
            // If target piece/place wasn't an empty space
                if(targetPiece == 'K' && type == "black") {
                    return true;
                }
                if(targetPiece == 'k' && type == "white") {
                    return true;
                }
                break;
                // If it wasn't an empty space and it wasn't a King then it was
                // a different kind of piece, which is an obstacle and will pre
                // vent any further moving in that direction.
            }
        }
    }
    return false;
}

bool rookAttacksKing(int y, int x, string type) {
// Rooks attack in hor/vert axis dirs, we'll assume that it can move 8 in every
// axis (its limit if it were in a board's side) and simply stop processing the
// axis if it exceeds the board's bounds or if it finds an obstacle. These are
// the possible moves for a given Rook piece:
//
//    . . X . .
//    . . X . .  For a total of 4 possible axis dirs (given that all of them
//    X X O X X  does not exceed the board's boundaries or meets an obstacle
//    . . X . .  piece) but we'll check for every ideally available move and
//    . . X . .  then check if its inside the board or doesn't have obstacles.
//
    int possibleDirections[4][2] = {
        { 0,  1}, // Rightwards
        { 0, -1}, // Leftwards
        {-1,  0}, // Upwards
        { 1,  0}  // Downwards
    };
    for(int k = 0; k < 4; k++) {
    // For all 4 possible directions
        for(int l = 1; l < 8; l++) {
        // For all max posible 8 moves in that direction
            int newY = y + (possibleDirections[k][0] * l);
            int newX = x + (possibleDirections[k][1] * l);
            if(!validSquare(newY, newX)) {
            // The bounds were exceeded in this direction, so stop checking the
            // other moves that go alongside this direction
                break;
            }
            char targetPiece = board[newY][newX];
            if(targetPiece != '.'){
            // If target piece/place wasn't an empty space
                if(targetPiece == 'K' && type == "black") {
                    return true;
                }
                if(targetPiece == 'k' && type == "white") {
                    return true;
                }
                break;
                // If it wasn't an empty space and it wasn't a King then it was
                // a different kind of piece, which is an obstacle and will pre
                // vent any further moving in that direction.
            }
        }
    }
    return false;
}

bool queenAttacksKing(int y, int x, string type) {
// Queens attack in every direction like a mix between Rooks and Bishops, we'll
// assume it can move 8 in every direction (its limit if it were in a side or a
// corner of the board) and simply stop processing that direction if it exceeds
// the board's bounds or if it finds an obstacle. These are the possible moves
// for a given Queen piece:
//
//    X . X . X
//    . X X X .  For a total of 8 possible directions (given that all of them
//    X X O X X  does not exceed the board's boundaries or meets an obstacle
//    . X X X .  piece) but we'll check for every ideally available move and
//    X . X . X  then check if its inside the board or doesn't have obstacles.
//
    int possibleDirections[8][2] = {
        // THIS IS FROM THE BISHOP MOVESET
        { 1,  1}, // Lower-Right
        { 1, -1}, // Lower-Left
        {-1, -1}, // Upper-Left
        {-1,  1},  // Upper-Right
        // THIS IS FROM THE ROOK MOVESET
        { 0,  1}, // Rightwards
        { 0, -1}, // Leftwards
        {-1,  0}, // Upwards
        { 1,  0}  // Downwards
    };
    for(int k = 0; k < 8; k++) {
    // For all 8 possible directions
        for(int l = 1; l < 8; l++) {
        // For all max posible 8 moves in that direction
            int newY = y + (possibleDirections[k][0] * l);
            int newX = x + (possibleDirections[k][1] * l);
            if(!validSquare(newY, newX)) {
            // The bounds were exceeded in this direction, so stop checking the
            // other moves that go alongside this direction
                break;
            }
            char targetPiece = board[newY][newX];
            if(targetPiece != '.'){
            // If target piece/place wasn't an empty space
                if(targetPiece == 'K' && type == "black") {
                    return true;
                }
                if(targetPiece == 'k' && type == "white") {
                    return true;
                }
                break;
                // If it wasn't an empty space and it wasn't a King then it was
                // a different kind of piece, which is an obstacle and will pre
                // vent any further moving in that direction.
            }
        }
    }
    return false;
}

bool checkIfAttacksKing(int y, int x, char piece, string type) {
    bool attacksKing = false;
    switch(piece) {
    case 'p': {
        attacksKing = pawnAttacksKing(y, x, type);
        break;
    }
    case 'n': {
        attacksKing = knightAttacksKing(y, x, type);
        break;
    }
    case 'b': {
        attacksKing = bishopAttacksKing(y, x, type);
        break;
    }
    case 'r': {
        attacksKing = rookAttacksKing(y, x, type);
        break;
    }
    case 'q': {
        attacksKing = queenAttacksKing(y, x, type);
        break;
    }
    case 'k': {
        // No King can attack another King since this would put it immediately
        // next to that other King and that would leave the first King also in
        // a check position and this is invalid. CHESS RULES.
        break;
    }
    default: {
        break;
    }
    }
    return attacksKing;
}

int checkForCheck() {
// This will check whether there is one King (and which) in check or if there's
// no King in check. According to the Laws of Chess no two Kings can be both in
// check altogether.
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            char piece = board[i][j];
            string type;
            if('a' <= piece && piece <= 'z') {
            // If the piece has lowercase letter, it is a black piece    
                type = "black";
            }
            if('A' <= piece && piece <= 'Z') {
            // If the piece has uppercase letter, it is a white piece
                type = "white";
                piece += ('a' - 'A');
                // In ascii this converts from uppercase to lowercase. We con-
                // vert to lowercase to have a general piece movement algorithm
                // and then instead of checking the letter's case we check the
                // type which we have got here and its easier to understand.
            }
            if(piece == '.') {
            // No piece was really here, it was an empty board square
                continue;
            }
            // Now we have to check for the piece legal moves if one of the
            // pieces under attack is a King and which one is it.
            bool res = checkIfAttacksKing(i, j, piece, type);
            if(res) {
                if(type == "white") {
                // If a King was in check and the attacker was white, -1
                    return -1;
                }
                if(type == "black") {
                // If a King was in check and the attacker was black,  1
                    return 1;
                }
            }
        }
    }
    return 0;
    // If no King was in check, then the returned value is 0
}

int main() {
// This program will check whether if the King in a given chess board is under
// attack or its in 'check'. White pieces will have uppercase letters, and the
// Black pieces will have lowercase letters. White side will always be on the
// bottom of the board while the Black side will always be on the top of it.
//
// Pawn   (P/p): can only move forward, or attack one square diagonally forward
// Knight (N/n): Has an L-shaped movement, only piece that can jump over others
// Bishop (B/b): Can move in diagonal in any direction any amount of squares
// Rook   (R/r): Can move vertically/horizontally in any direction any squares
// Queen  (Q/q): Can move like the Bishop and Rook, in any direction & squares
// King   (K/k): Can move in any direction but only one square at a time
    caseNumber = 0;
    while(readBoard()) {
        if(isEmpty()) {
        // Read until finding an empty board
            break;
        }
        int res = checkForCheck();
        if(res == -1) {
        // If a King was in check and the attacker was white, -1
            printf("Game #%d: black king is in check.\n", ++caseNumber);
        }
        if(res ==  0) {
        // If no King was in check, then the returned value is 0
            printf("Game #%d: no king is in check.\n",    ++caseNumber);
        }
        if(res ==  1) {
        // If a King was in check and the attacker was black,  1
            printf("Game #%d: white king is in check.\n", ++caseNumber);
        }
    }
}