"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

# def maxArea(height):
#     max_area = 0
#     area = 0
#     for i in range(0, len(height)-1):
#         for j in range(i+1, len(height)):
#             area = min(height[i], height[j]) * (j - i)
#             if area > max_area:
#                 max_area = area
#     return max_area

def maxArea(height):
    maxArea = 0
    area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        if height[left] <= height[right]:
            area = height[left] * (right - left)
            left += 1
        else:
            area = height[right] * (right - left)
            right -= 1
        if area > maxArea:
            maxArea = area
    return maxArea

# height = [4, 8, 1, 2, 3, 9]
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
