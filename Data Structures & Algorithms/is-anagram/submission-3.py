class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashtable = [0] * 26
        for i in range(len(s)):
            hashtable[ord(s[i]) - ord('a')] += 1
            hashtable[ord(t[i]) - ord('a')] -= 1
        for v in hashtable:
            if v != 0:
                return False
        return True