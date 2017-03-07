#Challenge Link: https://www.hackerrank.com/challenges/alternating-characters
testcase = int(raw_input())
for count in range(testcase):
    inp = raw_input().upper()
    counter = 0
    inp = list(inp)

    for i in range(0, len(inp)-1):
        if inp[i] == inp[i+1]:
            counter +=1
    print counter
       
