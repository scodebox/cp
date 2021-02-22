#include <stdio.h>
#include <stdlib.h>

int int_cmp(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int minimize_maximum_difference(int *arr, int size, int k)
{

    if (size <= 1)
        return -1;

    int max, min, difference;
    // sort all the elements.
    qsort(arr, size, sizeof(int), int_cmp);

    // If we add/subtract k to each every element difference will be same.
    difference = arr[size - 1] - (*arr); // one probable solution

    // add k to min element and substract k from max element.
    max = arr[size - 1] - k;
    min = (*arr) + k;
    // swap is max < min after add and substract.
    if (max < min)
    {
        int temp = max;
        max = min;
        min = temp;
    }

    // for all the intermediate elements.
    for (int i = 1; i < size - 1; i++)
    {
        // greedy approach.
        // we can add k or substract k.
        int temp_max = arr[i] + k;
        int temp_min = arr[i] - k;

        // If any of those value comes in range of (min -> max) that does not change the difference.
        if (temp_max <= max || temp_min >= min)
            continue;

        // Outside range (min -> max).
        // update with that value which one add less penalty.
        if (abs(max - temp_min) < abs(temp_max - min))
            min = temp_min;
        else
            max = temp_max;
    }
    return (difference < abs(max - min) ? difference : abs(max - min));
}

void main()
{
    int arr1[] = {1, 15, 10};             // ANS 5
    int arr2[] = {1, 5, 15, 10};          // ANS 8
    int arr3[] = {4, 6};                  // ANS 2
    int arr4[] = {6, 10};                 // ANS 2
    int arr5[] = {1, 10, 14, 14, 14, 15}; // ANS 5
    int arr6[] = {1, 2, 3};               // ANS 2

    int k1 = 6;
    int k2 = 3;
    int k3 = 10;
    int k4 = 3;
    int k5 = 6;
    int k6 = 2;

    int size1 = sizeof(arr1) / sizeof(int);
    int size2 = sizeof(arr2) / sizeof(int);
    int size3 = sizeof(arr3) / sizeof(int);
    int size4 = sizeof(arr4) / sizeof(int);
    int size5 = sizeof(arr5) / sizeof(int);
    int size6 = sizeof(arr6) / sizeof(int);

    printf("\n Minimized difference : %d ", minimize_maximum_difference(arr1, size1, k1));
    printf("\n Minimized difference : %d ", minimize_maximum_difference(arr2, size2, k2));
    printf("\n Minimized difference : %d ", minimize_maximum_difference(arr3, size3, k3));
    printf("\n Minimized difference : %d ", minimize_maximum_difference(arr4, size4, k4));
    printf("\n Minimized difference : %d ", minimize_maximum_difference(arr5, size5, k5));
    printf("\n Minimized difference : %d ", minimize_maximum_difference(arr6, size6, k6));
    printf("\n");
}