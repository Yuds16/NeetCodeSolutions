'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in t:
            s = s.replace(i, '', 1)

        return len(s) == 0
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for i in strs:
            if len(anagrams.keys()) == 0:
                anagrams[i] = [i]
                continue
                
            valid_anagram = False
            for j in anagrams.keys():
                if self.isAnagram(i, j):
                    anagrams[j].append(i)
                    valid_anagram = True
                    break
                
            if not valid_anagram:
                anagrams[i] = [i]
        return list(anagrams.values())
    
solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(solution.groupAnagrams(["x"])) # [["x"]]
print(solution.groupAnagrams([""])) # [[""]]

print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat","unps"]))