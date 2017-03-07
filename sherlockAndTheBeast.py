#Challenge Link: https://www.hackerrank.com/challenges/sherlock-and-the-beast
testcase = int(raw_input(""))
for i in xrange(testcase):
    num = ""
    k = 0
    base = int(raw_input(""))
    n = base
    check = False
    while not n <0:
        equation = (5*n) + (3*k)
        if equation % 15 == 0:
            check = True
            break
        else:
            k += 1
            n -= 1
    if check:
        num = (n * "5" )+ (k * "3")
        print num
    else:
        print "-1"

        
    
