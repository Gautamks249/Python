from pathlib import Path
import os

def create_file():
    print("\n--------------------------------\n          Creating File\n--------------------------------")
    try:
        name = input("\nPleae enter file name : ")
        path = Path(name)
        if path.exists():
            print("\nFile already Exists")
        else:
            with open(path, "w"):
                print("\nFile Created Successfully")
    except Exception as err:
        print(f"\nError : {err}")

def read_file():
    print("\n---------------------------------\n          Reading File\n----------------------------------")
    try:
        name = input("\nEnter file name : ")
        path = Path(name)

        if not path.exists():
            print("\nFile does not Exists")
        else:
            with open(path, "r") as f:
                data = f.read()
                print("\nFile Content :-\n",data)
    except Exception as err:
        print(f"\nError : {err}")

def update_file():
    print("\n--------------------------------\n          Updating File\n---------------------------------")
    try :
        name = input("\nEnter file name : ")
        path = Path(name)

        if not path.exists():
            print("\nFile does not exist")
        else:
            while True:
                print("\nPlease select option :-")
                print("1. Rename File \n2. Append to file \n3. Overwrite file")
            
                try:
                    option = int(input("\nPlease enter (1/2/3) : "))
                except:
                    print("\n !! Invalid Input !! \n")

                if option == 1:
                    try:
                        new_name = input("\nEnter new file name : ")
                        new_path = Path(new_name)

                        if new_path.exists():
                            print("\nFile name already exists")
                        else:
                            path.rename(new_path)
                            print("File rename successfull")
                            break
                    except Exception as err:
                        print(f"\nError : {err}")


                elif option == 2:
                    try:
                        with open(path, "a") as f:
                            new_data = input("\nEnter what you want to append : ")
                            f.write(new_data)
                            print("\nAppend Successfully")
                            break
                    except Exception as err:
                            print(f"\nError : {err}")

                    
                elif option == 3:
                    try :
                        with open(path, "w") as f:
                            new_data = input("\nEnter new content : ")
                            f.write(new_data)
                            print("\nFile Overwritten Successfully")
                            break
                    except Exception as err:
                        print(f"\nError : {err}")

                else:
                    print("\n !! Invalid Input !! \n")
            
            
    except Exception as err:
        print(f"Error : {err}")

def delete_file():
    print("\n---------------------------------\n         Deleting File\n----------------------------------")
    try:
        name = input("\nEnter File name : ")
        path = Path(name)

        if not path.exists() :
            print("\nFile does not exists")
        else:
            os.remove(path)
            print("\nFile deletted successfully")
    except Exception as err:
        print(f"Error : {err}")

print("---------------------------------------\n           CRUD APPLICATION\n---------------------------------------")

while True:
    print("\nSelect Option:--")
    print("1. Create File \n2. Read File \n3. Update File \n4. Delete File \n5. Exit")
    try:
        option = int(input("\nPlease enter (1/2/3/4/5) : "))
    except:
        print("\n!!Invalid Input!!\n")
    
    if option == 1:
        create_file()
    elif option == 2:
        read_file()
    elif option == 3:
        update_file()
    elif option == 4:
        delete_file()
    elif option == 5:
        print("\nExit Successfull.............\n")
        break
    else:
        print("\n!!Invalid Input!!\n")
    