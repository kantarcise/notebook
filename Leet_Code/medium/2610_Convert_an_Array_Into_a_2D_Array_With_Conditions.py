"""
You are given an integer array nums. You need to create a 2D 
array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]

Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1

All elements of nums were used, and each row of the 2D array 
contains distinct integers, so it is a valid answer.

It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]

Explanation: All elements of the array are distinct, so we can 
keep all of them in the first row of the 2D array.
 
Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length

Takeaway:

A frequeny map is classic.

Use a list comp for making a matrix

dicts has .keys() .values() and .items()

"""
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # only with elements of nums
        # each row has distinct integers
        # minimum rows
        # we cannot put same value in the same row
        
        map = {}
        for elem in nums:
            if elem not in map:
                map[elem] = 1
            else:
                map[elem] += 1
                
        # we will get the key
        two_d_array_size = max(map, key = map.get) 
        # this is the value
        # print(map[two_d_array_size])
        
        result = [list() for _ in range(map[two_d_array_size])]

        for key, value in map.items():
            for i in range(value):
                result[i].append(key)
        
        return result
