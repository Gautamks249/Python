import random

com = random.randint(1,100)

hum = -1
while com != hum:
    try :
        hum = int(input("\nGuss the number between 1 to 100 : "))
        if hum >0 and hum < 101: 
            if hum == com:
                print("\nCongratualizations You Won! \n")
            elif hum < com:
                print("\nWrong Guss, Guss a little big number")
            elif hum > com:
                print("\nWrong Guss, Guss a little small number")
    except:
        print("\n \n!!!Enter a valid number between 1 to 100!!! \n")


