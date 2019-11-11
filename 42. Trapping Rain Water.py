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
        front_wall = 0
        back_wall = 0
        front = 0
        back = len(height)-1
        while(front<back):
            if height[front]<height[back]:
                if height[front] >= front_wall:
                    front_wall = height[front]
                else:
                    water += front_wall - height[front]
                front += 1
            else:
                if height[back] >= back_wall:
                    back_wall = height[back]
                else:
                    water += back_wall - height[back]
                back -= 1
        return water