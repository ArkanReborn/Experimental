class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        cleaned_s = ' '.join(s.split())
        lst.append(cleaned_s)
        #print(lst)
        for word in lst:
            if word:
                word = word.split()[-1]  # Get the last word
                return len(word)
            # Runtime 12ms beats 74.35% of Python users
            # Memory 11.85 MB beats 81.56% of Python users
                

last = Solution()
print(last.lengthOfLastWord("Hello World"))  # Output: The last word is "World" with length 5
print(last.lengthOfLastWord("   fly me   to   the moon  ")) # Output: The last word is "moon" with length of 4