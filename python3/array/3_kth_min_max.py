def partition(arr,start,end):
    pivot=arr[end]
    tail_index=start

    for i in range(start,end):
        if arr[i]<pivot:
            arr[i],arr[tail_index]=arr[tail_index],arr[i]
            tail_index+=1
        
    arr[end],arr[tail_index]=arr[tail_index],arr[end]
    return tail_index

def find_kth_min(k,arr):
    if k<1 or k>len(arr):
        print ('Invalid Input!')
        return -1
    else:
        start=0
        end=len(arr)-1
        while start<=end:
            pivot_index=partition(arr,start,end)
            if pivot_index==(k-1):
                return arr[pivot_index]
            elif pivot_index<(k-1):
                start=pivot_index+1
            else:
                end=pivot_index-1


def find_kth_max(k,arr):
    if k<1 or k>len(arr):
        print ('Invalid Input!')
        return -1
    else:
        start=0
        end=len(arr)-1
        while start<=end:
            pivot_index=partition(arr,start,end)
            if pivot_index==(len(arr)-k):
                return arr[pivot_index]
            elif pivot_index<(len(arr)-k):
                start=pivot_index+1
            else:
                end=pivot_index-1

if __name__ == '__main__':
    arr = [10, 2, 7, 4, 9, 6, 3, 8, 1, 5]
    k=9
    print ("K-th MIN : ",find_kth_min(k, arr))
    print ("K-th MAX : ",find_kth_max(k, arr))