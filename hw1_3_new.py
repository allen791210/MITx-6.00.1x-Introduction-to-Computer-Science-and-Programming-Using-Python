# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:59:58 2017

@author: user
"""


#def longest_alp(s):
s ='azcbobobegghakl'    
   
count = 1
longest = 0
    
for i in range(len(s)-1):
    idx = i
    while s[idx] <= s[idx+1]:
        count += 1
        idx += 1
        if (idx+1) >= len(s):
            break
    if count > longest:
        longest = count
        res = s[i:(i+count)]
    count = 1

print("Longest substring in alphabetical order is: {0}".format(res))
    

#longest_alp(s)