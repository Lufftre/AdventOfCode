#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int parseSack(char *linebuf)
{
    int items = strlen(linebuf) - 1;
    for (size_t i = 0; i < items / 2; i++)
    {
        char item = linebuf[i];
        for (size_t j = items / 2; j < items; j++)
        {
            if (item == linebuf[j])
            {
                if (item < 97)
                    return item - 65 + 27;
                else
                    return item - 96;
            }
        }
    }
    return 0;
}

int parseGroup(FILE *file)
{
    char items1[100];
    char items2[100];
    char matches[100];
    int x = 0;
    fgets(items1, sizeof items1, file);
    int nitems1 = strlen(items1) - 1;

    fgets(items2, sizeof items2, file);
    int nitems2 = strlen(items2) - 1;

    for (size_t i = 0; i < nitems1; i++)
    {
        for (size_t j = 0; j < nitems2; j++)
        {
            if (items1[i] == items2[j])
            {
                matches[x] = items1[i];
                x++;
            }
        }
    }
    fgets(items1, sizeof items1, file);
    nitems1 = strlen(items1) - 1;

    for (size_t i = 0; i < x; i++)
    {
        for (size_t j = 0; j < nitems1; j++)
        {
            if (matches[i] == items1[j])
            {
                if ( matches[i] < 97)
                    return  matches[i] - 65 + 27;
                else
                    return  matches[i] - 96;
            }
        }
    }
    return 0;
}

int main(void)
{
    FILE *file = fopen("03.input", "r");
    char linebuf[100];
    int priority = 0;

    while (fgets(linebuf, sizeof linebuf, file))
    {
        priority += parseSack(linebuf);
    }
    printf("sum: %d\n", priority);

    fseek(file, 0, SEEK_SET);
    priority = 0;
    while (true)
    {
        priority += parseGroup(file);
        if (feof(file))
            break;
    }
    printf("sum: %d\n", priority);
}