#include <stdio.h>

int main(void)
{
    FILE *file = fopen("04.input", "r");

    char linebuf[100];
    int min1, min2, max1, max2;
    int contained = 0;
    int overlap = 0;
    while(fgets(linebuf, sizeof linebuf, file))
    {
        sscanf(linebuf, "%d-%d,%d-%d", &min1, &max1, &min2, &max2);
        if(min1 <= min2 && max1 >= max2)
            contained++;
        else if(min1 >= min2 && max1 <= max2)
            contained++;

        if(min1 <= min2 && max1 >= min2)
            overlap++;
        else if(min2 <= min1 && max2 >= min1)
            overlap++;


    }
    printf("%d\n", contained);
    printf("%d\n", overlap);
}