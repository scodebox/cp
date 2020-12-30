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

// Function for sorting.
void sort(int *arr, int size)
{
    // Low at first index.
    int low = 0;
    // High at last index.
    int high = size - 1;
    // Mid ar first index. Will be moving towards high.
    int mid = 0;

    while (mid <= high)
    {
        switch (arr[mid])
        {
        case 0:
            // When the mid index value is 0 -> swap with low.
            swap(arr, low, mid);
            // Increase the low and mid index by one.
            low++;
            mid++;
            break;
        case 1:
            // If the mid index value is 1 just move to next index.
            mid++;
            break;
        case 2:
            // If the mid index value is 2 -> swap with high index.
            swap(arr, high, mid);
            // Decrease the high index by 1. DONT do anything to mid index.
            high--;
            break;
        }
    }
}

void main()
{
    int arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
    int size = sizeof(arr) / sizeof(int);
    sort(arr, size);
    show(arr, size);
    printf("\n");
}