# String Manipulation  
# Write a program to check if a string is a palindrome (same forwards and backwards).

# str = list(input("Enter a word to check palindrome : "))
# str_cp = list(str)
# str_cp.reverse()
# print("Palindrome") if str == str_cp else print ("Not palindrome")


def rev_str(str): 
    str = str.replace(" ", "")
    return str[::-1]

str = input("Enter a word to check for palindrome : ").lower()
str_cp = rev_str(str)

print("Palindrome") if str == str_cp else print("Not palindrome")

