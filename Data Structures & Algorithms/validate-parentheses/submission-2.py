class Solution:
    def isValid(self, s: str) -> bool:
        
        #USE A STACK ITS LIFO

        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in "([{":
                stack.append(char)
            if char in "}])":
                if len(stack) == 0:
                    return False
                if pairs[char] != stack.pop():
                    return False

        if len(stack) != 0:
            return False
        
        return True

        



        
