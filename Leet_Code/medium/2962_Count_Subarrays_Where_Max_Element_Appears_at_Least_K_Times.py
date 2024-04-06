"""
You are given an integer array nums and a positive 
integer k.

Return the number of subarrays where the maximum element 
of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements 
within an array.

Example 1:

    Input: nums = [1,3,2,3,3], k = 2
    Output: 6
    Explanation: The subarrays that contain the element 3 at 
      least 2 times are: [1,3,2,3], 
                         [1,3,2,3,3], [3,2,3], [3,2,3,3], 
                         [2,3,3] and [3,3].

Example 2:

    Input: nums = [1,4,2,1], k = 3
    Output: 0
    Explanation: No subarray contains the element 4 at least 3 times.
 
Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    1 <= k <= 10^5

Takeaway:

    Using an index, you can modify something you are not 
    directly traversing in.

    freq counters, hashmaps, classic.

    two pointers, again.

"""
class Solution:
    def countSubarrays(self, nums, k):
        # two pointers
        
        n, left = len(nums), 0 

        # we need to find the max
        max_val = max(nums)
        
        # we will need a freq map 
        count, dict1 = 0, defaultdict(int)

        
        for right in range(n):
            # increment frequency on the fly
            dict1[nums[right]] += 1


            # we have at least k max elements
            while dict1[max_val] > k - 1:
                # If the condition is true, move the left 
                # pointer to the right
                # and decrement the frequency of the element 
                # at the left pointer in the dictionary
                dict1[nums[left]] -= 1

                if dict1[nums[left]] == 0:
                    # if freq becomes 0, delete key
                    del dict1[nums[left]]
    
                left += 1

            # Add the length of the current subarray 
            # to the count variable
            count += right - left + 1

        # Return the total number of subarrays - the number of subarrays
        # where the maximum element appears at least k times
        return (n * (n+1)) // 2 - count
