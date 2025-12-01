#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static inline uint8_t normalize(int dial) { return ((dial % 100) + 100) % 100; }

static uint16_t star1(FILE *f) {
  uint16_t score = 0;
  uint8_t dial = 50;
  char buf[8];

  while (fgets(buf, sizeof(buf), f)) {
    int delta = atoi(buf + 1) % 100;
    dial = normalize(dial + (buf[0] == 'L' ? -delta : delta));
    if (!dial)
      score++;
  }
  return score;
}

static uint16_t star2(FILE *f) {
  uint16_t score = 0;
  uint8_t dial = 50;
  char buf[8];

  while (fgets(buf, sizeof(buf), f)) {
    int step = buf[0] == 'L' ? -1 : 1;
    for (int i = atoi(buf + 1); i--;) {
      dial = normalize(dial + step);
      if (dial == 0)
        score++;
    }
  }
  return score;
}

int main() {
  FILE *f;
  uint16_t result;
  f = fopen("01.input", "r");
  result = star1(f);
  fclose(f);
  printf("star1: %u\n", result);

  f = fopen("01.input", "r");
  result = star2(f);
  printf("star2: %u\n", result);
  fclose(f);
}
