# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

def runningSum(nums):
    output =[]
    running_total = 0
    for i in nums:
        running_total += i
        output.append(running_total)
    return output

nums1 = [3,1,2,10,1]
nums2 = [1,1,1,1,1]
nums3 = [1,2,3,4]

print(f"Solution for nums1: {runningSum(nums1)}")
print(f"Solution for nums2: {runningSum(nums2)}")
print(f"Solution for nums3: {runningSum(nums3)}")
