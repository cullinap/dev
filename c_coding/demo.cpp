#include <iostream>
#include <vector>
#include <algorithm>

/* compile with g++ -std=c++11 -o democpp demo.cpp */

int main() {
	std::vector<int> w = {8,4,2,6,12};
	w.push_back(10);
	std::cout << "Number of elements in vector 'w': " << w.size() << std::endl;
	std::sort(w.begin(), w.end());

	for(int i : w)
		std::cout << i << std::endl;

	std::cout << "front: " << w.front() << std::endl;
	std::cout << "[1]: " << w[1] << std::endl;
	std::cout << "back: " << w.back() << std::endl;

	return 0;
}
