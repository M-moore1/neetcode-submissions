class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string + "**+**" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = s.split("**+**")
        decoded_strings = decoded_strings[1:]
        return decoded_strings
