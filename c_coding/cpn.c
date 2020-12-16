#include <stdio.h>

int main() {
	int i = 10;
	int *p;
	p = &i;

	printf("i, *p, p: %i, %i, %p\n", i, *p, p);

	*p = 5;
	printf("i: %i\n", i);

	char greeting[] = "Hello";
	char *q = greeting;

	while (*q != '\0') {
		printf("%c", *q);
		q++;
	}

	printf("\n");


	return 0;
}
