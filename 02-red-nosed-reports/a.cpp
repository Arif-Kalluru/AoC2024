#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

bool safe(std::vector<int>& v)
{
    bool increasing = false;
    bool decreasing = false;

    for (int i = 1; i < v.size(); i++) {
        auto diff = abs(v[i] - v[i-1]);
        if (diff < 1 || diff > 3)
            return false;

        if (!increasing && v[i] > v[i-1])
            increasing = true;
        
        if (!decreasing && v[i] < v[i-1])
            decreasing = true;

        if (increasing && decreasing)
            return false;
    }

    return true;
}

int main()
{
    std::ifstream file("input.txt");

    if (!file) {
        std::cerr << "Unable to open file\n";
        return 1;
    }

    std::string line;
    long count = 0;

    while (getline(file, line)) {
        std::vector<int> numbers;
        std::stringstream ss(line);
        int num;

        while (ss >> num) {
            numbers.emplace_back(num);
        }

        if (safe(numbers)) {
            count++;
        }
    }

    std::cout << count << '\n';
    file.close();

    return 0;
}