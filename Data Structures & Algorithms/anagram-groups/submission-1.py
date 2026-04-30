class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []
        for word in strs:

            sort_word = ''.join(sorted(word))

            if sort_word in anagrams:
                anagrams[sort_word].append(word)
            else:
                anagrams[sort_word] = []
                anagrams[sort_word].append(word)

        for key in anagrams:
            result.append(anagrams[key])
        
        return result