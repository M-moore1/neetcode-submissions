class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        count_dictionary = {}
        for char in s:
            count_dictionary[char] = count_dictionary.get(char, 0) + 1
        for char in t:
            count_dictionary[char] = count_dictionary.get(char, 0) - 1
        
        return all(x == 0 for x in count_dictionary.values())