#include <stdio.h>
#include <stdlib.h>

typedef struct minmax
{
    int min;
    int max;
} minmax;

minmax *find_min_max(int *arr, int size)
{
    minmax *min_max_value = (minmax *)malloc(sizeof(minmax));
    if (size <= 0)
    {
        min_max_value->max = arr[0];
        min_max_value->min = arr[0];
        return min_max_value;
    }
    min_max_value->max = arr[0];
    min_max_value->min = arr[0];

    for (int i = 1; i < size; i++)
    {
        if (arr[i] > (min_max_value->max))
            min_max_value->max = arr[i];
        else if (arr[i] < (min_max_value->min))
            min_max_value->min = arr[i];
    }

    return min_max_value;
}

void main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(int);

    minmax *result = find_min_max(arr, size);

    printf("\n MIN : %d", result->min);
    printf("\n MAX : %d", result->max);

    printf("\n");
}