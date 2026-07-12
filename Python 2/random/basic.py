gradelist = []
def calgrade(marks) :
    
    for sub in marks:
        if sub[1] > 90 :
            gradelist.append("A")
        elif sub[1] > 70 :
            gradelist.append("B")
        elif sub[1] > 50 :
            gradelist.append("C")
        elif sub[1] > 40 :
            gradelist.append("D")
        else:
            gradelist.append("Fail")

def printgrade(marks, gradelist):
    i=1
    print("Your Score Card....\n --------------------------------------------------")
    print ("\nSN  Subject    Marks   Grade\n")
    for sub in marks:
        print(i,"    ", sub[0], "   ", sub[1], "    ", gradelist[i-1], "\n")
        i+=1

    print("---------------------------------------------------------------")
    total = 0
    for sub in marks :
        total += sub[1]

    print("Total marks: ", len(marks)*100)
    print("Obtained marks : ", total)
    finalgrademarks = total/len(marks)
    finalgrade = []

    if finalgrademarks > 90 :
        finalgrade.append("A")
    elif finalgrademarks > 70 :
        finalgrade.append("B")
    elif finalgrademarks > 50 :
        finalgrade.append("C")
    elif finalgrademarks > 40 :
        finalgrade.append("D")
    else:
        finalgrade.append("Fail")

    print("Overall grade : ", finalgrade[0] )
    print("----------------------------------------------------------------\n")


print("\nGrading System :-")
print("------------------------------------------------------------------------------------------")
print("\nHey just enter the marks and i will tell the grade in different subjects and also the final grade ...")

print("\nMenu...\n-----")
print(" 1: Add Subject \n 2: Remove subject \n 3: calculate Grades \n 4: Exit \n What you want to do first....")

menuselected = int(input("Select from menu (1/2/3/4) :" ))

marks = []

while True:
    if menuselected == 4 :
        break
    if menuselected == 1 :
        sub = input("\nEnter subject name : ")
        mar = int(input("Enter marks : "))
        marks.append([sub,mar])
        

    elif menuselected == 2 :
        if len(marks) == 0:
            print("Please add subjects first... \n --------------------- \n \n")
        
        
        else:
            print("Avaiblable Subjects : ")
            i = 1
            for sub in marks:
                print(i, ":", sub[0] , ":",sub[1], "\n" )
                i+=1

            removeidx = int(input("Enter Subject number(1/2/3..) : "))
            marks.pop(removeidx-1)
            if len(gradelist) != 0: 
                gradelist.pop[removeidx-1] 
            print("Successfully removed...\n --------------------- \n \n")

            print("Avaiblable Subjects : \n")
            i = 1
            for sub in marks:
                print(i, ":", sub[0] , ":",sub[1], "\n" )
                i+=1
    elif menuselected == 3 :
            calgrade(marks)
            printgrade(marks, gradelist)

     
            

    menuselected = int(input("\nSelect from menu (1/2/3/4) :" ))






