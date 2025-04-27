print("Hello, World!")
answer = input("Are you ready to play? ")

if answer == "yes":
    print("Let's start the escape room!")
    code = input("What is the code to unlock the door? ")
    if code == "58967":
        print("You are correct!")
        
    else:
        print("You are incorrect! if you want to play again, please answer yes if not, please answer no")
        if answer == "yes":
            code = input("What is the code to unlock the door? ")
    if code == "58967":
        print("You are correct!")
    else:
        print("You are incorrect! if you want to play again, please answer yes if not, please answer no")
        if answer == "yes":
            code = input("What is the code to unlock the door? ")
            if code == "58967":
                print("You are correct!")
            else:
                print("You are incorrect! you will now be eliminated")
        code = input("What is the code to unlock the safe? ")
        if code == "123458768":
            print("You are correct!")
        else:
            print("You are incorrect! if you want to play again, please answer yes if not, please answer no")
            if answer == "yes": 
                code = input("What is the code to unlock the safe? ")
        if code == "123458768":
            print("You are correct!")
        else:
            print("You are incorrect! if you want to play again, please answer yes if not, please answer no")
            if answer == "yes":code = input("What is the code to unlock the safe? ")
        if code == "123458768":
            print("You are correct!")
        else:
            print("You are incorrect! you will now be eliminated")    
            code = input("What is the code to open the window? ")
            if code == "333":
                print("You are correct!")
                code = input("What is the code to open the box? ")
                if code == "777":
                    print("You are correct!")
            if answer == "no":
                print("Thank you for playing!")
if answer == "no":
    print("Thank you for playing!")
if answer == "no":
    print("Thank you for playing!")
if answer == "no":
    print("Thank you for playing!")
