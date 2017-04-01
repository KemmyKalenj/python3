#Program to find the prime factors of any positive integer

def Prime_finder(num):
    factors = []
    short = int(round(num/2,0))
    z = 0
# Check for negative
    if num < 0:
        return "That's a negative number."
# Determines first prime factor
    for x in range(2, short+1):
        if num % x == 0:
            factors.append(x)
            num1 = int(num / x)
            break
# States the input is prime if no factors are found up to number/2
    if len(factors) == 0:
        return "%d is prime." %(num)
# Checks for additional prime factors      
    while num1 > factors[z]:
        if factors[z] == num1:
            break
        for w in range(factors[z],num1+1):
            if num1 % w == 0 and w != factors[z]:
                factors.append(w)
                z += 1
                num1 = int(num1 / w)
                for y in factors:
                    if w % y == 0 and w != y:
                        
                        z -= 1
                        factors.remove(w)
                        break
    return factors

def Prime_ask():
    num = int(input("What integer would you want the prime factors for? "))
    print(Prime_finder(num))
    
Prime_ask()
