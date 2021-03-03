#include <stdio.h>

void show_array(int *a, unsigned int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
}

void swap(int *list, int index_1, int index_2)
{
    int temp = list[index_1];
    list[index_1] = list[index_2];
    list[index_2] = temp;
}

void reverse(int *list, int start, int end)
{
    while (start < end)
    {
        swap(list, start, end);
        ++start;
        --end;
    }
}

int next_permutation(int *list, int size)
{
    int inverse_position = size - 1;

    while (inverse_position >= 0 && list[inverse_position - 1] >= list[inverse_position--])
        ;

    if (inverse_position >= 0)
    {
        int next_greater = size - 1;
        while (next_greater >= 0 && list[next_greater] <= list[inverse_position])
            --next_greater;

        swap(list, next_greater, inverse_position);
    }

    reverse(list, inverse_position + 1, size - 1);
}

int main()
{
    int arr[] = {1, 3, 5, 4, 2}; // 1,4,2,3,5
    // int arr[] = {1, 2, 3}; // 1,3,2
    // int arr[] = {3, 2, 1}; // 1,2,3
    // int arr[] = {1, 1, 5}; // 1,5,1
    // int arr[] = {1}; // 1

    int size = sizeof(arr) / sizeof(int);

    next_permutation(arr, size);
    show_array(arr, size);

    printf("\n");
}