class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
	        return []
        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 
             6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        def dfs(digits, index, path, res, d):
            if index == len(digits):
                res.append(''.join(path))
                return
            digit = int(digits[index])
            for i in d[digit]:
                path.append(i)
                dfs(digits,index+1,path,res,d)
                path.pop()
            
        path = []
        res = []
        dfs(digits, 0, path, res, d)
        return res


class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> d {
            {'0'," "}, {'1', "*"}, {'2', "abc"},
            {'3',"def"}, {'4',"ghi"}, {'5',"jkl"},
            {'6',"mno"}, {'7',"pqrs"},{'8',"tuv"},
            {'9',"wxyz"}
        };



        vector<string> res;
        string path;
        if (digits == "") return res;
        dfs(digits, 0, path, res, d);
        return res;    
    }
        void dfs(string &digits, int index, string path, vector<string> &res, unordered_map<char, string> &d) {
        if (index == digits.size()) {
            res.push_back(path);
            return;
        }
        string digit = d[digits[index]];
        for(char i : digit){
            path += i;
            dfs(digits, index+1, path, res, d);
            path.pop_back();
        }
    }

};