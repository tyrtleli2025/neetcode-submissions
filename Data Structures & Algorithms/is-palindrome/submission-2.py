class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"
        cleanList = []
        for c in s.lower():
            if c in dictionary:
                cleanList.append(c)
        cleaned = "".join(cleanList)
        left = 0
        right = len(cleaned)-1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True