class Solution:
    def encode(self, strs: List[str]) -> str:
        # ["#Hello", "World", "55"]
        # "5#Hello5#World2#55"
        new_string_parts = []
        for string in strs:
            new_string_parts.append(str(len(string)))
            new_string_parts.append("#")
            new_string_parts.append(string)
        return "".join(new_string_parts)

    def decode(self, s: str) -> List[str]:
        # length = all characters before # 
        # append the next length characters to the decoded list
        # skip to the index after the end of the previous string
        decoded = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j+1+length

        return decoded
