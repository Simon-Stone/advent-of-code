#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::vector<int> > parse_input(std::istream& input)
{
    std::vector<int> current_elf;
    std::vector< std::vector<int> > elves;
    for (std::string line; std::getline(input, line); )
    {
        if(!line.empty())
        {
            current_elf.push_back(std::stoi(line));
        }
        else
        {
            elves.push_back(current_elf);
            current_elf.clear();
        }
    }
    return elves;
}


std::vector<int> sum_calories(const std::vector< std::vector<int> >& elves)
{
    std::vector<int> sums;

    std::transform(elves.begin(), elves.end(), 
                   std::back_inserter(sums),  
                   [](const auto& elf){ 
                    return std::reduce(elf.begin(), elf.end());
                    });
    return sums;
}
 
int part_one(const std::vector< std::vector<int> >& elves)
{
    auto sums = sum_calories(elves);
    return *std::max_element(sums.begin(), sums.end());
}


int part_two(const std::vector< std::vector<int> >& elves)
{
    auto sums = sum_calories(elves);
    std::sort(sums.begin(), sums.end());
    return std::reduce(sums.rbegin(), sums.rbegin()+3);
}

int main()
{
    std::ifstream input("2022/day-01/input.txt");

    auto elves = parse_input(input);
    std::cout << part_one(elves) << std::endl;
    std::cout << part_two(elves) << std::endl;
} 