#Challenge Link: https://www.hackerrank.com/challenges/sherlock-and-squares
testcase = int(raw_input())
for i in range (testcase):
    var1, var2 = raw_input().split(' ')
    var1  = int(var1)
    var2 = int(var2)
    while var1 <= var2:
       counter = 0
       root = var1**0.5
       if root == int(root):
           new =int(root)
           while new**2<var2+1:
                new += 1
                counter += 1
           break
       var1 += 1
    print counter
