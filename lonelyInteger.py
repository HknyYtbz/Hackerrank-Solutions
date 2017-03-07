#Challenge Link: https://www.hackerrank.com/challenges/lonely-integer
k = input() 
lonely = raw_input().split()
lonely = sorted(lonely)
if len(lonely) != 1:
    k = 0
    while k < len(lonely)-1:
        if lonely[k]== lonely[k+1]:
            k += 2
        else:
            print lonely[k]
            break
    if lonely[k] == lonely[-1]:
        print lonely[-1]
else:
    print lonely[0]
