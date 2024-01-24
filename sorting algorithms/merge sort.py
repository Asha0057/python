#merge sort: divide and conquer method.
def merging(arr):
    if(len(arr)>1):
        b=len(arr)//2

        left=arr[:b]
        right=arr[b:]

        merging(left) #until arr become <1 this recursive fun executes
        merging(right)

        i = k = j = 0

        while(i<len(left)) and (j<len(right)):
            if left[i]<right[j]:
                arr[k]=left[i]
                i=i+1
                k=k+1
            else:
                arr[k]=right[j]
                k=k+1
                j = j + 1

        while(i<len(left)):
            arr[k]=left[i]
            k=k+1
            i=i+1
        while(j<len(right)):
            arr[k]=right[j]
            k=k+1
            j=j+1
arr=[3,1,4,6,4,7,3]
merging(arr)
print("sorted",arr)
