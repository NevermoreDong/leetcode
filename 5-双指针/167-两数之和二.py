class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            rest = target - num
            if rest in numbers[index+1:]:
                rest_index = index + 1 + numbers[index+1:].index(rest)
                return [index+1, rest_index+1]