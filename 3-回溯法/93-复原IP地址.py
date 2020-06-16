class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid_path(path):
            # path_list_int = list(map(int, path))
            # path_list_str = list(map(str, path_list_int))
            path_list_str = list(map(str, map(int, path)))

            path_int = ''.join(path_list_str)
            return True if path_int == s else False

        def dfs(path, path_length, deep):
            if deep == 4:
                # 判断path是否有效，看长度
                # 然后处理下path
                if is_valid_path(path):
                    res.append('.'.join(path[:]))
                    return
                return
            for i in ([1, 2, 3]):
                # 确保加到path里面的数是有效的
                get_num = s[path_length:path_length+i]
                cur_path_length = path_length + i
                if get_num == '': continue
                if 0 <= int(get_num) <= 255:
                    path.append(get_num)
                    dfs(path, cur_path_length, deep + 1)
                    path.pop()

        res = []
        dfs([], 0, 0)
        return list(set(res))