'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

def letterCombinations(digits):
    digits = str(digits)
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = helper(digits,phone)
    # result = ' '.join(res)
    return res

def helper(digits,phone):
    if len(digits)==0:
        return []
    if len(digits)==1:
        return list(phone[digits])
    back = helper(digits[1:],phone)
    front = list(phone[digits[0]])
    res = [f+b for f in front  for b in back]
    return res