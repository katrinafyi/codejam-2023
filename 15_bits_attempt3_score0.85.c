#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);

int parse_int(char*);
long parse_long(char*);

/*
 * Complete the 'bits' function below.
 *
 * The function is expected to return a LONG_INTEGER_ARRAY.
 * The function accepts LONG_INTEGER_ARRAY a as parameter.
 */

/*
 * To return the long integer array from the function, you should:
 *     - Store the size of the array to be returned in the result_count variable
 *     - Allocate the array statically or dynamically
 *
 * For example,
 * long* return_long_integer_array_using_static_allocation(int* result_count) {
 *     *result_count = 5;
 *
 *     static long a[5] = {1, 2, 3, 4, 5};
 *
 *     return a;
 * }
 *
 * long* return_long_integer_array_using_dynamic_allocation(int* result_count) {
 *     *result_count = 5;
 *
 *     long *a = malloc(5 * sizeof(long));
 *
 *     for (int i = 0; i < 5; i++) {
 *         *(a + i) = i + 1;
 *     }
 *
 *     return a;
 * }
 *
 */
long* bits(int a_count, long* a, int* result_count) {

    long* out = malloc(sizeof(long) * a_count);
    *result_count = a_count;
    
    for (int i = 0; i < a_count; i++) {
        int x = a[i];
        out[i] = x & (x-1);
    }
    return out;    
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    long nn = parse_long(ltrim(rtrim(readline())));

    long* aa = malloc(nn * sizeof(long));

    for (int i = 0; i < nn; i++) {
        long aa_item = parse_long(ltrim(rtrim(readline())));

        *(aa + i) = aa_item;
    }

    int yy_count;
    long* yy = bits(nn, aa, &yy_count);

    for (int i = 0; i < yy_count; i++) {
        fprintf(fptr, "%ld", *(yy + i));

        if (i != yy_count - 1) {
            fprintf(fptr, "\n");
        }
    }

    fprintf(fptr, "\n");

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}

long parse_long(char* str) {
    char* endptr;
    long value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
