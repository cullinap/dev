#include <stdio.h>

int main() {
	int x = 3;
	char c = 'D';
	double p = 3.14;

	int y = x + 3;
	char d = c + 3;
	double q = p + 3;

	printf("x, y: %i, %i\n", x, y);
	printf("c, d: %c, %c\n", c, d);
	printf("p, q: %f, %f\n", p, q);

	return 0;
}
