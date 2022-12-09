#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
bool bufCheck(char *buf, int n)
{
    for (size_t i = 0; i < n - 1; i++)
    {
        for (size_t j = i + 1; j < n; j++)
        {
            if (buf[i] == buf[j])
                return false;
        }
    }
    return true;
}

int main(int argc, char *argv[])
{
    FILE *file = fopen("06.input", "r");
    char c;
    int n = strtol(argv[1], NULL, 10);
    char buf2[15] = "--------------";
    int i = 0;
    while ((c = fgetc(file)) != EOF)
    {
        memcpy(buf2 + 1, buf2, n);
        buf2[0] = c;
        puts(buf2);
        if (++i >= n && bufCheck(buf2, n))
            break;
    }
    long idx = ftell(file);
    printf("%d\n", i);
}