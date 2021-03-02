#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define MAX_NAME 256
#define TABLE_SIZE 10

typedef struct {
	char name[MAX_NAME];
	int age;
} person;

person * hash_table[TABLE_SIZE];

unsigned int hash(char *name) {
	int length = strnlen(name, MAX_NAME);
	unsigned int hash_value = 0;
	for (int i=0; i < length; i++) {
		hash_value += name[i];
		hash_value = (hash_value * name[i]) % TABLE_SIZE;
	}	
	return hash_value;
}

void init_hash_table() {
	for (int i=0; i < TABLE_SIZE; i++) {
		hash_table[i] = NULL;
	}
	// table is empty
}

int main() {
	
	printf("Jacob => %u\n", hash("Jacob"));
	printf("Louise => %u\n", hash("Louise"));
	return 0;
}
