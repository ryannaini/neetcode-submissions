class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; // standard c++ library

        for (size_t i = 0; i < nums.size(); i++) { // size_t makes i and nums.size() or any comparison the same type 
            if (seen.contains(nums[i])) {
                return true;
            }
            seen.insert(nums[i]);
        }
        return false;
    }
};