"""
Given an integer array nums, return the maximum result 
of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

    Input: nums = [3,10,5,25,2,8]
    
    Output: 28
    
    Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

    Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    
    Output: 127

Constraints:

    1 <= nums.length <= 2 * 10^5

    0 <= nums[i] <= 2^31 - 1

Takeaway:

    `<< 1` is multiplying by 2

    `>> 1` is floor division by 2

    max xor will happen, on biggest numbers
    
    and on most different numbers

    bin() for binary representations
    
"""

class Solution:
    def findMaximumXOR__(self, nums: list[int]) -> int:
        # brute force
        # o(n^2) - time limit exceeeded
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i, n):
                result = max(result, nums[i] ^ nums[j])
        return result
    

    def findMaximumXOR_(self, nums: list[int]) -> int:
        # works 
        
        # Find the maximum length of the binary 
        # representation of the max number in nums.
        L = len(bin(max(nums))) - 2
        
        maxXor = 0
        
        # Start with the leftmost bit (MSB) 
        # and iterate through all the numbers in nums.
        for i in range(L)[::-1]:
            
            maxXor <<= 1
            
            currentXor = maxXor | 1
            
            # For each bit position i, make a prefix_set 
            # that stores the prefixes of length i 
            # for each number in nums.
            prefixSet = {num >> i for num in nums}
            
            for prefix in prefixSet:
                # for each number in nums, check if the XOR 
                # of its prefix with any prefix in 
                # prefix_set results in a number in nums
                if currentXor ^ prefix in prefixSet:
                    # If it does, update the XOR result 
                    # and continue to the next bit position.
                    maxXor |= 1
                    break
        return maxXor
    
    def findMaximumXOR(self, nums: list[int]) -> int:
        result = 0

        # Iterate through the bits of the 
        # numbers from MSB to LSB. 
        for i in range(32)[::-1]:

            # This is done to make room for the 
            # new bit we're about to add.
            result <<= 1 # (multiply by two)

            # This is done to get the 
            # first (32 - i) bits of each number.
            prefixes = {num >> i for num in nums} 

            result += any((result + 1) ^ p in prefixes for p in prefixes)
        
        return result
    

sol = Solution()
print(sol.findMaximumXOR([3,10,5,25,2,8]))
print(sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
