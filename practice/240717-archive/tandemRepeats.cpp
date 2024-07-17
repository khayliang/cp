#include <iostream>
#include <vector>
#include <string>
#include <iterator>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        int mx = 0;
        for (string::iterator i = s.begin(); i != s.end(); ++i) {
            int dist = 0;
            int k = dist;
            bool finding = false;

            string::iterator cp = i;

            for (string::iterator j = next(i); j != s.end(); ++j) {
                if (*j == *cp && !finding) {
                    dist = distance(i, j);
                    k = dist;
                    finding = true;
                }
                if (finding) {
                    cout << k << endl;
                    if (*j != *cp) {
                        finding = false;
                        cp = i;
                    }
                    if (k == 0) {
                        mx = max(mx, dist);
                        finding = false;
                        cp = i;
                    }
                    ++cp;
                    --k;
                }
            }
        }
        cout << mx * 2;
    }
    return 0;
}