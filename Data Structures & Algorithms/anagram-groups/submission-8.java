class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<List<Integer>, List<String>> hashMap = new HashMap<>();

        for (String str : strs) {
            List<Integer> list = new ArrayList<>(Collections.nCopies(26, 0));

            for (char chr : str.toCharArray()) {
                int index = chr - 'a';
                list.set(index, list.get(index) + 1);
            }

            hashMap.computeIfAbsent(list, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(hashMap.values());
    }
}
