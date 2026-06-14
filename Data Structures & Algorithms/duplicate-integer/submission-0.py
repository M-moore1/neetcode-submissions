class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracking_set = set()
        for num in nums:
            tracking_set.add(num)
        if len(tracking_set) < len(nums): return True
        return False