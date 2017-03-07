#Challenge Link: https://www.hackerrank.com/challenges/pangrams
enter = raw_input().lower()
if len(enter) == 1:
    print "not pangram"
    exit(0)
char = "abcdefghijklmnopqrstuxyzvw"
enter = sorted(set(enter),key=enter.index)
enter.sort()
for c in enter:
    if c  not in " ,+'!-*()?[]{}=/%:;.0123456789 ^#" :
        enter += c
    else:
        enter = ""
if len(enter) == len(char):
    print "pangram"
else:
    print "not pangram"
