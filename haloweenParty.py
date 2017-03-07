#Challenge Link: https://www.hackerrank.com/challenges/halloween-party
testcase = int(raw_input(""))
for count in range(0,testcase):
    cutting = int(raw_input(""))
    maxcase = (cutting / 2)
    if  cutting % 2 == 0:
        print (maxcase) ** 2
    else:
        print (maxcase)*(maxcase+1)
