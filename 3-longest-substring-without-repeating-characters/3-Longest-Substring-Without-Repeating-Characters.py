class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen= set()
        i=0
        maxLength = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            maxLength = max(maxLength, j-i+1)
        return maxLength
        