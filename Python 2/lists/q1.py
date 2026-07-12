# print positive and negative numbers separately

l = list(map(int, input("Enter numbers : ").split()))

p = []
n = []

for i in l:
    # if i < 0:
    #     n.append(i)
    # else :
    #     p.append(i)
    n.append(i) if i < 0 else p.append(i)

print(f"Given list : {l} \nPositive list : {p} \nNegative list : {n}")
