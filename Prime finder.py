#Program to find primes starting with 2.

primes = []
def Prime_finder(num):
    primes.append(num)
    w = 0
#Adds primes to array
    while w < len(primes):
        if num % primes[w] == 0 and num != primes[w]:
            primes.remove(num)
            num += 1
            primes.append(num)
            w = -1
        w += 1
    x = input("%d. Press Enter to continue or 'n' to exit. " %(primes[w-1]))      
    if x == "n":
        exit()
    else:
        print(Prime_finder(num+1))
        
Prime_finder(2)
