def reverse(l,start,end):
    if start>=end:
        return
    temp=l[start]
    l[start]=l[end]
    l[end]=temp

    reverse(l,start+1,end-1)

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reverse(l,0,len(l)-1)
    print (l)