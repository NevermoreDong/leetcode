class Solution:
    def minWindow(self, s: str, t: str) -> str:
            size = len(s)
            res = ''
            left, right = 0, 0
            need, window = {}, {}   # 需要凑齐的数，「窗口」中的相应字符的出现次数
            for c in t:
                need[c] = need.get(c, 0) + 1
            match, all_match = 0, len(need) # 当前匹配到的字符数，所有需要匹配的字符数
            min_window_length = size        # 包含所有字符的最小串的长度


            while right< size:
                if s[right] in need:
                    window[s[right]] = window.get(s[right], 0) + 1
                    if window[s[right]] == need[s[right]]:      # 通过移动右指针，使窗口有所有需要字符
                        match += 1                              # 每匹配到到一个字符，当前匹配字符数加一
                    while match == all_match:                   # 相等时，窗口里有所有匹配到的字符，下面移动左指针
                        now_window_length = right - left        # 此时窗口串的长度
                        if now_window_length < min_window_length:         # 如果最小窗口长度大于此时窗口长度
                            res = s[left:right + 1]             # 进行记录和更新
                            min_window_length = now_window_length

                        if s[left] in need:                         # 移动左窗口
                            window[s[left]] = window[s[left]] - 1   # 减少窗口里的字符统计
                            if window[s[left]] < need[s[left]]:     # 当窗口里的字符统计数小于所需要的字符统计数时
                                match -= 1                          # 减少一个匹配数
                        left += 1
                right += 1
            return res
