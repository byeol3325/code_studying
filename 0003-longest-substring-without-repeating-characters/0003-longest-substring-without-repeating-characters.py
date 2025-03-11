class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l, length = 0, 0
        
        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            length = max(length, r - l + 1)
            seen[char] = r
        
        return length