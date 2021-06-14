#include <stdio.h>

int main() {
	int i,j;

	char end,alphabet = 'A';

	printf("Enter the letter your would like to end on: ");
	scanf("%s", &end);

	for(i=1; i<=(end - 'A' + 1); ++i) {
		for(j=1; j<=i; ++j) {
			printf("%c", alphabet);
		}

		++alphabet;
		printf("\n");
	}

	return 0;
}


