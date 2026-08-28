class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        results = []
        for i in range(len(nums)):
            choice = nums[i]
            remaining = nums.copy()
            remaining.remove(choice)

            perms = self.permute(remaining)
            for result in perms:
                results.append([choice] + result)
        
        return results
            # return []

        # for choice in nums:
            # identify remaining
            # result = permute(remaining)
            # if result is not None:
                # return [choice] + result
        
        # return None

        


        # permute returns a list of lists


        # Choose — pick one element from what's remaining, add it to your current path
# Explore — recurse with the shrunken remaining list
# Un-choose (backtrack) — remove that element from your path so you can try the next choice in the loop
        # Think about how you would build a list of all possibilities. This problem can be visualized as a tree where each branch represents choosing one of the remaining available numbers.