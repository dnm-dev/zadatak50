from FN import fact, prime
import time

start = time.time()

arr = []

s1 = 0
X = 0
count = 0
limit = int(input())

while X<=limit:
	if prime(X)==True:
		s1+=X
		count+=1
		arr.append(X)
		print("{} - {}, {}".format(X,count,s1))
		if s1>1000000:
			break
	X+=1 

arr = arr[::-1]
ind = 0

for i in range(count, 1, -1):
	if prime(s1)==False:
		s1-=arr[ind]
		ind+=1
		
print(s1)

end = time.time()
print(end-start)


