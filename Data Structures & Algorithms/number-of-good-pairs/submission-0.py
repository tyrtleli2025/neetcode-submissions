class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = [i]
            else:
                dictionary[nums[i]].append(i)

        print(dictionary)
        numPairings = 0
        for num in dictionary:
            n = len(dictionary[num])
            if n > 1:
                numPairings += (n*(n-1))/2
        
        return int(numPairings)
            