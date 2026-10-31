class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        // Setup of our hashMap
        for (int i = 0; i < nums.length; i++) {
            hashMap.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            Integer complement = target - nums[i]; // Calculate complement (MUST BE MATCHING TYPE FOR COMPARE)
            if (hashMap.containsKey(complement) && hashMap.get(complement) != i)
                return new int[] {i, hashMap.get(complement)};
        }

        return new int[] {};
    }
}
