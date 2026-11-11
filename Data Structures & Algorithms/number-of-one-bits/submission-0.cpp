class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n != 0) {
            int val = n & 1;
            count += val;
            n = (n >> 1);
        }
        return count;
    }
};
