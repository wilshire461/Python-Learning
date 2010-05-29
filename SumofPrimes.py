from math import *
def productOfPrimes(max):
    prime_list=[2]    
    n=1
    while prime_list[-1] <= max:
        n+=2
        for divisor in range(3,int(n**0.5)+1, 2):
	        remainder = n % divisor
	        if remainder == 0: break
	else:
	    prime_list.append(n)
    sumOfPrimes=0
    for prime in prime_list:
        sumOfPrimes+=log(prime)
    print 'Sum of Primes:',sumOfPrimes
    ratio=sumOfPrimes/max
    return ratio    

ratio = productOfPrimes(700)
print 'Ratio:',ratio