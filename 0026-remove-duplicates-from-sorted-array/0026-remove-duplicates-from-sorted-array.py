class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        DICT_NUM = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] not in DICT_NUM:
                DICT_NUM.add(nums[i])
                nums[k] = nums[i]
                k += 1
        return k