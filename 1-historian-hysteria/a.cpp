#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::ifstream inf{ "input.txt" };
    std::vector<int> left, right;
    left.reserve(1000);
    right.reserve(1000);

    if (!inf) {
        std::cerr << "Couldn't open file for reading!";
        return -1;
    }

    std::string s;
    for (int i = 0; inf >> s; i++) {
        int num = stoi(s);
        if (i & 1) {
            right.emplace_back(num);
        } else {
            left.emplace_back(num);
        }
    }

    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    long long result = 0;

    for (int i = 0; i < left.size(); i++) {
        result += abs(left[i] - right[i]);
    }

    std::cout << result;

    return 0;
}