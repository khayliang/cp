#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <stack>
#include <cmath>
#include <queue>

using namespace std;

struct coords {
    double row;
    double col;
};

int main() {
    double t;
    cin >> t;
    while (t--) {
        double n;
        cin >> n;

        vector<vector<char>> map(2, vector<char> (n));

        string top, btm;
        cin >> top;
        cin >> btm;
        
        for (string::iterator i = top.begin(); i != top.end(); ++i) {
            map[0][distance(top.begin(), i)] = *i;
        }

        for (string::iterator i = btm.begin(); i != btm.end(); ++i) {
            map[1][distance(btm.begin(), i)] = *i;
        }

        vector<vector<bool>> dp(2, vector<bool> (n, false));
        queue<coords> q;

        coords init;
        init.row = 0;
        init.col = 0;  
        q.push(init);

        while(q.size() != 0) {
            coords curr = q.front();
            q.pop();
            double row, col;
            row = curr.row;
            col = curr.col;

            dp[row][col] = true;

            int parity = fmod(row + col, 2);

            if (parity == 0) {
                // left
                if (col > 0) {
                    if (!dp[row][col - 1]) {
                        dp[row][col - 1] = true;
                        coords c;
                        c.row = row;
                        c.col = col - 1;  
                        q.push(c);
                    }
                }
                // right
                if (col < n - 1) {
                    if (!dp[row][col + 1]) {
                        dp[row][col + 1] = true;
                        coords c;
                        c.row = row;
                        c.col = col + 1;
                        q.push(c);
                    }
                }

                // top
                if (row == 1) {
                    if (!dp[0][col]) {
                        dp[0][col] = true;
                        coords c;
                        c.row = 0;
                        c.col = col;
                        q.push(c);
                    }
                }
                // bot
                if (row == 0) {
                    if (!dp[1][col]) {
                        dp[1][col] = true;
                        coords c;
                        c.row = 1;
                        c.col = col;
                        q.push(c);
                    }
                }
            } else {
                char ch = map[row][col];
                if (ch == '>') {
                    dp[row][col + 1] = true;
                    coords c;
                    c.row = row;
                    c.col = col + 1;
                    q.push(c);
                } else {
                    dp[row][col - 1] = true;
                    coords c;
                    c.row = row;
                    c.col = col - 1;
                    q.push(c);
                }
            }
        }

        if (dp[1][n - 1]) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}