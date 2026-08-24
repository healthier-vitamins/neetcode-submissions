class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a = sorted(s)
        # b = sorted(t)
        # return a == b
        
        first = self.countObj(s)
        sec = self.countObj(t)
        print(sec)
        return self.compare(first, sec)

        

    def countObj(self, s: str):
        first = {}
        for i in range(len(s)):
            first[s[i]] = first.get(s[i], 0) + 1
        return first

    def compare(self, x: dict, y: dict):
        if len(x) != len(y):
            return False
        for k, z in x.items():
            if y.get(k, 0) != z:
                return False
        return True
        
            
        
            


