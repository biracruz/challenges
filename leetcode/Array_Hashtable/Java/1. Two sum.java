//https://leetcode.com/submissions/detail/116027272/
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:
// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].


class Solution {
    public int find(int[] nums, int number, int start){
        for(int i = start; i < nums.length; i++){
            if (nums[i] == number)
                return i;
        }
        return -1;
    }
    
    public int[] twoSum(int[] nums, int target) {
        for(int i =0; i < nums.length ; i++){
            int find = target - nums[i];
            int found = find(nums, find, i+1);
            if (found >= 1 ){
                return new int[]{i, found};
            }
        }
        return new int[]{-1,-1};
    }
}