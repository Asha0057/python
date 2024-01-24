#insertion sort: consider 1st ele as sorted and other half as unsorted and select the 2nd element as key value
#and compare with previuos value

def insertion(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1 #j is sorted part
        while(j>=0 and key<a[j]):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
        print(a)
a=[2,1,30,5,10,7]
insertion(a)
print(a)