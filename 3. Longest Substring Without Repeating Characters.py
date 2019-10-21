'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)<1):
            return 0
        max_len = 1
        cur_len = 1
        hashtable = [-1]*256
        hashtable[ord(s[0])]=0
        for i in range(1,len(s)):
            pos = hashtable[ord(s[i])]
            if pos == -1 or i-cur_len>pos:
                cur_len += 1
                hashtable[ord(s[i])] = i
            else:
                if cur_len>max_len:
                    max_len = cur_len
                cur_len = i-pos
            hashtable[ord(s[i])] = i
        if cur_len>max_len:
                    max_len = cur_len
        return max_len