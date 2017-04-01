# Program to determine Fibonnacci sequence or a specific number in the sequence

def Fibonacci(count,option):
    num = [0,1,0]
# Returns the sequence
    if option == 1:
        while(num[2]<count):
            print(num[1])
            num[1]=num[1]+num[0]
            num[0]=num[1]-num[0]
            num[2] += 1
        return num[1]
# Returns a specific number
    if option == 2:
        while(num[2]<count):
            num[1]=num[1]+num[0]
            num[0]=num[1]-num[0]
            num[2] += 1
        return num[1]

def Fibonacci_ask():
# Determines what the user wants
    print("This program can give you the sequence of Fibonacci or a specific number. Which would you like?")
    print("Sequence: enter '1' ")
    option = float(input("Specific number: enter '2' "))
    if option == 1:
        count = float(input("What Fibonacci number would you like to go to? "))
        if count %1 !=0:
            print("That number is not an integer, try again.")
            Fibonacci_ask()
        if count <=0:
            print("That number is negative, try again.")
            Fibonacci_ask()
        else:
            print(Fibonacci(count,option))
            x=input("Press Enter to exit")
            exit(Fibonacci_ask)
    if option == 2:
        count = float(input("Which Fibonacci number would you like to see? "))
        if count %1 !=0:
            print("That number is not an integer, try again.")
            Fibonacci_ask()
        if count <=0:
            print("That number is negative, try again.")
            Fibonacci_ask()
        else:
            print(Fibonacci(count,option))
            x=input("Press Enter to exit")
            exit(Fibonacci_ask)
    else:
        print("That's not a valid option")
        Fibonacci_ask()

Fibonacci_ask()
