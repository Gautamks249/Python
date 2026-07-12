# Dictionary & Frequency Count  
# Count the frequency of each word in a given sentence and print the results.

para = input("Enter your para : ").lower()
print("\n ------------------------------------------- \n")

para_list = list(map(str, para.split()))

word_dict = {}
 
for word in para_list:
    fr = para_list.count(word)
    word_dict[word] = fr

print(f"{"word":<8}", "frequency")
for word in word_dict:
    print(f"{word :<8}", word_dict[word])






