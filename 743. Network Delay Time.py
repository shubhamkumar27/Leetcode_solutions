'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[] for i in range(N+1)]
        
        for edge in times:
            graph[edge[0]].append([edge[1],edge[2]])
            
        distance = [2**31-1]*(N+1)
        distance[K] = 0
        
        minheap = []
        heapq.heappush(minheap, (0,K))
        
        while(len(minheap)):
            v,u = heapq.heappop(minheap)
            
            for neighbor in graph[u]:
                node, dis = neighbor[0], neighbor[1]
                
                if dis+v<distance[node]:
                    heapq.heappush(minheap, (dis+v,node))
                    distance[node] = dis+v
                    
        d = max(distance[1:])
        if d==2**31-1:
            return -1
        else:
            return d
        