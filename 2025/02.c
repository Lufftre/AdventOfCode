#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE 1024
#define MAX_NUM_STR 32

typedef struct {
    long start, end;
} range_t;

static bool has_repeating_halves(long num) {
    char str[MAX_NUM_STR];
    int len = snprintf(str, sizeof(str), "%ld", num);

    if (len % 2 != 0) return false;

    int half = len / 2;
    return memcmp(str, str + half, half) == 0;
}

static bool has_repeating_pattern(long num) {
    char str[MAX_NUM_STR];
    int len = snprintf(str, sizeof(str), "%ld", num);

    for (int pattern_len = 1; pattern_len <= len / 2; pattern_len++) {
        if (len % pattern_len != 0) continue;

        bool matches = true;
        for (int i = pattern_len; i < len && matches; i++) {
            if (str[i] != str[i % pattern_len]) {
                matches = false;
            }
        }
        if (matches) return true;
    }
    return false;
}

static long solve_part1(const range_t *ranges, int count) {
    long total = 0;
    for (int i = 0; i < count; i++) {
        for (long num = ranges[i].start; num <= ranges[i].end; num++) {
            if (has_repeating_halves(num)) {
                total += num;
            }
        }
    }
    return total;
}

static long solve_part2(const range_t *ranges, int count) {
    long total = 0;
    for (int i = 0; i < count; i++) {
        for (long num = ranges[i].start; num <= ranges[i].end; num++) {
            if (has_repeating_pattern(num)) {
                total += num;
            }
        }
    }
    return total;
}

static int parse_ranges(const char *line, range_t *ranges, int max_ranges) {
    int count = 0;
    const char *pos = line;
    long start, end;
    int consumed;

    while (count < max_ranges && sscanf(pos, "%ld-%ld%n", &start, &end, &consumed) >= 2) {
        ranges[count++] = (range_t){start, end};
        pos += consumed;
        if (*pos == ',') pos++;  // Skip comma
        else break;
    }
    return count;
}

int main(void) {
    FILE *f = fopen("02.input", "r");
    if (!f) return EXIT_FAILURE;

    char line[MAX_LINE];
    if (!fgets(line, sizeof(line), f)) {
        fclose(f);
        return EXIT_FAILURE;
    }

    range_t ranges[100];  // Assume max 100 ranges
    int range_count = parse_ranges(line, ranges, 100);

    printf("Part 1: %ld\n", solve_part1(ranges, range_count));
    printf("Part 2: %ld\n", solve_part2(ranges, range_count));

    fclose(f);
    return EXIT_SUCCESS;
}
