#include <stdio.h>
#include <iostream>

int main() {
	int values[5] = {10,20,30,40,50};

	printf("Basic fore loop over an array:\n");
	for (int i=0; i<5; i++)
		printf("%i\n", values[i]);

	printf("\nC++ range-based for loop\n");
	for(int i: values)
		std::cout << i << std::endl;

	std::cout << std::endl;

	printf("\nWhile loop with a break statement:\n");
	int v=1;
	while(v<10) {
		if(v % 7 == 0)
			break;
		printf("%i\n", v);
		v++;
	}
	printf("\n");

	return 0;
}

