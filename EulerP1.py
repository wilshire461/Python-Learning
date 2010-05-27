number_below = raw_input('Enter a number to find the sum of multiples of 3 and 5:')

number_below = int(number_below)

sum_list = []
n=0

for n in range(number_below):
    if not n % 3 or not n % 5:
        sum_list.append(n)
answer = sum(sum_list)

print answer
