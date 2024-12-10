#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

int main()
{
    std::ifstream inf{ "input.txt" };
    std::unordered_map<int, int> left, right; // number, freq

    if (!inf) {
        std::cerr << "Couldn't open file for reading!";
        return -1;
    }

    std::string s;
    for (int i = 0; inf >> s; i++) {
        int num = stoi(s);
        if (i & 1) {
            right[num]++;
        } else {
            left[num]++;
        }
    }

    long long result = 0;

    for (const auto& [num, freq] : left) {
        result += num * freq * right[num];
    }

    std::cout << result;

    return 0;
}