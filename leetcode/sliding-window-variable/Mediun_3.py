class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = set()
        max_ss = 0

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            max_ss = max(max_ss, end - start + 1)

        return max_ss