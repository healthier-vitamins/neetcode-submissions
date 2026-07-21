class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            gotten = count.get(num, 0) + 1
            if gotten > 1:
                return True
            count[num] = gotten
        return False
