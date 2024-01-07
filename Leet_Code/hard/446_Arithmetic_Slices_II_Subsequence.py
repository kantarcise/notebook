"""
Given an integer array nums, return the number of all 
the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists 
of at least three elements and if the difference between 
any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by 
removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

Example 1:

Input: nums = [2,4,6,8,10]

Output: 7

Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.

Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1

Takeaway:

For subsets, you can use combinations and chain from itertools

Time limit Exceeded will be waiting for you.

Solution is in DP. Which consists a really special map.

"""

from itertools import combinations, chain

class Solution:
    def numberOfArithmeticSlices_(self, nums: List[int]) -> int:
        # this was cool, but exceeded memory
        
        def all_subsets(collection: list):
            return chain.from_iterable(combinations(collection, n) for n in range(len(collection)+1))
        
        subsets = list(filter(lambda x: len(x)>=3, list(all_subsets(nums))))
        
        result = []
        
        # this did not work
        """
        for elem in subsets:
            for i in range(len(elem) - 1):
                temp = elem[0] - elem[1]
                if elem[i] - elem[i+1] != temp:
                    break
            # difference is same
            result.append(elem)
        """
        # different approach
        
        for elem in subsets:
            temp_diff = elem[0] - elem[1]
            is_arithmetic = all(elem[i] - elem[i + 1] == temp_diff for i in range(len(elem) - 1))
            
            if is_arithmetic:
                result.append(elem)
        
        return len(result)
    
    def numberOfArithmeticSlices__(self, nums: list) -> int:
        # this too, throw a memory limit exception
        
        def is_arithmetic(subset: list) -> bool:
            # Check if the subset is an arithmetic subsequence
            if len(subset) < 3:
                return False

            diff = subset[1] - subset[0]

            for i in range(1, len(subset) - 1):
                if subset[i + 1] - subset[i] != diff:
                    return False

            return True

        result = []

        for r in range(3, len(nums) + 1):
            # Generate all combinations of length r
            for subset in combinations(nums, r):
                if is_arithmetic(subset):
                    result.append(subset)

        return len(result)

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # well well well
        # turns out it is an another dp problem
        total = 0
        n = len(nums)
        
        # a list of dictionaries for every element
        # The dictionary stores the count of arithmetic slices 
        # ending at that element with a specific difference.
        dp = [defaultdict(int) for _ in nums]
        #  dp[i][diff] - number of subsequences ending at i with diff

        for i in range(1, n):
            for j in range(0, i):
                # calc the difference
                diff = nums[j] - nums[i]
                
                # Update the count of slices ending at the 
                # current element i with the specific difference diff. 
                # The count is increased by 1 plus the count of slices 
                # ending at the previous element j with the same difference.
                
                # number of subsequences ending at i with diff
                dp[i][diff] += dp[j][diff] + 1
                
                # Accumulates the total count of arithmetic slices. 
                # This step accounts for slices that can be extended 
                # from the previous elements to the current element.
                total += dp[j][diff]
                
        return total
