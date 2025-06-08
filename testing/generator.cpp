#include <iostream>
#include <string>
#include <cstdlib>
#include <set>

using namespace std;

int main() {
    cout << "1\n";
    set<pair<int, int>> coords;
    for (int i = 0; i != 5; ++i) {
        coords.insert({rand() % 5 + 1, rand() % 5 + 1});
    }
    cout << coords.size() << "\n";
    for (const auto& coord : coords) {
        cout << coord.first << " " << coord.second << "\n";
    }
}