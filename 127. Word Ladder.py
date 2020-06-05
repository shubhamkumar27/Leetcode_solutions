'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        combinations = {}
        for w in wordList:
            for i in range(len(w)):
                permu = w[:i]+'*'+w[i+1:]
                combinations[permu] = combinations.get(permu,[])+[w]
        
        q = deque([[beginWord, 1]])
        visited = set()
        while(len(q)>0):
            node = q.popleft()
            word, level = node[0], node[1]
            visited.add(word)
            for i in range(len(word)):
                p = word[:i]+'*'+word[i+1:]
                if p in combinations:
                    for nextWord in combinations[p]:
                        if nextWord == endWord:
                            return level+1
                        elif nextWord not in visited:
                            q.append([nextWord,level+1])
        return 0
