x = 600851475143
i= 1 

sum_list = []

for i in range(n):
    if not i % 3 or not i % 5:
        sum_list.append(n)
answer = sum(sum_list)

print answer


while(i*i <x):
	if x%i == 0: 
		print 'divisor' ,i
	i = i+1
 
