'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

import math
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        recursion(s, 3, 0, [], result)
        return result
        
def recursion(s, dots, index, current, result):
    if dots==0 and index<len(s):
        part = int(s[index:])
        if (part==0 and (len(s)-index)==1) or (0<part<=255 and (len(s)-index)==int(math.log(part,10))+1):
            current.append(s[index:])
            result.append('.'.join(current))
        return
    
    for i in range(index, len(s)):
        part = int(s[index:i+1])
        if (part==0 and (i+1-index)==1) or (0<part<=255 and (i+1-index)==int(math.log(part,10))+1):
            recursion(s, dots-1, i+1, current+[s[index:i+1]], result)
            