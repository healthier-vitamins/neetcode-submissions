class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort s and t 
        # s == t??
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

