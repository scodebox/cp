#include <stdio.h>

void show(int *arr, int size)
{
    printf("\nARRAY: ");
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

void swap(int *arr, int x, int y)
{
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
}

// Function to move all negative elements one side.
void sort(int *arr, int size)
{
    // Start index 0.
    int start = 0;
    // End index
    int end = size - 1;

    while (start <= end)
    {
        // Swap all positive value with last index end & decrease end by 1.
        if (arr[start] >= 0)
        {
            swap(arr, start, end);
            end--;
        }
        else
            start++; // If arr[start] is not positive then increase start by 1.
    }
}

void main()
{
    int arr[] = {-1, 2, -3, 4, 5, 6, -7, 8, 9};
    int size = sizeof(arr) / sizeof(int);
    sort(arr, size);
    show(arr, size);
    printf("\n");
}