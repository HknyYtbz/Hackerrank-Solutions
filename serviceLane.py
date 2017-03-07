# Challenge Link: https://www.hackerrank.com/challenges/service-lane
# -*- coding: cp1254 -*-
inp = raw_input()
a = inp.split()
n = int(a[0]) 
t = int(a[1]) 
inp = raw_input() 

width = inp.split() 
for couter in range(t):
    inp = raw_input().split() 
    bas = int(inp[0])
    bit = int(inp[1])
    print min(width[bas:bit+1])
    
