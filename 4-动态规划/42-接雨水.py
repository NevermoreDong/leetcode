解法三: 动态规划

我们注意到，解法二中。对于每一列，我们求它左边最高的墙和右边最高的墙，
都是重新遍历一遍所有高度，这里我们可以优化一下。

首先用两个数组，max_left [i] 代表第 i 列左边最高的墙的高度，
max_right[i] 代表第 i 列右边最高的墙的高度。

对于 max_left我们其实可以这样求。

max_left [i] = Max(max_left [i-1],height[i-1])。
它前边的墙的左边的最高高度和它前边的墙的高度选一个较大的，就是当前列左边最高的墙了。

对于 max_right我们可以这样求。

max_right[i] = Max(max_right[i+1],height[i+1]) 。
它后边的墙的右边的最高高度和它后边的墙的高度选一个较大的，就是当前列右边最高的墙了。

class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        l_max = [0]*size
        r_max = [0]*size
        res = 0
        
        for l in range(1, size-1):
            l_max[l] = max(l_max[l-1], height[l-1])
        for r in range(size-2, 0,-1):
            r_max[r] = max(r_max[r+1], height[r+1])
        for i in range(1, size-1):
            min_h = min(l_max[i], r_max[i])
            if height[i] < min_h:
                res += min_h - height[i]
        return res


class Solution {
public:
    int trap(vector<int>& height) {
        int size = height.size();
        int sum = 0;
        for (int i=1; i < size; i++) {
            int l_max=0, r_max=0;
            for (int l=i-1; l>=0; l--) {
                l_max = max(l_max, height[l]);
            }
            for (int r=i+1; r<size; r++) {
                r_max = max(r_max, height[r]);
            }
            int min_h = min(l_max, r_max);
            if (height[i] < min_h) {
                sum += min_h - height[i];
            }
        }
        return sum;    
    }
};