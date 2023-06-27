"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water 
it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

# Brute force method
def trapBruteForce(height):
    total_area = 0
    max_L = 0
    max_R = 0
    for i in range(0, len(height)):

        max_L = max(height[:i+1])
        max_R = max(height[i:])

        if max_L > 0 and max_R > 0:
            total_area += min(max_L, max_R) - height[i]
            max_R = 0
            max_L = 0

    return total_area


def trap(height):
    total_area = 0
    max_L = 0
    max_R = 0
    left_p = 0
    right_p = len(height) - 1
    while left_p < right_p:
        if height[left_p] <= height[right_p]:
            if height[left_p] > max_L:
                max_L = height[left_p]
                total_area += max_L - height[left_p]
                left_p += 1
            else:
                total_area += max_L - height[left_p]
                left_p += 1
        else:
            if height[right_p] > max_R:
                max_R = height[right_p]
                total_area += max_R - height[right_p]
                right_p -= 1
            else:
                total_area += max_R - height[right_p]
                right_p -= 1
    return total_area


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
# height = [4,2,0,3,2,5]
height = [0,1,2,5,3,2,1,0]

print(trap(height))