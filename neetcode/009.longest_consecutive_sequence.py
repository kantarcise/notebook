"""
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

     Therefore its length is 4.
     
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


Takeaway:

# to get rid of reapparent values, you can use a set,

# imply defining the question in ENGLISH is the first step.

you can override a value in an iteration with 
    
    current = max(current, new)

"""

class Solution:
    
    def longestConsecutive(self, nums) -> int:
        # My first try - it failed because I did not cover the streaks
         
        # in the list, we need to find all the elements
        #  that has the difference of 1 between them
        
        # I can sort the list
        # for each element difference between elements for one 

        if not nums:
            return 0
        consecutive = 1

        sorted_list = sorted(nums)

        for i in range(len(sorted_list)-1):
            if sorted_list[i+1] - sorted_list[i] == 1:
                consecutive +=1

        return consecutive

    def longestConsecutiveSecond(self, nums) -> int:

        nums_set = set(nums)  # Convert the list to a set for faster lookup
        
        longest_streak = 0
        
        for num in nums_set:
            # Check if num is the start of a consecutive subsequence
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Find the length of the consecutive subsequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # override longest_streak for each consecutive subsequence
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    
    prod = Solution()

    print("This is my first approach")
    print("This should be 9: ", prod.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print("This should be 7: ", prod.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
    print("This should be 0: ", prod.longestConsecutive([]))

    print("This is my second approach")
    print("Which works")

    print("This should be 9: ", prod.longestConsecutiveSecond([0,3,7,2,5,8,4,6,0,1]))
    print("This should be 7: ", prod.longestConsecutiveSecond([9,1,4,7,3,-1,0,5,8,-1,6]))
    print("This should be 0: ", prod.longestConsecutiveSecond([]))
