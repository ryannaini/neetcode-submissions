class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // First Loop Go over the index and 
        vector<int> res(nums.size(), 1);
        int multiplier = 1;
        for (int i = 0; i < nums.size(); i++) {
            res[i] = multiplier;
            multiplier *= nums[i];
        }
        multiplier = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            res[i] *= multiplier;
            multiplier *= nums[i];
        }
        return res;
    }
};
