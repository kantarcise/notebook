# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         freq = {elem: 0 for elem in nums}
#         for elem in nums:
#             freq[elem] = freq.get(elem) + 1
#         return max(freq, key=freq.get)
    
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
