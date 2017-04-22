#String reversal. Takes an input and outputs the reverse.

def StrRev(string):
    rev = list(string)
    d = len(string)
    c = 0
    while c < d:
        b = rev.pop()
        rev.insert(c,b)
        c += 1
    rev = "".join(rev)
    print (rev)
    
string =input("What would you like reversed? ")
StrRev(string)
