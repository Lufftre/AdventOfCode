#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    FILE* file = fopen("01.input", "r");
    char linebuf[8];
    int sum;
    int cal[3] = {0,0,0};
    while (fgets(linebuf, sizeof linebuf, file)) {
        long snack = strtol(linebuf, NULL, 10);
        sum += snack;

        if(linebuf[0] == '\n' || feof(file) != 0) {
            for (int i = 0; i < 3; i++) {
                if(sum > cal[i]) {
                    memcpy(cal + i + 1, cal + i, (2 - i) * sizeof(*cal));
                    cal[i] = sum;
                    break;
                }
            }
            sum = 0;
        }
    }

    printf("top: %d\n", cal[0]);
    int top3;
    for (size_t i = 0; i < 3; i++)
    {
        top3 += cal[i];
    }
    printf("top3: %d", top3);

    fclose(file);
}