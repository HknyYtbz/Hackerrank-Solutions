#Challenge Link: https://www.hackerrank.com/challenges/angry-children
n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
dif = []
temp = []
counter = 0
for i in range(len(candies)-(k-1)):
    fark = candies[i+(k-1)]-candies[i]
    dif.append(fark)
dif.sort()
#for i in range(0,k/2): # /2
for i in range(0,len(dif)):
    a = dif[i]
    temp.append(a)
print min(temp)
