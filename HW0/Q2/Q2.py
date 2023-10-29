#define prime function
def isprime(n):
    if n>1:
        for i in range(2, n-1):
            #loop for search divisors
            if n % i == 0:
                #if find a divisor,the number is not prime
                return False
                break
        else:
            return True
    else:
        #if the number,the number is not prime
        return False
#test function
if(isprime(1)):
    print("1 is prime")
else:
    print("1 is not prime")
if(isprime(37)):
    print("37 is prime")
else:
    print("37 is not prime")
if (isprime(51)):
    print("51 is prime")
else:
    print("51 is not prime")