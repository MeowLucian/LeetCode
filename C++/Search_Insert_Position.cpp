class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto p = begin(nums);
        for(; p != end(nums); p++) {
            if (target <= *p) {
                return (p-begin(nums));
                break;
            }
        }
        return (p-begin(nums));
    }
};