class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string_as_word = ""
        for char in s:
            if not char.isalnum():
                continue
            string_as_word += char
        string_as_word = string_as_word.lower()

        if string_as_word == string_as_word[::-1]:
            return True
        
        return False
