#include <iostream>
#include <string>
#include <cstdlib>
#include <set>

using namespace std;

int main() {
    cout << "1\n";
    int n = 10;
    cout << n << "\n";
    for (int i = 0; i != n; ++i) {
        cout << -(rand() % 2) << " ";
    }
    cout << "\n";
    for (int i = 0; i != n; ++i) {
        int x = rand() % 10;
        int y = rand() % 10;
        cout << min(x, y) << " " << max(x, y) << "\n";
    }
}