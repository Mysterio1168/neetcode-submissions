class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> seen;
        for (int i : nums){
            if(seen.find(i) == seen.end()){
                seen[i] = 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};