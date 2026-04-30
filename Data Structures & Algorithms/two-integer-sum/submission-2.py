class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            rest = target - num

            if rest in seen:
                return [seen[rest], index]
            else:
                seen[num] = index

        