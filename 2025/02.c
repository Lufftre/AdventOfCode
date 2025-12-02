#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  char start[128];
  int nStart;
  char end[128];
  int nEnd;
} Range;

long process_range(Range r) {
  long res = 0;
  // printf("%s [%d] | %s [%d]\n", r.start, r.nStart, r.end, r.nEnd);
  long start = atol(r.start);
  long end = atol(r.end);
  for (long i = start; i <= end; i++) {
    char sstart[32];
    sprintf(sstart, "%ld", i);
    size_t nChars = strlen(sstart);
    if (nChars % 2 != 0)
      continue;
    size_t half = nChars / 2;
    if (strncmp(sstart, sstart + half, half) == 0) {
      res += i;
    }
  }
  return res;
}

// Checks if long is made of any repeating biword, triword etc
bool isInvalid(long l) {
  // 2121212121
  char sstart[32];
  sprintf(sstart, "%ld", l);
  size_t nChars = strlen(sstart);
  size_t half = nChars / 2;
  for (int i = 1; i <= half; i++) {
    if (nChars % i != 0)
      continue;
    bool allMatch = true;
    for (int j = 0; j < nChars / i; j++) {
      if (strncmp(sstart, sstart + j * i, i) != 0) {
          allMatch = false;
          break;
      }
    }
    if (allMatch) return true;
  }
  return false;
}

long process_range2(Range r) {
  long res = 0;
  long start = atol(r.start);
  long end = atol(r.end);
  for (long i = start; i <= end; i++) {
    if (isInvalid(i)) {
      res += i;
    }
  }
  return res;
}

int main() {
  FILE *f = fopen("02.input", "r");
  if (!f)
    return 1;

  char *line = NULL;
  size_t len = 0;
  Range r = {0};
  long res, res2 = 0;

  if (getline(&line, &len, f) != -1) {
    char *token = strtok(line, "-");
    while (token) {
      strcpy(r.start, token);
      r.nStart = strlen(r.start);
      token = strtok(NULL, ",");
      strcpy(r.end, token);
      r.nEnd = strlen(r.end);
      res += process_range(r);
      res2 += process_range2(r);
      token = strtok(NULL, "-");
    }
  }

  free(line);
  fclose(f);
  printf("res: %ld\n", res);
  printf("res2: %ld\n", res2);
  return 0;
}
