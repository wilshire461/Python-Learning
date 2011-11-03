limit = X
series = range(limit)
for n in xrange(2, int(limit**0.5)+1):
  if series[n]: 
    for i in xrange(n ** 2, limit, n): 
      series[i] = 0
print "Sum = ",sum(series)

