class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        top_k = []
        for i in range(k):
            most_frequent = max(frequencies, key=frequencies.get)
            top_k.append(most_frequent)
            del frequencies[most_frequent]

        return top_k