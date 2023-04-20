from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        perms = permutations(nums)
        for i, perm in enumerate(perms):
            if i+1 == k:
                return ''.join(perm)
