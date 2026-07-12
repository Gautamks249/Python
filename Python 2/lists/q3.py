# #index of largest element

# l = list(map(int, input("Enter Numbers :").split()))
# l_copy = l.copy()
# l_copy.sort()
# print(f"Index of largest element is : {l.index(l_copy[-1])}")

l = list(map(int, input("Enter Numbers :").split()))

largest = l[0]
idx = 0
for i in range(len(l)):
    if l[i] > largest :
        largest = l[i]
        idx = i
else :
    print(f"Largest element : {largest} at index : {idx}")