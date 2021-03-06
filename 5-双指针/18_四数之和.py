'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int size = nums.size();
        for (int i = 0; i < size-3; ++i){
            if (i>0 && nums[i]==nums[i-1]) continue;
            for (int j = i+1; j < size-2; ++j){
                if (j>i+1 && nums[j]==nums[j-1]) continue;
                int l = j+1;
                int r = size-1;
                int new_target = target-nums[i]-nums[j];
                while (l<r){
                    if (nums[l]+nums[r]==new_target){
                        res.push_back({nums[i],nums[j],nums[l],nums[r]});
                        ++l;
                        while (l<r && nums[l]==nums[l-1]) ++l;
                    }else if (nums[l]+nums[r]<new_target) {
                        ++l;
                    }else {
                        --r;
                    }
                }
                
            }
        }
        return res;
    }
};