#include <stdio.h>

int main() {
	int i,j,rows;

	char alphabet = 'A'; 

	printf("Enter the number of row: ");
	scanf("%d", &rows);

	for(i=0; i<=rows; ++i) {
		for(j=0; j<=i; ++j) {
			printf("%c", alphabet);
		}

		++alphabet;
		printf("\n");
	}

	return 0;
}

