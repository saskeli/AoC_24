#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>
#include <unordered_set>

int main(int argc, char const *argv[]) {
    std::vector<uint64_t> a;
    std::unordered_multiset<uint64_t> b;
    uint64_t v;
    while (std::cin >> v) {
        a.push_back(v);
        std::cin >> v;
        b.insert(v);
    }
    uint64_t acc = 0;
    for (uint64_t i = 0; i < a.size(); ++i) {
        acc += a[i] * b.count(a[i]);
    }
    std::cout << acc << std::endl;
    return 0;
}
