class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = []
        for num in nums:
            if num not in exists:
                exists.append(num)
            else:
                return True
        
        return False