# File Handling  
# Write a program that reads a text file and prints the number of lines, words, and characters.

with open("ex.txt", "r") as f:
    data = f.read()
    print("\nText in our file :\n" + data)
    print("\n-----------------------------")
    print("Number of lines : ",data.count("\n")+1)
    data_li = list(data.split())
    print("Number of words : ", len(data_li))
    print("Number of characters : ", len(data))