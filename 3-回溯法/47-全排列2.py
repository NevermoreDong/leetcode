class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, path, nums):
            if len(nums) == 0:
                res.append(path[:])
                return 
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(res, path, nums[:i]+nums[i+1:])
                path.pop()
        res, path = [], []
        dfs(res, path, nums)
        return list(set((tuple(i) for i in res)))   # 利用set去重
        # result = []
        # for i in res:
        #     if i not in result:
        #         result.append(i)      
        # return result

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> re;
        vector<int> used(nums.size(), 0);   

        sort(nums.begin(), nums.end());
        dfs(res, re, used, nums);
        return res;
    }

    void dfs(vector<vector<int>>& res, vector<int>& re, vector<int>& used, vector<int>& nums)
    {
        if(re.size() == nums.size()) {
            res.push_back(re);
            return;
        }
        int r = INT_MAX;
        for(int i = 0; i < nums.size(); i++) {
            if(used[i] == 0) {
                // 针对重复数字漂亮的剪枝，前提是需要排序
                if(nums[i] != r) {
                    r = nums[i];
                    re.push_back(nums[i]);
                    used[i] = 1;

                    dfs(res, re, used, nums);

                    re.pop_back();
                    used[i] = 0;
                }
            }
        }
    }
};