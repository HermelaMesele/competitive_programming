class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [j for j , k in enumerate(nums) if k == target]    
