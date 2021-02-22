#include <stdio.h>

void swap(int *arr, int x, int y)
{
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
}

int partition(int *arr, int start, int end)
{
    int pivot = arr[end];
    int tail_index = start;

    for (int i = start; i < end; i++)
    {
        if (arr[i] < pivot)
        {
            swap(arr, i, tail_index);
            tail_index++;
        }
    }
    swap(arr, end, tail_index);
    return tail_index;
}

int find_kth_max(int k, int *arr, int size)
{
    if ((k < 1) || (k > size))
    {
        printf("\nInvalid Input!");
        return -1;
    }
    else
    {
        int start = 0;
        int end = size - 1;

        while (start <= end)
        {
            int pivod_index = partition(arr, start, end);

            if (pivod_index == (size - k))
                return arr[pivod_index];

            if (pivod_index < (size - k))
                start = pivod_index + 1;
            else
                end = pivod_index - 1;
        }
    }
}

int find_kth_min(int k, int *arr, int size)
{
    if ((k < 1) || (k > size))
    {
        printf("\nInvalid Input!");
        return -1;
    }
    else
    {
        int start = 0;
        int end = size - 1;

        while (start <= end)
        {
            int pivod_index = partition(arr, start, end);

            if (pivod_index == (k - 1))
                return arr[pivod_index];

            if (pivod_index < (k - 1))
                start = pivod_index + 1;
            else
                end = pivod_index - 1;
        }
    }
}

void main()
{
    int arr[] = {10, 2, 7, 4, 9, 6, 3, 8, 1, 5};
    int size = sizeof(arr) / sizeof(int);
    int k;
    printf("\n ENTER K : ");
    scanf("%d", &k);
    printf("\n K-th MIN : %d ", find_kth_min(k, arr, size));
    printf("\n K-th MAX : %d ", find_kth_max(k, arr, size));
    printf("\n");
}