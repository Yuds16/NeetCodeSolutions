'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

You should aim for a solution with O(m) time and O(1) space for each encode() and decode() call, where m is the sum of lengths of all the strings.
'''
class Solution:
    def encode(self, strs: list[str]) -> str:
        size = len(strs)
        return str(size) + ":" + ":".join(strs)

    def decode(self, s: str) -> list[str]:
        size = int(s.split(":")[0])
        if size == 0:
            return []
        
        decrypted = s.split(":")[1:]
        for i in range(len(decrypted) - 1):
            if len(decrypted[i]) == 0 and len(decrypted[i+1]) == 0:
                decrypted[i] = ":"
                decrypted.pop(i+1)
        return decrypted
    
Solution = Solution()
print(Solution.decode((Solution.encode(["neet","code","love","you"])))) # ["neet","code","love","you"]
print(Solution.decode((Solution.encode(["we","say",":","yes"])))) # ["we","say",":","yes"]
print(Solution.decode((Solution.encode(["we","say",":"])))) # ["we","say",":"]
print(Solution.decode((Solution.encode([])))) # []
print(Solution.decode((Solution.encode([""])))) # [""]