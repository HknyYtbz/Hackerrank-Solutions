#Challenge Link: https://www.hackerrank.com/challenges/restaurant/submissions
# Enter your code here. Read input from STDIN. Print output to STDOUT
def gcd(l,b):
    while b:
        l, b = b, l%b
    return l 

for i in xrange(int(raw_input(""))):
    sze = raw_input().split()
    l = int(sze[0])
    b = int(sze[1])
    comdv = gcd(l,b)
    maxim = l * b
    result = (maxim)/(comdv**2)
    print result
