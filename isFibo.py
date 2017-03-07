#Challenge Link: https://www.hackerrank.com/challenges/is-fibo
testcase = int(raw_input())
for counter in range(0,testcase):
    number = int(raw_input())
    fibo = [0,1]
    zeroth , first = 0 , 1
    while len(fibo) < 100 :
        temp = zeroth + first
        zeroth , first = first , temp
        fibo.append(first)
        fibo.append(temp)
    if number in fibo:
        print "IsFibo"
    else:
        print "IsNotFibo"
