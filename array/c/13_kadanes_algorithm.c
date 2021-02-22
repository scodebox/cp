#include <stdio.h>

// Kadane's Algorithm
// TC: O(n) | SC: O(1)
int kadans_algo(int *arr, int size)
{
    int global_max = *arr;
    // Check the current value && current value + previous value >> take the max.
    for (int i = 1; i < size; i++)
    {
        arr[i] = arr[i] < arr[i] + arr[i - 1] ? arr[i] + arr[i - 1] : arr[i];
        global_max = global_max < arr[i] ? arr[i] : global_max;
    }
    return global_max;
}

void main()
{
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3}; // 7
    // int arr[] = {-2, 1, -3, 4,-1, 2, 1, -5, 4}; // 6
    int size = sizeof(arr) / sizeof(int);
    printf("GLOBAL MAX: %d", kadans_algo(arr, size));
    printf("\n");
}