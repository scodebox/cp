#include <stdio.h>
#include <stdlib.h>

// TC: O(n) | SC: O(n)
int solution_1(int *arr, int size)
{
    int *frequency_count = (int *)calloc(size, sizeof(int));

    for (int i = 0; i < size; i++)
    {
        frequency_count[arr[i]]++;
        // when frequency of a number is more than 1 return that number.
        if (frequency_count[arr[i]] > 1)
            return arr[i];
    }
    // no duplicate number.
    return -1;
}

// Floyd's Tortoise and Hare (Cycle Detection)
// TC: O(n) | SC: O(1)
int solution_2(int *arr, int size)
{
    int fast_pointer, slow_pointer;
    fast_pointer = slow_pointer = *arr;

    do
    {
        fast_pointer = arr[arr[fast_pointer]];
        slow_pointer = arr[slow_pointer];
    } while (fast_pointer != slow_pointer);

    fast_pointer = *arr;

    while (fast_pointer != slow_pointer)
    {
        slow_pointer = arr[slow_pointer];
        fast_pointer = arr[fast_pointer];
    }
    
    return slow_pointer;
}

void main()
{
    int arr[] = {1, 3, 4, 2, 2}; // 2
    // int arr[] = {3,1,3,4,2}; // 3
    // int arr[] = {1,1}; // 1
    // int arr[] = {1,1,2}; // 1

    int size = sizeof(arr) / sizeof(int);

    printf("\n Duplicate item : %d", solution_1(arr, size));
    printf("\n Duplicate item : %d", solution_2(arr, size));
    printf("\n");
}