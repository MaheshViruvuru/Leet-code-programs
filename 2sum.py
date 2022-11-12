class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            sam_list = nums.copy()
            sam_list.pop(i)
            for j in range(len(sam_list)):
                k = nums[i] + sam_list[j]
                if k == target:
                    if nums[i] == sam_list[j]:
                        List = [i, nums.index(sam_list[j], i+1)]
                        return List
                    else:
                        List = [i, nums.index(sam_list[j])]
                        return List
