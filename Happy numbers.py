##Happy Starting with any positive integer,
##replace the number by the sum of the squares of its digits,
##and repeat the process until the number equals 1 (where it will stay),
##or it loops endlessly in a cycle which does not include 1.
##Those numbers for which this process ends in 1 are happy numbers,
##while those that do not end in 1 are unhappy numbers.

def Happy(num1):
    num = num1
    repeat = []
    while True:
        mod = 10
        counter = 1
        calc = []
        digits = len(str(num))
        squares = 0
        while digits >= counter:
            calc.append(int((num % mod)*10/mod))
            num -= calc[counter - 1]
            mod *= 10
            counter += 1
        for x in calc:
            squares += x**2
        if squares == 1:
            return("%d is a happy number" %(num1))
        else:
            for y in repeat:
                if y == squares:
                    return("%d is not a happy number..." %(num1))
            repeat.append(squares)
            num = squares
            
def Happy_ask(num1):
    print(Happy(num1))
    stop = input("Enter 'n' to stop, or anything else to find out if the next number is happy. ")
    if stop == "n":
        exit()
    else:
        print(Happy_ask(num1+1))

num1 = int(input("What number would you like to find out if it's happy? "))
Happy_ask(num1)
