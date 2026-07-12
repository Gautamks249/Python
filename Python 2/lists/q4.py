#second largest element

l = list (map(int, input("Enter numbers : ").split()))

largest = l[0]
sec_largest = l[0]

for i in l :
    if i > largest :
        sec_largest = largest
        largest = i
print("Second largest is : ", sec_largest)


# l.sort()
# print("Second Largest : ", l[-2])
