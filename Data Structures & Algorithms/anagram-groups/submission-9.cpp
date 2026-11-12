class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dictionary;
        // Loop Through every string in the vector then sort it and add it to a hashmap
        for (const string& s : strs) { // We won't copy that 
            string key = s;
            sort(key.begin(), key.end()); // sort the copy
            // C++ Automatically creates an empty vector if it does not exist
            dictionary[key].push_back(s);
        }
        vector<vector<string>> res;
        for (auto& pairs : dictionary) {
            res.push_back(pairs.second);
        }

        return res;
    }
};
