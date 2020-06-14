'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Node:
    def __init__(self):
        self.end = False
        self.child = [None]*26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for ch in word:
            ind = ord(ch)-ord('a')
            if cur.child[ind]==None:
                cur.child[ind] = Node()
            cur = cur.child[ind]
        cur.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for ch in word:
            ind = ord(ch)-ord('a')
            if cur.child[ind]==None:
                return False
            cur = cur.child[ind]
        if cur.end==True:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for ch in prefix:
            ind = ord(ch)-ord('a')
            if cur.child[ind]==None:
                return False
            cur = cur.child[ind]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
