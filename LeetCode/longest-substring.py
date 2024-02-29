class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        start = 0
        char_dict = {}
        
        for i in range(len(s)):
            if s[i] in char_dict and start <= char_dict[s[i]]:
                start = char_dict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_dict[s[i]] = i
        return max_length
    # Run Time 30ms beats 84.45% of Python users
    # Memory 12.66 MB. Beats 59.42% of Python users

st = Solution()
print(st.lengthOfLongestSubstring("pwwkew"))
print(st.lengthOfLongestSubstring("dvdf"))