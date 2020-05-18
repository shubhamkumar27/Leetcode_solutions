'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
'''

import math
answer = False
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        global answer
        answer = False
        recursive(num, 0, 0, [])
        return answer
        
        
def recursive(num, index, length, cur):
    global answer
    if len(cur)>=3 and cur[-1] != cur[-2]+cur[-3]:
        return
    
    if len(num)==length and len(cur)>2:
        answer = True
        return
    
    for i in range(index, len(num)):
        number = int(num[index:i+1])
        if (number==0 and (i+1-index)==1) or (number>0 and int(math.log(number, 10))+1==(i+1-index)):
            recursive(num, i+1, length+(i+1-index), cur+[number])
        if answer:
            return

