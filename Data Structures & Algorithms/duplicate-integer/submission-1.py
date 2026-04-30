class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dublicates = []
        for num in nums:
            if num in dublicates:
                return True
            else:
                dublicates.append(num)
        return False