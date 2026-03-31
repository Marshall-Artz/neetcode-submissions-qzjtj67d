class Solution {
    public int getSum(int a, int b) {
        int bits = b;
        int cars = a;
        int temp = 0;

        while (cars != 0) {
            temp = bits;
            bits = bits ^ cars;
            cars = (temp & cars) << 1;
        }

        return bits;
    }
}
