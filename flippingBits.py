#Challenge Link: https://www.hackerrank.com/challenges/flipping-bits
#Faster solution found, yet this one is the first try.

def makeBinary(number):
    num = ""
    while number > 0 :
        num = str(number % 2) + num
        number = number /2
    return num
def make32bit(flip):
    for i in xrange(32-len(flip)):
        flip = "0" + flip
    return flip
def flipBits(num):
    flip = ""
    num = make32bit(num)
    for i in num:
        if i == "1":
            flip += "0" 
        else:
            flip += "1"
    flip = flip[::-1]
    return flip
def makeDecimal(flip):
    decimal = 0
    for i in xrange(len(flip)):
        decimal += int(flip[i]) * (2**i)
    return decimal

testcase = int(raw_input(""))
for i in xrange(testcase):
    number = int(raw_input(""))
    num    = makeBinary(number)
    flip   = flipBits(num)
    newnum = makeDecimal(flip)
    print newnum
