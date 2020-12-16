#include <iostream>
#include <string>
using std::string;
using std::cout;

void f(string recipient) {
	cout << "Hello, " << recipient << "!\n";
}

int g(int a, int b) {
	return a + b;
}

double circ(double r) {
	return r * 2 * 3.14159;
}

int main() {
	string recipient = "World";

	f(recipient);

	cout << "g(2,3): " << g(2,3) << std::endl;
	cout << "circ(5): " << circ(5) << std::endl;

	return 0;
}
