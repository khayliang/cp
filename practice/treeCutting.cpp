#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <stack>
#include <cmath>
#include <queue>

using namespace std;

void compute_weights(vector<vector<int>>& tree, vector<int>& weights, int node) {
    if (tree[node].size() == 0) {
        weights[node] = 1;
        return;
    }

    weights[node] = 1;
    for (int i : tree[node]) {
        compute_weights(tree, weights, i);
        weights[node] += weights[i];
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> N >> K;

        vector<vector<int>> tree(N, vector<int>());

        vector<int> parents(N);
        parents[0] = -1;

        for (int i = 0; i != N - 1; ++i) {
            int v, u;
            cin >> v >> u;
            tree[v - 1].push_back(u - 1);
            parents[u - 1] = v - 1;
        }
        vector<int> weights(N, 0);
        compute_weights(tree, weights, 0);

        int mid = *lower_bound(weights.begin(), weights.end(), N / 2);

        
    }
    return 0;
}