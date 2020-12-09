#include <stdio.h>

int main() {
    //char star = '*';

    int i,j,z;


    j = 0;
    z = 0;

    for (i=0; i<3; i++){
        if (i==0)
            do {
                printf("*");
                j += 1;
            } while (j <= 3);
        if (i==1)
            printf("\n");
            do {
                printf("*");
                z += 1;
            } while (z <= 2);
      };

    printf("\n");

    return 0;
}
