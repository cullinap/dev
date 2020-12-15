#include <iostream>
using std::cout;

int main() {
	int i = 0;
	bool b = true;

	if(i==10)
		cout << "i is 10\n";
	else
		cout << "i is not 10\n";
	
	if(i > 0) {
		cout << "i > 0\n";
	} else if (i<0) {
		cout << "I < 0\n";
	} else {
		cout << "else (i==0)\n";
		if(!b) {
			cout << "!b\n";
		} else {
			cout << "else (b)\n";
		}
	}

	return 0;
}

