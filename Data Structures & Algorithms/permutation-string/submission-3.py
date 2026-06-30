class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)
        for i in range(len(s2) - len(s1) + 1):
            # reset temp and index every iteration
            temp = s1[:]
            temp_index = i
            # while character in s2 is in s1 and temp is not empty
            while temp_index < len(s2) and (s2[temp_index] in temp) and temp:
                # we remove the character from temp 
                temp.pop(temp.index(s2[temp_index]))
                temp_index += 1
            # if temp is empty, then we found a match
            if not temp:
                return True
        return False
