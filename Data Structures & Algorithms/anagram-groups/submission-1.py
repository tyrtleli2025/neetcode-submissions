class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            alphabetical = "".join(sorted(word))
            if alphabetical not in anagrams:
                anagrams[alphabetical] = [word]
            else:
                anagrams[alphabetical].append(word)
        
        final = []
        for anagram in anagrams:
            final.append(anagrams[anagram])

        return final