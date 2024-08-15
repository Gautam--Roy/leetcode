class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        tens = 0
        fives = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                tens += 1
                fives -= 1
            if bill == 20:
                if tens > 0: 
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0: return False
        return True
result = Solution().lemonadeChange([5,5,5,10,20])
print(result)
            
                    
# date : 15thAugust2024       
 # class Solution:
 #    def lemonadeChange(self, bills: List[int]) -> bool:
 #        tens = 0
 #        fives = 0
 #
 #        for bill in bills:
 #            if bill == 5:
 #                fives += 1
 #            if bill == 10:
 #                tens += 1
 #                fives -= 1
 #            if bill == 20:
 #                if tens > 0: 
 #                    tens -= 1
 #                    fives -= 1
 #                else:
 #                    fives -= 3
 #            if fives < 0: return False
 #        return True       
