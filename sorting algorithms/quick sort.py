#quick sort:choose one element as pivot,based on that compare the elements and segregate the lower in left side
#and greater in right side.
#here we used 3 list to store lower,uper,and equal values  of pivot
def quick_sort(l1):
    if(len(l1))<=1:
        return l1
    else:
        pivot_ind = len(l1) // 2
        pivot = l1[pivot_ind]
        lp = []
        up = []
        eq=[]
        for i in l1:
            if (i < pivot):
                lp.append(i)
            elif i>pivot:
                up.append(i)
            else:
                eq.append(i)

    return quick_sort(lp) + eq +quick_sort(up)

n=int(input("how many?"))
l1=[]
for i in range(n):
    l1.append(int(input()))
sorted=quick_sort(l1)
print("sorted:",sorted)

