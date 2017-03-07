#Challenge Link: https://www.hackerrank.com/challenges/game-of-thrones
counter = []
for i in xrange(ord("z")-ord("a")+1):
    counter.append(0)
string = raw_input()
for c in string:
    counter[ord(c)-ord('a')]+=1
oddnum = 0
for c in counter:
	oddnum += c%2

if oddnum >= 2:
	print "NO"
else:
	print "YES"
