#Challenge Link: https://www.hackerrank.com/challenges/utopian-tree
height = 1
testcase = int(raw_input(""))
for counttestcase in range(0,testcase):
    cyclenumber = int(raw_input(""))
    for cycle in range(0,cyclenumber):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1
    print height
    height = 1  
