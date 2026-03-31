class Solution {
    public int getSum(int a, int b) {
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        
        int bits = a ^ b;
        int cars = (a & b) << 1;

        return getSum(bits, cars);
    }
}
