
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define STAR2 1


void star1(FILE* f) {
    int s = 0;
    int dial = 50;
    char line[256];
    while (fgets(line, sizeof(line), f)) {
        char dir = line[0];
        int d = atoi(line + 1);
        d %= 100;
        if (dir == 'L') {
           dial -= d;
           if (dial < 0) {
               dial += 100;
           }
        } else {
            dial += d;
        }
        dial %= 100;
        if (dial == 0) {
            s += 1;
        }
        printf("%c %d => %d\n", dir, d, dial);
    }
    printf("%d\n", s);
}

void star2(FILE* f) {
    printf("Star 2\n");
    int s = 0;
    int dial = 50;
    char line[256];
    while (fgets(line, sizeof(line), f)) {
        char dir = line[0];
        int v = 1;
        if (dir == 'L') {
            v = -1;
        }
        int d = atoi(line + 1);
        for (int i = 0; i < d; i++) {
            dial += v;
            if (dial < 0) {
                dial += 100;
            } else if (dial > 99) {
                dial -= 100;
            }

            if (dial == 0) {
                s += 1;
            }
        }
    }
    printf("%d\n", s);
}

int main() {
    FILE *file = fopen("01.input", "r");
    if (file == NULL) {
        printf("Error: Could not open file 01.input\n");
        return 1;
    }

    if(!STAR2)
        star1(file);
    else
        star2(file);

    fclose(file);
    return 0;
}
