#include <stdio.h>

#define ROCK 'A'
#define PAPER 'B'
#define SCISSORS 'C'

#define WIN_SCORE 6
#define DRAW_SCORE 3
#define LOSE_SCORE 0

#define LOSE 'X'
#define DRAW 'Y'
#define WIN 'Z'

#define Bonus(x) ((x) - (64))

int rps(char elf, char myhand)
{
    if(elf == myhand)
        return DRAW_SCORE;

    if (elf == ROCK)
    {
        if(myhand == PAPER)
            return WIN_SCORE;
        return LOSE_SCORE;
    }

    if (elf == PAPER)
    {
        if(myhand == SCISSORS)
            return WIN_SCORE;
        return LOSE_SCORE;
    }

    if (elf == SCISSORS)
    {
        if(myhand == ROCK)
            return WIN_SCORE;
        return LOSE_SCORE;
    }
}

int main(void)
{
    FILE* file = fopen("02.input", "r");
    char linebuf[5];
    char elf, x, myhand, myhand2;
    int totalscore1 = 0;
    int totalscore2 = 0;
    while(fgets(linebuf, sizeof linebuf, file))
    {
        sscanf(linebuf, "%c %c", &elf, &x);
        myhand = x - 23;
        totalscore1 += rps(elf, myhand);
        totalscore1 += Bonus(myhand);

        if(x == DRAW)
            myhand2 = elf;
        else if (x == WIN)
            myhand2 = ((elf + 2) % 3) + 65;
        else
            myhand2 = ((elf) % 3) + 65;

        totalscore2 += rps(elf, myhand2);
        totalscore2 += Bonus(myhand2);
    }
    printf("part1 score: %d\n", totalscore1);
    printf("part2 score: %d\n", totalscore2);
}