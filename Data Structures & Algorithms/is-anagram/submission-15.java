class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        HashMap<Character, Integer> sDic = new HashMap<>();
        HashMap<Character, Integer> tDic = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sDic.put(s.charAt(i), sDic.getOrDefault(s.charAt(i), 0) + 1);
            tDic.put(t.charAt(i), tDic.getOrDefault(t.charAt(i), 0) + 1);
        }

        return sDic.equals(tDic);
    }
}
