'''
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs):
        l = len(strs)
        has = {}
        for i in range(l):
            l = list(strs[i])
            l.sort()
            string = ''.join(l)
            if string in has:
                has[string] += [strs[i]]
            else:
                has[string] = [strs[i]]
        res = []
        for key in has:
            res.append(has[key])
        return res