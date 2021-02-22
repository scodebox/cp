#include <stdio.h>
#include <stdlib.h>

void show(int *arr, int size, char *msg)
{
    printf("\n%s: ", msg);
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

// Function for union.
void compute_union(int *arr1, int *arr2, int size_1, int size_2)
{
    // Max possible size for union size_1 + size_2.
    int *result = (int *)malloc(sizeof(int) * (size_2 + size_1));
    // arr1 index i.
    // arr2 index j.
    // result index index.
    int index, i, j;
    index = i = j = 0;

    // modified merge function from merge sort.
    while ((i < size_1) && (j < size_2))
    {
        if (arr1[i] == arr2[j])
        {
            result[index++] = arr1[i++];
            j++;
        }
        else if (arr1[i] < arr2[j])
            result[index++] = arr1[i++];
        else if (arr1[i] > arr2[j])
            result[index++] = arr2[j++];
    }

    while (i < size_1)
        result[index++] = arr1[i++];
    while (j < size_2)
        result[index++] = arr2[j++];

    show(result, index, "UNION");
}

void compute_intersection(int *arr1, int *arr2, int size_1, int size_2)
{
    // Max possible size for intersection min(size_1, size_2).
    int *result = (int *)malloc(sizeof(int) * (size_1 < size_2 ? size_1 : size_2));
    // arr1 index i.
    // arr2 index j.
    // result index index.
    int index, i, j;
    index = i = j = 0;

    // modified merge function from merge sort.
    while ((i < size_1) && (j < size_2))
    {
        if (arr1[i] == arr2[j])
        {
            result[index++] = arr1[i++];
            j++;
        }
        else if (arr1[i] < arr2[j])
            i++;
        else if (arr1[i] > arr2[j])
            j++;
    }

    show(result, index, "INTERSECTION");
}

void main()
{
    int arr1[] = {1, 3, 4, 5, 7};
    int arr2[] = {2, 3, 5, 6};
    // int arr1[] = {2, 5, 6};
    // int arr2[] = {4, 6, 8, 10};
    int size_1 = sizeof(arr1) / sizeof(int);
    int size_2 = sizeof(arr2) / sizeof(int);
    compute_union(arr1, arr2, size_1, size_2);
    compute_intersection(arr1, arr2, size_1, size_2);
    printf("\n");
}