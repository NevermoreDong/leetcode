class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(res, path, nums):
            if len(nums) == 0:
                res.append(path[:])
                return 
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(res, path, nums[:i]+nums[i+1:])
                path.pop()
        res = []
        path = []
        dfs(res, path, nums)
        return res

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(res, path, nums);
        return res;
    }
    void dfs(vector<vector<int>>& res, vector<int>& path, vector<int>& nums){
        if(path.size() == nums.size()){
            res.push_back(path);
            return;
        }
        for(int i = 0; i<nums.size(); i++){
            // 返回值是目标元素的下标，找不到时返回值为迭代器结尾
            if(find(path.begin(), path.end(), nums[i]) == path.end()){
                path.push_back(nums[i]);
                dfs(res, path, nums);
                path.pop_back();
            }    
        }
    }
};

