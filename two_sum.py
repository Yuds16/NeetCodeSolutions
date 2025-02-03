'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1, 0, -1):
            if target - nums[i] in nums:
                return [nums.index(target-nums[i]), i]
            
solution = Solution()
print(solution.twoSum([3,4,5,6], 7))
print(solution.twoSum([4,5,6], 10))
print(solution.twoSum([5,5], 10))