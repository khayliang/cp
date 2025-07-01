#include <iostream>
#include <string>
#include <cstdlib>
#include <set>
#include <vector>

using namespace std;

int main() {
    cout << "1\n";
    int n = (rand() % 10000) + 1;
    int m = (rand() % 10000) + 1;
    cout << n << " " 
    << m << " " 
    << (rand() % n) + 1<< " " 
    << (rand() % m) + 1<< "\n";
}