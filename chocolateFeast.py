#Challenge Link: https://www.hackerrank.com/challenges/chocolate-feast
T = int(raw_input())
for i in range (0,T):
    mon,pri,dep = [int(x) for x in raw_input().split(' ')]
    numCoke = mon/pri
    garb =tempGarb= numCoke
    while tempGarb >= dep:
    	numCoke += tempGarb/dep
        tempGarb -= dep * (garb/dep)
        tempGarb += garb / dep
        garb = tempGarb

    print numCoke
