class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict = {}
        for ch in nums:
            if ch not in dict.keys():
                dict[ch] = 1
            else:
                dict[ch] += 1
        if set(dict.values()) !={1}:
            return True
        else:
            return False
