#check if list is already sorted

l = [0, 0, 1, 0]

sorted = False

if l[0] >= l[-1] :
    for i in range(len(l)-1):
        if l[i] >= l[i+1] :
            sorted = True
        else :
            sorted = False
            break
else :
    for i in range(len(l)-1):
        if l[i] <= l[i+1] :
            sorted = True    
        else :
            sorted = False
            break

print("Sorted list") if sorted else print("Not sorted")