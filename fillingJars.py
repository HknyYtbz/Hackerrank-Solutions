#Challenge Link: https://www.hackerrank.com/challenges/filling-jars
testcase = raw_input("").split()
n = int(testcase[0])
m = int(testcase[1])
toplam = 0
for i in xrange(m):
    operations = raw_input("").split()
    a = int(operations[0])-1
    b = int(operations[1])-1
    k = int(operations[2])
    toplam += (b-a+1)*k
print toplam/n

