class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            char charFront = Character.toLowerCase(s.charAt(i));
            char charBack  = Character.toLowerCase(s.charAt(j));

            if (!Character.isLetterOrDigit(charFront)) {
                i += 1;
                continue;
            }
            if (!Character.isLetterOrDigit(charBack)) {
                j -= 1;
                continue;
            }

            if (charFront != charBack) {
                return false;
            }
            i += 1;
            j -= 1;
        }

        return true;
    }
}

// s="Was it a car or a cat I saw?"
// int i = 0;
// int j = 26;
// char charFront = w;
// char charBack  = w;

