class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        longest = 0
        seen = set()

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            longest = max(longest, right - left + 1)
