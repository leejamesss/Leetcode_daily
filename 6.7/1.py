# https://leetcode.cn/problems/gas-station/submissions/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas, curr_gas, start = 0, 0, 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start = i + 1
                curr_gas = 0

        return start if total_gas >= 0 else -1
