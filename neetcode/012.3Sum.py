"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


Takeaway:

- Two pointer approach is simple. you define them and you set up 
conditions on their changes.

- Updating a sequence on the fly is NOT HELPFUL so far.

- defining the object which you are thinking to return is a good and simple idea.


"""

# TODO
class Solution:
    # first attempt to solve the problem
    def three_sum(self, nums):
        # sum of two elements is the negative to the other
        
        for i in range(len(nums)):
            to_be_countered_index , to_be_countered =  i , nums[i] 
            sliced_nums = nums.remove(to_be_countered)
            for j in range(len(sliced_nums)-1):
                for k in range(1,len(sliced_nums)):
                    if sliced_nums[j] + sliced_nums[k] == to_be_countered * (-1):
                        return [sliced_nums[j], sliced_nums[k], nums[to_be_countered_index]]

    """Your approach is a good start, but there are some issues with
     your code:

    sliced_nums is assigned the result of nums.remove(to_be_countered),
     but remove() does not return the list with the element removed; it
      modifies the list in place and returns None. You should make
       a copy of nums and then remove the element from the copy.

    Your current code only attempts to find one triplet that sums to zero.
     However, the problem statement asks you to find all such triplets.
      You should collect all the valid triplets in a list and return that list.

    To avoid duplicate triplets, you should sort the input list nums first and
     then use two pointers approach to find the triplets. This approach will
      help you skip duplicates efficiently.

    """

    def threeSum(self, nums):
        # sort the input list for easier handle on duplicates
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # skip duplicate values
                continue

            ## tow pointer just like two sum
            left , right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left] , nums[right]])
                    # skip duplicates of nums[left] == nums[left + 1]
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1
                    left +=1
                    right -=1
                elif total<0:
                    left += 1
                else:
                    right -=1
        return triplets        

    
    # this is pretty cool
    def threeSumSolid(self, nums):
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            # two pointers
            l, r  = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # move the left pointer
                    l += 1
                    # if there are duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

if __name__ == '__main__':  
    sol = Solution()
    
    # issues with this solution
    # print(sol.three_sum([-1, 0, 1, 2, -1, -4]))
    # print(sol.three_sum([0, 1, 1]))
    # print(sol.three_sum([0, 0, 0]))
    
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([0, 1, 1]))
    print(sol.threeSum([0, 0, 0]))

    
    print(sol.threeSumSolid([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSumSolid([0, 1, 1]))
    print(sol.threeSumSolid([0, 0, 0]))