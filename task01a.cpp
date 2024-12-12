#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>

int main(int argc, char const *argv[]) {
    std::vector<uint64_t> a;
    std::vector<uint64_t> b;
    uint64_t v;
    while (std::cin >> v) {
        a.push_back(v);
        std::cin >> v;
        b.push_back(v);
    }
    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());
    uint64_t acc = 0;
    for (uint64_t i = 0; i < a.size(); ++i) {
        acc += a[i] > b[i] ? a[i] - b[i] : b[i] - a[i];
    }
    std::cout << acc << std::endl;
    return 0;
}
