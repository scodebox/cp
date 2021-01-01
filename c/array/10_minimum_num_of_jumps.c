#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

// Brute Force & Top Down approach
// TC: O(n^n)
// SC: O(1)
int solution_1(int index, int *arr, int size)
{
    // exit condition.
    if (index >= size)
        return -1;
    if (index == size - 1)
        return 0;

    int min_step = INT_MAX;

    // Try the all possible steps.
    for (int step = 1; step <= arr[index]; step++)
    {
        int temp_min = solution_1(index + step, arr, size);
        if (temp_min == -1)
            continue;
        // Take th minimum one.
        min_step = temp_min < min_step ? temp_min : min_step;
    }
    // If array element was zero | arr[index]==0.
    if (min_step == INT_MAX)
        return -1;
    // return min + 1.
    return (min_step + 1);
}

// Dynamic programming
// TC: O(n^2)
// SC: O(n)
int solution_2(int *arr, int size)
{
    // Invalid inputs.
    if (size <= 1 || *arr == 0)
        return -1;

    // To store min step to reach each elements.
    int *min_step = (int *)calloc(size, sizeof(int));

    for (int i = 1; i < size; i++)
    {
        // Calculating min step to reach element arr[i].
        for (int j = 0; j < i; j++)
        {
            if (j + arr[j] >= i)
            {
                min_step[i] = min_step[j] + 1;
                break;
            }
        }
        // If arr[i] element is not reachable. so last element is not also reachable.
        if (min_step[i] == 0)
            return -1;
    }
    // return the min step to reach last element.
    return (min_step[size - 1]);
}

// Dynamic programming
// TC: O(n)
// SC: O(1)
int solution_3(int *arr, int size)
{
    // Invalid inputs.
    if (size <= 1 || *arr == 0)
        return -1;

    // to store maximum reachable index of the array.
    int max_reachable_index = arr[0];
    // each step of a jump.
    int step = arr[0];
    // tract number of jumps to reach end.
    int jump = 1;
    // index of the array.
    int index = 1;

    // Traversing the array.
    for (int index = 1; index < size; index++)
    {
        // reached to the end return the jumps;
        if (index == size - 1)
            return jump;

        // decreasing the step by 1.| take a new step.
        step--;
        // updating the maximum reachable index with new step.
        max_reachable_index = max_reachable_index < (index + arr[index]) ? (index + arr[index]) : max_reachable_index;

        // when step is 0 count it as a jump.
        if (step == 0)
        {
            jump++;
            // The end is not rechable condition.
            if (index >= max_reachable_index)
                return -1;
            // steps for next jump.
            step = arr[index];
        }
    }
}

void main()
{
    int arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}; // 3
    // int arr[] = {1, 3, 0, 0, 0, 0, 6, 7, 6, 8, 9}; // Not reachable -1
    // int arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    // int arr[] = {0,0,0,0}; // Not rechable -1
    // int arr[] = {1, 1, 1}; // 2

    int size = sizeof(arr) / sizeof(int);

    printf("\n solution_1: %d", solution_1(0, arr, size));
    printf("\n solution_2: %d", solution_2(arr, size));
    printf("\n solution_3: %d", solution_3(arr, size));
    printf("\n");
}