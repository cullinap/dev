#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char password[16];
	int passcheck = 0;

	printf("\nWhat's the secret password?\n");
	gets(password);

	if(strcmp(password, "password1")) {
		printf("\nYou fail!\n");
	} else {
		printf("\nCorrect Password\n");
		passcheck = 1; // change pass value so code executes below
	}

	if(passcheck) { // A value other than 0 means it was set above
		// Do privleged stuff here, in this case read a protected fil
		system("cat shadow");
	}

	return 0;
}





