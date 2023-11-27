"""
You are given a 0-indexed array of positive integers nums 
and a positive integer limit.

In one operation, you can choose any two indices i and j and 
swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained 
by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the 
first position where a and b differ, array a has an element that is 
less than the corresponding element in b. For example, the array [2,10,3] is 
lexicographically smaller than the array [10,2,3] because they differ 
at index 0 and 2 < 10.

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.

Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can 
obtain because we cannot apply the operation on any two indices.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109

Takeaway:

The numbers is nums can be separated into different disjoint sets. 
        
For each nums[i] in nums, result[i] will be the minimum of 
the disjoint set to which nums[i] belongs.

With usage of limit, form the deque groups

After, usa a hashmap to map all elements to groups

pop 1 by 1 from sorted groups

"""

from collections import deque

class Solution:
    def lexicographicallySmallestArray_(self, nums: List[int], limit: int) -> List[int]:
        # this was a fight, first try
        # could not make it work in time.
        
        # find all differences
        # if under limit, start swapping
        
        # Input: nums = [1,5,3,9,8], limit = 2
        # Output: [1,3,5,8,9]
        # difflist = [4, 2, 6,]
        
        # try to get the lowest value to the as front as possible
        temp = nums[:] 
        nums.sort()
        
        for i in range(len(nums) - 1):
            if abs(nums[i] - temp[i]) <= limit:
                pass
            else:
                nums[i] = temp[i]
                
        return nums
    
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        # from a homie
        
        # Intuition
        # The numbers is nums can be separated into different disjoint sets. 
        
        # For each nums[i] in nums, result[i] will be the minimum of 
        
        # the disjoint set to which nums[i] belongs.
        
        # Approach
        
        # Sort nums.
        
        # From sorted_nums find the disjoint sets, here sorted_groups.
        
        # Give a common parent to the numbers in a disjoint set, here index 
        # i of each sorted_group in sorted_groups.
        
        # Pop the minimum element of sorted_group to which nums[i] belongs and append to result.

        # time complexity is o(nlogn)
        
        n = len(nums)
        
        sorted_nums = sorted(nums)
        print("sorted", sorted_nums)
        sorted_groups = [deque([sorted_nums[0]])]
        # print("sorted groups", sorted_groups)
        # sorted groups [deque([1])]

        for i in range(1, n):
            # if the element in list has the 
            # smaller difference than limit in current group last element
            if sorted_nums[i] - sorted_groups[-1][-1] <= limit:
                sorted_groups[-1].append(sorted_nums[i])
            else:
                # exceeded limit
                sorted_groups.append(deque([sorted_nums[i]]))
        
        print("sorted groups", sorted_groups)
        # sorted groups [deque([1, 3, 5]), deque([8, 9])]

        # map all elements to groups
        d = {}
        for i, sorted_group in enumerate(sorted_groups):
            for num in sorted_group:
                d[num] = i

        # just grouping
        # print(d)
        # {1: 0, 3: 0, 5: 0, 8: 1, 9: 1}


        # pop results with using deque
        result = []
        for num in nums:
            # the group number from the hash map
            result.append(sorted_groups[d[num]].popleft())
        return result
    
sol = Solution()

print(sol.lexicographicallySmallestArray([1,5,3,9,8], 2))
