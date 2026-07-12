# Lists & Iteration  
# Take 5 numbers as input, store them in a list, and print the largest number.


# nums = list(map(int, input("Enter numbers seperated by space : ").split()))
# nums.sort()
# print("Lagest number is : ",nums[-1])

nums = []
for i in range(5):
    nums.append(int(input("Enter a number  : ")))

nums.sort()
print(f"Largest Number is : {nums[-1]}")