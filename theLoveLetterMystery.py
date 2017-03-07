#Challenge Link: https://www.hackerrank.com/challenges/the-love-letter-mystery
list1 = []
list2 = []
testcase = int(raw_input())
for i in  range(testcase):
    string = raw_input()
    for i in xrange(len(string)/2):
        list1.append(string[i])
    string = string[::-1]
    n = 0
    for i in xrange(len(string)/2):
        list2.append(string[i])
    for j in range(len(string)/2):
        if list1 != list2:
            n += abs(ord(list1[j])-ord(list2[j]))
    print n
    list1 = []
    list2 = []
