"""
Given an integer array nums, return the length of 
the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Takeaway:

Think about the decision tree as:
can we add the each elemen to the streak or not?

Starting  from backwards, you can calculate the result
depending on the value of adjacents.

"""
class Solution:
    def lengthOfLIS_(self, nums: list[int]) -> int:
        # brute force
        # did not work
        
        # for every element, check every streak 
        # o(n^2)
        final = []
        # [10,9,2,5,3,7,101,18]
        for i in range(len(nums)-1):
            streak = 1
            temp = nums[i]
            print(temp, "aaa")
            for j in range(i + 1, len(nums)-1):
                if nums[j] > temp:
                    streak += 1
                    temp = nums[j]
            final.append(streak)
            print(f"for {temp}, final  is {final}")
        
        return final
    
    
    def lengthOfLIS(self, nums: list[int]) -> int:
        # from a homie
        if not nums:
            return 0

        n = len(nums)
        # Initialize an array to store the length of LIS ending at each index
        dp = [1] * n

        # Iterate over the array from the second element onward
        for i in range(1, n):
            for j in range(i):
                # Check if the current element can be included in the LIS
                if nums[i] > nums[j]:
                    # Update the length of LIS ending at index i
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in the dp array represents the length of the overall LIS
        return max(dp)
    
        
    def lengthOfLIS(self, nums: list[int]) -> int:
        # neet
        # we start from last value and work to start
        # o(n^2)

        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] =  max(lis[i], 1 + lis[j])
        return max(lis)
