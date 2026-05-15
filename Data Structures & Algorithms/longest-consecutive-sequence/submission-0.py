class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        max_consecutive = 1
        consecutive = 1
        for i in range(len(nums)-1):
            j = i+1
            if nums[j] == nums[i] + 1:
                consecutive += 1
            else:
                consecutive = 1
            max_consecutive = max(max_consecutive, consecutive)
        return max_consecutive