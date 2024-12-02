#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

bool safe(std::vector<int>& v)
{
    bool increasing = false;
    bool decreasing = false;

    int prev = -1;

    for (const int& num : v) {
        if (num == -1) // that number was removed from the list
            continue;

        if (prev == -1) {
            prev = num;
            continue;
        }

        auto diff = abs(num - prev);

        if (diff < 1 || diff > 3)
            return false;

        if (!increasing && num > prev)
            increasing = true;
        
        if (!decreasing && num < prev)
            decreasing = true;

        if (increasing && decreasing)
            return false;
            
        prev = num;
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
        } else { // try to remove 1 element and see if it's safe (removing means, make that element -1)
            for (int i = 0; i < numbers.size(); i++) {
                int tmp = numbers[i];
                numbers[i] = -1;
                if (safe(numbers)) {
                    count++;
                    break;
                }
                numbers[i] = tmp;
            }
        }
    }

    std::cout << count << '\n';
    file.close();

    return 0;
}