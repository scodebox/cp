#include <stdio.h>

void show(int *arr, int size, char *msg)
{
    printf("\n%s: ", msg);
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

void rotate(int *arr, int size)
{
    // copy last element
    int last_item = arr[size - 1];

    // shift all elements to next cell.
    for (int i = size - 2; i >= 0; i--)
        arr[i + 1] = arr[i];

    // copy back last element to first cell.
    *arr = last_item;

    show(arr, size, "ROTATE");
}

void main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(int);
    rotate(arr, size);
    rotate(arr, size);
    rotate(arr, size);
    rotate(arr, size);
    printf("\n");
}