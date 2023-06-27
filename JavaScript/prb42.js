/* 42. Trapping Rain Water
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
0 <= height[i] <= 105 */

const getTrappedRainwaterBruteForce = function (heights) {
    let totalWater = 0;
    for (let i = 0; i < heights.length; i++) {
        let leftI = i, rightI = i, maxLeft = 0, maxRight = 0;
        while (leftI >= 0) {
            maxLeft = Math.max(maxLeft, heights[leftI]);
            leftI--;
        }
        while (rightI < heights.length) {
            maxRight = Math.max(maxRight, heights[rightI]);
            rightI++;
        } 
        const currentWater = Math.min(maxLeft, maxRight) - heights[i];
        if (currentWater >= 0) {
            totalWater += currentWater;
        }
    }
    return totalWater;
}

const trapped = function(height) {
    let totalWater = 0, left_p = 0, right_p = height.length - 1, maxLeft = 0, maxRight = 0;
    while (left_p < right_p){
        if (height[left_p] <= height[right_p]){
            if (height[left_p] > maxLeft) {
                maxLeft = height[left_p];
                left_p++;
            } else {
                totalWater += maxLeft - height[left_p];
                left_p++;
            }
        } else {
            if (height[right_p] > maxRight) {
                maxRight = height[right_p];
                right_p--;
            } else {
                totalWater += maxRight - height[right_p];
                right_p--;
            }
        }
    }
    return totalWater;
}

const height = [0,1,0,2,1,0,1,3,2,1,2,1];
// const height = [4,2,0,3,2,5]
console.log(trapped(height));