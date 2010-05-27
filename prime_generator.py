prime_iteration = raw_input('Enter the nth prime you wish to calculate:')

prime_iteration = int(prime_iteration)
prime_list = [2]
n = 1

while len(prime_list) < prime_iteration:
    n+=2
    for divisor in range(3,int(n**0.5)+1, 2):
        remainder = n % divisor
        if remainder == 0: break
    else:
        prime_list.append(n)
        

print 'The' + ' ' + str(prime_iteration) + 'th' + ' ' +'prime is:', prime_list[prime_iteration - 1]

