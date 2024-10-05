class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot = skill[0] + skill[-1]  
        chemsum = 0
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] != tot:
                return -1  
            chemsum += skill[i] * skill[-i - 1]
        return chemsum
