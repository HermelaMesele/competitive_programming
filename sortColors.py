class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while(n>1):
            n-=1
            
            for i in range(len(nums)-1):
               if(nums[i] > nums[i+1]):
               
                   tmp = nums[i]
                   nums[i] = nums[i+1]
                   nums[i+1] = tmp
         
