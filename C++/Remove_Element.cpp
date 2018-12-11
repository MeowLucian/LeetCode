class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for (auto p = begin(nums); p != end(nums);) {
            if (*p == val)
                p = nums.erase(p);
            else
                p++;
	    }
        return nums.size();
    }
};