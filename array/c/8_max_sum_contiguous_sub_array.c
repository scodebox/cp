#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

/*
Dynamic Programming : using Kadane’s Algorithm
*/

int max_sub_array_sum(int *arr, int size)
{
    int max_sum = INT_MIN;
    for (int i = 1; i < size; i++)
    {
        // calculating max possible sub array sum upto index i.
        arr[i] = (arr[i] < (arr[i] + arr[i - 1]) ? (arr[i] + arr[i - 1]) : arr[i]);
        // keeping track of max sum.
        if (max_sum < arr[i])
            max_sum = arr[i];
    }
    return max_sum;
}

void main()
{
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3}; // 7
    // int arr[] = {-2, 1, -3, 4,-1, 2, 1, -5, 4}; // 6
    int size = sizeof(arr) / sizeof(int);
    printf("MAX SUM: %d", max_sub_array_sum(arr, size));
    printf("\n");
}