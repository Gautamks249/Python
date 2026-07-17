from pathlib import Path
from abc import ABC, abstractmethod
import json

#creating database and temperory data
db = "datbase.json"
data = {"students" : [], "teachers" : []}

#reading data from file if avaiblable
if Path(db).exists() :
    try:
        with open(Path(db), "r") as f:
            data = json.load(f)
    finally:
        pass
        

#save function to dump data to json
def save_data(data):
    with open(Path(db), "w") as f:
        json.dump(data, f)


#email validtor function
def email_checker(email):
    return ("@" in email and "." in email)

#phone validator function
def phone_checker(phone):
    return len(phone) == 10

#common class to implement abstraction and common functions
class Manage(ABC):
    @abstractmethod
    def get_details(self):
        name = input("Name : ")
        father = input("Father's Name : ")
        mother = input("Mother's Name : ")
        address = input("Address : ")

        phone = input("Phone Number : ")

        while not phone_checker(phone):
            print("!! INVALID PHONE NUMBER !!")
            phone = input("Phone Number : ")

        email = input("Email : ")

        while not email_checker(email):
            print("!! INVALID EMAIL !!")
            email = input("Email : ")

        return {"Name" : name, "Father's Name" : father, "Mother's Name" : mother, "Address" : address, "Phone Number" : phone, "Email" : email}

    @abstractmethod
    def show_details(self, role, id = False):
        if id:
            if role == "students" :
                for current_data in data[role]:
                    if current_data["Roll number"] == id:
                        print(f"\n{"*"*100}\n")
                        #printing details
                        i = 1
                        for detail in current_data:
                            print(f"{i}. {detail} : {current_data[detail]}")
                            i+=1
                        return

            elif role == "teachers" :
                for current_data in data[role]:
                    if current_data["Employee ID"] == id:
                        print(f"\n{"*"*100}\n")
                        i = 1
                        for detail in current_data:
                            print(f"{i}. {detail} : {current_data[detail]}")
                            i+=1
                        return
            print("no matching detail found")
        else :
            for current_data in data[role]:
                print(f"\n{"*"*100}\n")
                for detail in current_data:
                    print(f"{detail} : {current_data[detail]}")
                

    @abstractmethod
    def edit_details(self, role, id):
        print("-"*100)
        print("\nWhat you want to edit :- ")

        if role == "students" :
            for current_data in data[role]:
                
                if current_data["Roll number"] == id:
                    
                    #printing details
                    i = 1
                    for detail in current_data:
                        print(f"{i}. {detail} : {current_data[detail]}")
                        i+=1

                    #editing
                    detail_list = list(current_data)
                    option = int(input("Please enter (1/2/3...) : "))
                    if option == 9 :
                        student.add_grades()
                        return
                        
                    else :
                        updated_data = input(f"please enter new {detail_list[option-1]} : ")
                        current_data[detail_list[option-1]] = updated_data
                        save_data(data)

                    print("\nDetails updated successfully\n")

                    return

            
        elif current_data["Employee ID"] == id:
            print("*"*100)
            i = 1
            for detail in current_data:
                print(f"{i}. {detail} : {current_data[detail]}")
                i+=1

            #editing
            detail_list = list(current_data)
            option = int(input("Please enter (1/2/3...) : "))
            updated_data = input(f"please enter new {detail_list[option-1]} : ")
            current_data[detail_list[option-1]] = updated_data
            save_data(data)

            print("\nDetails updated successfully\n")

            return



