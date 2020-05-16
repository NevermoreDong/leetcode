class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        queue = {s}
        while True:
            ans = list(filter(isvalid, queue))
            if ans:
                return ans
            next_queue = set()
            for item in queue:
                for i in range(len(item)):
                    if item[i] in "()":
                        next_queue.add(item[:i]+item[i+1:])
            queue = next_queue