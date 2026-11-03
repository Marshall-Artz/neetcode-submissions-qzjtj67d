class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (Integer num : nums) {
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        hashMap.forEach((key, value) -> {
            freq[value - 1].add(key);
        });

        ArrayList<Integer> result = new ArrayList<>();

        for (int i = freq.length - 1; i > -1; i--) {
            while (!freq[i].isEmpty()) {
                result.add(freq[i].remove(freq[i].size() - 1));

                if (result.size() == k)
                    return result.stream().mapToInt(Integer::intValue).toArray();
            }
        }

        return new int[] {};
    }
}
