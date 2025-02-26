'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        for i in nums:
            total *= i
        
        result = []
        for i in nums:
            result.append(total / i)
        
        return result
    
solution = Solution()
print(solution.productExceptSelf([1,2,4,6])) # [48,24,12,8]
# print(solution.productExceptSelf([-1,0,1,2,3])) # [0,-6,0,0,0]

print([2, 3] * [3, 5])