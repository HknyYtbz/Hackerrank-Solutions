#Challenge Link: https://www.hackerrank.com/challenges/manasa-and-stones
def findPossibilty(n, a, b):
    items = []
    step = n - 1
    new = step * a   # a* (n-k) + b * (k-1)
    diff = b-a
    if diff and b > a:
        while new <= step*b:
            items.append(new)
            new += diff
    elif diff and a > b:
        while new >= step * b:
            items.append(new)
            new += diff
    else:
        items.append(new)
    items = sorted(items)
    return items    

testcase = int(raw_input())
for i in xrange(testcase):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    items = findPossibilty(n, a, b)
    out = ""
    for j in items:
        out += str(j)
        out += " "
    print out
    
