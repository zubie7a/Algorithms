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

struct Image {
    int n, m;
    // Dimensions of the image 'bitmap'.
    // n: the rows number
    // m: the cols number
    char bitmap[252][252];
    // Image bitmap. By default it has max dimensions available 250 x 250
    string filename;
    void clear() {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                bitmap[i][j] = '0';
            }
        }
    }
    void setPixel(int i, int j, char c) {
        bitmap[i - 1][j - 1] = c;
    }
};

Image img;
// The image to edit
vector<Image> imgs;
// Place to go storing all the previous images

void bfsFill(int x, int y, char c) {
    int dimx = img.m;
    int dimy = img.n;
    bool visited[dimx][dimy];
    for(int i = 0; i < dimy; i++) {
        for(int j = 0; j < dimx; j++) {
            visited[i][j] = false;
        }
    }
    char original = img.bitmap[x][y];
    // Store the color of the original starting pixel
    queue< pair<int, int> > q;
    q.push(make_pair(y, x));
    while(q.size()) {
        int py = q.front().first;
        int px = q.front().second;
        q.pop();
        if(py >= 0 && px >= 0 && py < dimy && px < dimx) {
        // If the new point we want to access is within boundaries
            if(img.bitmap[py][px] != original || visited[py][px]) {
            // If the point we're standing on did not share color with original
            // then ignore the point and proceed to check the next one. Ignore
            // it also if it was an already visited point. Endless cycles could
            // happen if we were tasked to do a fill in a zone that already has
            // the color we want to fill it with.
                continue;
            }
            img.bitmap[py][px] = c;
            visited[py][px] = true;
            // Change the color of the current pixel. If its here in the queue
            // it means it shared a color with the original pixel. Also mark it
            // as visited.
            q.push(make_pair(py + 1, px)); // Pixel below
            q.push(make_pair(py - 1, px)); // Pixel above
            q.push(make_pair(py, px - 1)); // Pixel to the left
            q.push(make_pair(py, px + 1)); // Pixel to the right
        }
    }
}

void writeResults() {
    for(int k = 0; k < imgs.size(); k++) {
        Image image = imgs[k];
        cout << image.filename << endl;
        for(int i = 0; i < image.n; i++) {
            for(int j = 0; j < image.m; j++) {
                cout << image.bitmap[i][j];
            }
            cout << endl;
        }
    }
}

int main(){
    string instruction;
    // Command to read from the input
    bool finish = false;
    // false while no terminating command has been given
    while(getline(cin, instruction)) {
        int x1, y1;
        int x2, y2;
        int  x,  y;
        char c;
        stringstream ss(instruction);
        char cmd;
        ss >> cmd;
        switch(cmd){
        case 'X': {
        // X: Terminate session
            writeResults();
            finish = true;
            break;
        }
        case 'I': {
        // I: Create new image
            int m, n;
            ss >> m >> n;
            img.m = m;
            img.n = n;
            img.clear();
            break;
        }
        case 'C': {
        // C: Clears the image
            img.clear();
            break;
        }
        case 'L': {
        // L: Colors a x, y pixel in a c color
            ss >> x >> y >> c;
            img.setPixel(y, x, c);
            break;
        }
        case 'V': {
        // H: Draw a vertical segment of c color from y1 to y2 at x horizontal
            ss >> x >> y1 >> y2 >> c;
            for(int k = y1; k <= y2; k++) {
                img.setPixel(k, x, c);
            }
            break;
        }
        case 'H': {
        // H: Draw a horizontal segment of c color from x1 to x2 at y vertical
            ss >> x1 >> x2 >> y >> c;
            for(int k = x1; k <= x2; k++) {
                img.setPixel(y, k, c);
            }
            break;
        }
        case 'K': {
        // K: Draw a filled rectangle of c color from x1,y1 to x2,y2
            ss >> x1 >> y1 >> x2 >> y2 >> c;
            for(int i = y1; i <= y2; i++) {
                for(int j = x1; j <= x2; j++) {
                    img.setPixel(i, j, c);
                }
            }
            break;
        }
        case 'F': {
        // F: Fills a region starting at a x,y pixel with a certain color, by
        // changing the color of all recursively neighboring pixels that are
        // the same color of the starting pixel
            ss >> x >> y >> c;
            bfsFill(x - 1, y - 1, c);
            break;
        }
        case 'S': {
        // S: save the file with a desired filename
            string name;
            ss >> name;
            img.filename = name;
            imgs.push_back(img);
            break;
        }
        default: {
            break;
        }
        }
        if(finish) {
            break;
        }
    }
}