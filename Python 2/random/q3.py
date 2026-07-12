# Loops  
# Print the multiplication table of a number (from 1 to 10).

print("Table from 1 to 10 :- \n -------------------------------------------------------")
for i in range(1,11):
    for j in range(1,11):
        print(f"{j*i:4}", end = " ")
    print()
print("-----------------------------------------------------")
num = int(input("\n \nEnter a number for which you want to print Table : "))
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")