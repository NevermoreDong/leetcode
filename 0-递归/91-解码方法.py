def solution(s):
	if not s: return 0
	size = len(s)
	# 递归的套路，加一个index控制递归的层次
	def recursive(s, point):
		# 递归的第一步，应该是加终止条件，避免死循环。
		if point == size:
			return 1
		if s[point] == '0': # 以0位开始的数是不存在的
			return 0
		ans1 = recursive(s, point+1)
		ans2 = 0
		if point < size - 1: # 这种情况下后一位point不能去
			if int(s[point:point+2]) <= 26:
				ans2 = recursive(s, point+2) 
		return ans1 + ans2
	return recursive(s, 0)
print(solution("226"))