# find average

l = list(map(int, input("Enter Numbers : ").split()))

sum = 0

for i in l:
    sum+=i

print(f"Average is : {sum/len(l)}")