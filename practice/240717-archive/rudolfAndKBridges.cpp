#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <limits.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, M, K, D;
        cin >> N >> M >> K >> D;

        vector<int> costs(N);

        for (int i = 0; i != N; ++i) {
            multiset<int> mst = { 1 };
            queue<int> vals;
            vals.push(1);
            int x;
            cin >> x;
            for (int j = 1; j != M; ++j) {
                int depth, cost;
                cin >> depth;
                cost = *mst.begin() + depth + 1;
                mst.insert(cost);
                vals.push(cost);
                if (j >= D + 1) {
                    mst.erase(vals.front());
                    vals.pop();
                }
            }
            costs[i] = vals.back();
        }

        int mn = INT_MAX;
        int curr = 0;
        for (int i = 0; i != N; ++i) {
            curr += costs[i];
            if (i >= K) {
                curr -= costs[i - K];
            }
            mn = min(curr, mn);
        }
        cout <<endl << "result: "<< mn << endl;
    }
    return 0;
}