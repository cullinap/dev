#include <stdio.h>
#include <string.h>

int main() {
	char recipient[6] = {'W','o','r','l','d','\0'};
	char greeting[6] = "Hi";

	char message[10];

	int len = sprintf(message, "%s, %s!", greeting, recipient);
	int len2 = strlen(message); //redundant

	printf("Message: %s\n", message);
	printf("Message length: %i\n", len);
	printf("strlen: %i\n", len2);

	return 0;
}
