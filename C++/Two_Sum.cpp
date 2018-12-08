class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;

        for (vector<int>::iterator p = begin(nums); p != end(nums)-1; p++)	{
            vector<int>::iterator j = find(p+1, end(nums), (target - *p));

            // Found
            if (j != end(nums)) {
                result = { p-begin(nums), j-begin(nums) };
                break;
            }
        }
        return result;
    }
};