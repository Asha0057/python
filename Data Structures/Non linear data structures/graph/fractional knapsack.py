class item:
    def _init_(self, weight, profit):
        self.weight = weight
        self.profit = profit
def fractional_knapsack(w,arr):
    arr.sort(key=lambda x:(x.profit/x.weight),reverse=True)
    finalvalue=0.0
    for item in arr:
        if item.weight<=w:
            w-=item.weight
            finalvalue+=item.profit
        else:
            finalvalue+=item.profit*w/item.weight
            break
    return finalvalue
w=int(input())
n=int(input())
arr = []
a=[]
for i in range(n):
    weight = int(input("Enter the weight of item {}: ".format(i + 1)))
    profit = int(input("Enter the profit of item {}: ".format(i + 1)))
    arr.append(item(weight,profit))

print(fractional_knapsack(w, arr))