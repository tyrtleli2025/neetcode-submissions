class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 1
        longest = 1
        current = 1
        while left < right and right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                current += 1
            else:
                if current > longest: 
                    longest = current
                if left+1 < right:
                    left += 1
                    current -= 1
                else:
                    left += 1
                    right += 1
            if current > longest: 
                    longest = current
        return longest

        # start with 2 pointers at one end of the string
        # advance one pointer until reach a repeat
        # then, advance the other pointer until there is no repeat
        # keep track of the longest substring
        # do this until the right pointer reaches the end of the string, or the left pointer reaches the right pointer 