#class for student management
class Students(Manage):
     
    def get_details(self):
        print("\nEnter following Details :- ")
        details = super().get_details()

        #getting additional details
        roll = input("Roll number : ")
        cl = input("Class : ")

        #adding additional details in details dictonary
        details["Roll number"], details["Class"] = roll, cl

        #append details to data
        data["students"].append(details)

        #save data to file
        save_data(data)

        print("\nDetails added successfully\n")
    
    def show_details(self):
        print("\nSelect an option :- ")
        print("\n1.Show all students data \n2.Show details of specific student")
        option = input("Please enter (1/2) : ")

        match option :
            case "1":
                super().show_details("students")
            case "2":
                roll = input("Please enter roll number : ")
                super().show_details("students", roll)
            case _:
                print("\n!! INVALID INPUT !!\n")
    
    def edit_details(self):
        roll = input("Please enter roll number : ")
        super().edit_details("students", roll)

        

    def add_grades(self):
        roll = input("Please enter roll number : ")
        for current_data in data["students"]:
                if current_data["Roll number"] == roll:
                    print(f"\n{"*"*100}\n")
                    #printing details
                    i = 1
                    for detail in current_data:
                        print(f"{i}. {detail} : {current_data[detail]}")
                        i+=1

                    #adding scores
                    print("\nPlease enter marks :-")
                    hindi = input("Hindi : ")
                    eng = input("English : ")
                    maths = input("Maths : ")
                    comp = input("Computer : ")
                    sc = input("Science : ")

                    scores = {"Hindi" : hindi, "English" : eng, "Maths" : maths, "Computer" : comp, "Science" : sc}

                    current_data["Scores"] = scores

                    save_data(data)

                    print("\nScores added successfully\n")

                    return

            
        print("no matching detail found")
    
    def show_result(self):
        def status(marks):
            return "PASS" if int(marks) >= 35 else "FAIL"

        roll = input("Please enter roll number : ")
        try:
            for i in range(len(data["students"])):
                if data["students"][i]["Roll number"] == roll:

                    scores = data["students"][i]["Scores"]

                    print(f"\n{"*"*100}\n")

                    print(f"Name : {data["students"][i]["Name"] :<20} Father's Name : {data["students"][i]["Father's Name"]}")
                    print(f"Roll number : {data["students"][i]["Roll number"] :<15} Mother's Name : {data["students"][i]["Mother's Name"]}")
                    print(f"\n{"-"*100} \n")

                    total_score = 0
                    for sub in scores:            
                        print(f"{sub :<15}{scores[sub] :<10}{status(scores[sub])}")
                        total_score += int(scores[sub])

                    print(f"\n{"-"*100} \n")
                    per = total_score/5
                    print(f"Percentage : {per}%")

                    final_status = status(per)

                    print(f"Result : {final_status}")

                    print(f"\n{"*"*100} \n")
        except :
            print("\n!! Please add scores first !!\n")




#class for teacher management
class Teachers(Manage):

    def get_details(self):
        print("\nEnter following Details :- ")
        details = super().get_details()

        #getting additional details
        emp_id = input("Employee ID : ")
        subject = input("Subject : ")

        #adding additional details in details dictonary
        details["Employee ID"], details["Subject"] = emp_id, subject

        #append details to data
        data["teachers"].append(details)

        #save data to file
        save_data(data)
        
        print("\nDetails added successfully\n")
    
    def show_details(self):
        print("\nSelect an option :- ")
        print("\n1.Show all teachers data \n2.Show details of specific teacher")
        option = input("Please enter (1/2) : ")

        match option :
            case "1":
                super().show_details("teachers")
            case "2":
                emp_id = input("Please enter employee id : ")
                super().show_details("teachers", emp_id)
            case _:
                print("!! INVALID INPUT !!")

    
    def edit_details(self):
        emp_id = input("Please enter employee id : ")
        super().edit_details("teachers", emp_id)


#creating objects for students and teachers
student = Students()
teacher = Teachers()



while True:
    print(f"\n{"-"*100} \n {" "*40} Management System \n{"-"*100}\n")

    print("\nPlease select an option :- ")
    print("1. Add Student / Teacher\n2. Show Students / Teachers Details\n3. Add Grades of Student\n4. Show Result of Student\n5. Edit Details of Student / Teacher\n0. Exit")
        
    option = input("Please Enter (1/2/3/4/5/0) : ")
   

    if option == "0":
        print("\nEXIT SUCCESSFULL\n")
        break

    elif option == "1":
        print(f"\n{"-"*100} \n {" "*40} Add Student / Teacher \n{"-"*100}\n")

        print("\nWhat you want to add :- ")
        print("1. Student\n2. Teacher")

        
        option = input("Please Enter (1/2) : ")
        

        if option == "1" :
            student.get_details() 
        elif option == "2" :
            teacher.get_details()
        else:
            print("\n!! INVALID INPUT !!\n")

    elif option == "2":
        print(f"\n{"-"*100} \n {" "*40} Show Student / Teacher Details \n{"-"*100}\n")

        print("What you want to add :- ")
        print("1. Student\n2. Teacher")

        option = input("Please Enter (1/2) : ")
        
        if option == "1":
            student.show_details() 
            
        elif option == "2":
            teacher.show_details()
        else:
            print("\n!! INVALID INPUT !!\n")

    elif option == "3":
        print(f"\n{"-"*100} \n {" "*40}  Add grades of Student \n{"-"*100}\n")

        student.add_grades()

    elif option == "4":
        print(f"\n{"-"*100} \n {" "*40} Show Result \n{"-"*100}\n")

        student.show_result()

    elif option == "5":
        print(f"\n{"-"*100} \n {" "*40} Edit Details of Student / Teacher \n{"-"*100}\n")

        print("\nWhose details you want to edit :- ")
        print("1. Student\n2. Teacher")
 
        option = input("Please Enter (1/2) : ")
     
        if option == "1" :
            student.edit_details() 
        elif option == "2":
            teacher.edit_details()
        else:
            print("\n!! INVALID INPUT !!\n")
    
    else:
        print("\n!! INVALID INPUT !!\n")
    



