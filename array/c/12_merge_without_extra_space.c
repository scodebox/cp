// compile using lm flag -> cc 12_merge_without_extra_space.c -lm

#include <stdio.h>
#include <math.h>

void show(int *arr, int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

void swap(int *item_1, int *item_2)
{
    int temp = *item_1;
    *item_1 = *item_2;
    *item_2 = temp;
}

// Insertion 1 pass :: O(n)
void sort(int *arr, int size)
{
    int temp;
    for (int i = 1; i < size; i++)
        if (arr[i - 1] > arr[i])
            swap(arr + i, arr + (i - 1));
}

// TC: O(mxn) | SC: O(1)
void solution_1(int *arr_1, int *arr_2, int size_1, int size_2)
{
    int index_1 = 0;
    int index_2 = 0;
    int temp;

    while (index_1 < size_1)
    {
        if (arr_1[index_1] >= arr_2[index_2])
        {
            swap(arr_1 + index_1, arr_2 + index_2);
            // After each swap sort the arr_2.
            sort(arr_2, size_2);
        }
        else
            index_1++;
    }
}

// TC: O(n log n) | SC: O(1) :: Gap Method
void solution_2(int *arr_1, int *arr_2, int size_1, int size_2)
{
    int i, j;
    // calculating gap. [(size 1 + size 2)/2]
    int gap = (int)ceil((double)(size_1 + size_2) / 2);

    // Do this till gap = 1.
    while (gap >= 1)
    {
        // For arr 1.
        for (i = 0; i + gap < size_1; i++)
            if (arr_1[i] > arr_1[i + gap])
                swap(arr_1 + i, arr_1 + i + gap);

        // For arr 1 & arr 2.
        for (j = gap < size_1 ? 0 : (size_1 - gap); i < size_1 && j < size_2; i++, j++)
            if (arr_1[i] > arr_2[j])
                swap(arr_1 + i, arr_2 + j);

        // For arr 2. while arr 1 exceeded.
        if (!(i < size_1) && j < size_2)
            for (j = 0; j + gap < size_2; j++)
                if (arr_2[j] > arr_2[j + gap])
                    swap(arr_2 + j, arr_2 + (j + gap));

        // Because of ceil value gap would not become 0. So when operation of gap = 1 is done break the loop.
        if (1 == gap)
            break;
        else
            gap = (int)ceil((double)gap / 2);
    }
}

void main()
{
    // int arr_1[] = {10};
    // int arr_2[] = {2, 3};

    // int arr_1[] = {1, 5, 9, 10, 15, 20};
    // int arr_2[] = {2, 3, 8, 13};

    int arr_1[] = {3, 4, 7, 10};
    int arr_2[] = {1, 2, 8, 9, 12, 13};

    int size_1 = sizeof(arr_1) / sizeof(int);
    int size_2 = sizeof(arr_2) / sizeof(int);

    // solution_1(arr_1,arr_2,size_1,size_2);
    solution_2(arr_1, arr_2, size_1, size_2);

    show(arr_1, size_1);
    printf("\n");
    show(arr_2, size_2);
    printf("\n");
}