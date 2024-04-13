"""
Q: Given an integer array nums, return all the 
triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

    The distinct triplets are [-1,0,1] and [-1,-1,2].

    Notice that the order of the output and the order of the 
    triplets does not matter.

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
    -10^5 <= nums[i] <= 10^5

Takeaway:

    Two pointer approach is simple. you define 
        them and you set up conditions on their changes.

    Updating a sequence on the fly is NOT HELPFUL so far.

    Defining the object which you are thinking to 
        return is a good and simple idea.

"""

class Solution:
    
    def threeSum(self, nums):
        # sort the input list for 
        # easier handle on duplicates
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # skip duplicate values
                continue

            ## two pointers just like two sum
            left , right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # found a candidate!
                    triplets.append([nums[i], nums[left] , nums[right]])
                    
                    # skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1
                    
                    # move pointers
                    left +=1
                    right -=1
                elif total<0:
                    # move up the left pointer to increase total
                    left += 1
                else:
                    # move down the right to decrease the total
                    right -=1

        return triplets   

    def threeSum_(self, nums):
        # this is pretty cool

        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                # skip duplicates
                continue

            # two pointers for each selection of i
            l, r  = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    # move down r
                    r -= 1
                elif three_sum < 0:
                    # move up l
                    l += 1
                else:
                    # found a candidate!
                    res.append([a, nums[l], nums[r]])
                    # move the left pointer
                    l += 1
                    # if there are duplicates
                    while nums[l] == nums[l-1] and l < r:
                        # move l further
                        l += 1
        
        return res

sol = Solution()
    
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 1, 1]))
print(sol.threeSum([0, 0, 0]))
   
print(sol.threeSum_([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum_([0, 1, 1]))
print(sol.threeSum_([0, 0, 0]))
