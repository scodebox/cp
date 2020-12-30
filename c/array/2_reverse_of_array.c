#include <stdio.h>

void show(int *arr, int size)
{
    printf("\nARRAY: ");
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

void reverse(int *arr, int start, int end)
{
    if (start >= end)
        return;

    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;

    reverse(arr, start + 1, end - 1);
}

void main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(int);
    show(arr, size);
    reverse(arr, 0, size - 1);
    show(arr, size);
    printf("\n");
}
