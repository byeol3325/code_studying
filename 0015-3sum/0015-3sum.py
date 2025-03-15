class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answers = set()
        
        nums_dict = Counter(nums)
        
        list_nums_dict = sorted(list(nums_dict.items()))
        
        for i in range(len(list_nums_dict)):
            k1, v1 = list_nums_dict[i]
            for j in range(i+1, len(list_nums_dict)):
                k2, v2 = list_nums_dict[j]
                if (-k1-k2) in nums_dict:
                    if -k1-k2 != k1 and -k1-k2 != k2:
                        answers.add(tuple(sorted([k1, k2, -k1-k2])))
                    elif -k1-k2 == k1 and -k1-k2 != k2 and nums_dict[k1] >= 2:
                        answers.add(tuple(sorted([k1, k1, k2])))
                    elif -k1-k2 == k2 and -k1-k2 != k1 and nums_dict[k2] >= 2:
                        answers.add(tuple(sorted([k1, k2, k2])))
        
        if nums_dict[0] >= 3:
            answers.add((0, 0, 0))
        return list(answers)