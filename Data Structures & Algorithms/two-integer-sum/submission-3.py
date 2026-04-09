class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in storage:
                return [storage[difference], index]
            else:
                storage[value] = index

        ## storage: 6: index 1
        ## storage: 5: index 2
        ## [1, 3]