'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        curr = ''
        while(n>26):
            if n%26:
                curr = chr((n%26)+64)+curr
                n = n//26
            else:
                curr = 'Z'+curr
                n = (n//26)-1
        curr = chr(n+64)+curr
        return curr

