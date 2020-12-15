#include <iostream>
#include <string>
using std::string;
using std::cout;

int main() {
	string recipient = "World";
	string greeting = "Hi";
	string message;

	message = greeting + ", " + recipient + "!";

	cout << "Message: " << message << std::endl;
	cout << "Message length: " << message.size() << std::endl;

	return 0;

}

