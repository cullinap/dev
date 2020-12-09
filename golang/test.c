#include <stdio.h>

int x = 5;

int fn(int val) {
    if (val == 0)
        return 0; 
    val -= 1;
    printf("%d\n", val);
    return fn(val);
}

int main() {
    fn(x);

    return 0;
}


