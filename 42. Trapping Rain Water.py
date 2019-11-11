'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
6 units of rain water (blue section) are being trapped.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height):
        water = 0
        maxfh = height[0]
        maxbh = height[-1]
        f = 0
        b = len(height)-1
        while(f<b):
            if height[f+1]<maxfh:
                d = maxfh-height[f+1]
                water += d
                f += 1
            else:
                maxfh = height[f+1]
                f += 1
            if height[b-1]<maxbh:
                d = maxbh-height[b-1]
                water += d
                b -= 1
            else:
                maxbh = height[b-1]
                b -= 1
            #print(water,f,b)
        print(water)