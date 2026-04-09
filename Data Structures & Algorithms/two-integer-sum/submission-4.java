class Solution {
    public int[] twoSum(int[] nums, int target) {
    for (int j = 0; j < nums.length; j++) {
        for (int i = nums.length-1; i >= 0; i--) {
            if ((nums[i] + nums[j]) == target && i != j) {
                int[] tgt = {j, i};
                return tgt;
            }
        }
    }
        return null;
    }
}
