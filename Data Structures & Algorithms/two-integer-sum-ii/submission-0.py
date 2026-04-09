class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # [1, 2, 3, 4] target 5 ---
        ## normally, we could compare all the elmts against each other 
        ## using 2 loops -- O(n^2)
        ## left and right pointer
        ## initially, l = start and right = end
        ## add them, compare against the target
        ## if its too small, then we increase the sum by shifting left
        ## if its too big, we can decrease the sum by shifting right

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l+1, r+1]
                
        