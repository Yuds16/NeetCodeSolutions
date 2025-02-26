'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
'''

'''
This is most likely greater than O(n) space since I had to setup a new storage
Python makes use of Timsort for its sorting algorithm (https://en.wikipedia.org/wiki/Timsort), it has the time complexity of O(n log n) which is the worst case as well for this algorithm
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for i in nums:
            if i not in counter.keys():
                counter[i] = 1
            else:
                counter[i] += 1
                
        sorted_count = sorted(counter.items(), key=lambda item : item[1])[::-1]
        return [sorted_count[x][0] for x in range(k)]
        
    
solution = Solution()
print(solution.topKFrequent(nums = [1,2,2,3,3,3], k = 2)) # [2,3]
print(solution.topKFrequent(nums = [7,7], k = 1)) # [7]
print(solution.topKFrequent(nums = [1,1,1,1,2,2,2,7], k = 2)) # [1,2]