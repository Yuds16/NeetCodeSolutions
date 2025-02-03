'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in t:
            print(i, s)
            s = s.replace(i, '', 1)

        return len(s) == 0
    
solution = Solution()
solution.isAnagram("racecar", "carrace")