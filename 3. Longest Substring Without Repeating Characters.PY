class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = ""
        longest = 0

        for ch in s:
            if ch in current:
                idx = current.index(ch)
                current = current[idx + 1:]

            current += ch
            longest = max(longest , len(current))
        return longest