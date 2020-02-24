'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''

class Solution:
    def getPermutation(self, n, k):
        seq = [p for p in range(1,n+1)]
        fact = self.factorial(n)
        ans = []
        while n>0:
            i = (k-1)//fact[n-1]
            ans.append(seq[i])
            del seq[i]
            k -= i*fact[n-1]
            n-=1
        return ''.join(str(i) for i in ans)
        
    def factorial(self,m):
        fact = [1]
        for i in range(1,m+1):
            fact.append(fact[i-1]*i)
        return fact