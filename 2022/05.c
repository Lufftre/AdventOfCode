#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct Cargo
{
    char cargo;
    struct Cargo *next;
} Cargo;

Cargo *stacks[10];
Cargo *stacks2[10];

void draw()
{
    for (int i = 0; i < 10; i++)
    {
        if (stacks[i] != NULL)
            printf("%c", stacks[i]->cargo);
    }
    puts("\n");
    for (int i = 0; i < 10; i++)
    {
        if (stacks2[i] != NULL)
            printf("%c", stacks2[i]->cargo);
    }
}

int main(void)
{
    FILE *file = fopen("05.input", "r");
    char linebuf[50];
    bool setup = true;
    while (fgets(linebuf, sizeof linebuf, file))
    {
        if (linebuf[0] == '\n')
        {
            setup = false;
        }
        else if (setup)
        {
            int i = 0;
            char c;
            do
            {
                c = linebuf[i];
                if (c >= 65 && c <= 90)
                {
                    // printf("i: %d %c\n", (i-1)/4, c);
                    int idx = (i - 1) / 4;
                    Cargo *cargo = malloc(sizeof(Cargo));
                    Cargo *cargo2 = malloc(sizeof(Cargo));
                    cargo->cargo = c;
                    cargo2->cargo = c;
                    if (stacks[idx])
                    {
                        Cargo *temp = stacks[idx];
                        while (temp->next != NULL)
                            temp = temp->next;
                        temp->next = cargo;

                        temp = stacks2[idx];
                        while (temp->next != NULL)
                            temp = temp->next;
                        temp->next = cargo2;
                        // stacks[idx]->next = cargo;
                    }
                    else
                    {
                        stacks[idx] = cargo;
                        stacks2[idx] = cargo2;
                    }
                }
                i++;
            } while (c);
        }
        else
        {
            int n, from, to;
            sscanf(linebuf, "move %d from %d to %d", &n, &from, &to);
            from--;
            to--;
            // 9000
            for (int i = 0; i < n; i++)
            {
                Cargo *moved = stacks[from];
                stacks[from] = moved->next;
                moved->next = stacks[to];
                stacks[to] = moved;
            }
            // 9001
            puts(linebuf);
            Cargo *top = stacks2[from];
            Cargo *bot = top;
            for (int i = 0; i < n - 1; i++)
            {
                bot = bot->next;
            }
            stacks2[from] = bot->next;
            bot->next = stacks2[to];
            stacks2[to] = top;
        }
    }

    draw();
}