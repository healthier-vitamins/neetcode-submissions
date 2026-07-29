class Solution:
    DELIMITER = '#'
    def encode(self, strs: List[str]) -> str:
        final = []
        for s in strs:
            len_str = len(s)
            final.append(f"{len_str}{self.DELIMITER}{s}")
        return "".join(final)
    def decode(self, s: str) -> List[str]:
        print("s", s)
        final = []
        i = 0 
        while i < len(s):
            j= i 
            while s[j] != self.DELIMITER:
                j += 1 
            print(f"s[{i}: {j}]", s[i: j])
            length = int(s[i: j])
            start = j + 1
            word = s[start: start + length]
            final.append(word)
            i = start + length 
        return final 
