"""
Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if 
every element is distinct.

Example 1:

    Input: nums = [1,2,3,1]
    Output: true

Example 2:

    Input: nums = [1,2,3,4]
    Output: false

Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Takeaway:

    You can use sets or you can use a dictionary
    
    You can see the max valued dict by: max(dict.items()) 
    
    CAREFUL - max (dict , key=dict.get()) WILL GIVE YOU THE KEY not the VALUE
    
    You can use Greedy approach in the loop to exit faster.
    
    sets have add() and remove() methods

"""

class Solution:

    def containsDuplicate__(self, nums) -> bool:
        # my first solution
        freq = {elem : 0 for elem in nums}
        for elem in nums:
            freq[elem] += 1
        max_occurance = max(freq.values())
        return max_occurance > 1
 
    def containsDuplicate_(self, nums) -> bool:
        # another one would be
        freq = {elem : 0 for elem in nums}
        for elem in nums:
            freq[elem] += 1
            if freq[elem] > 1:
                return True
        return False

    def containsDuplicate(self, nums)-> bool:
        # sets are really helpful too.
        hset = set()
        
        for elem in nums:
            if elem in hset:
                return True
            else:
                hset.add(elem)

        return False 


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4]))
    print(sol.containsDuplicate([1,2,3,4,3]))
    print(sol.containsDuplicate_([1,2,3,4]))
    print(sol.containsDuplicate_([1,2,3,4,3]))
    print(sol.containsDuplicate__([1,2,3,4]))
    print(sol.containsDuplicate__([1,2,3,4,3]))
