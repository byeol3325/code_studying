class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        result = ""
        is_negative = 0
        
        for i in range(n):
            if s[i] == " " and (result == "" and is_negative == 0):
                continue

            if s[i] == "-" and (result == "" and is_negative == 0):
                is_negative = 1
                continue
            
            if s[i] == "+" and (result == "" and is_negative == 0):
                is_negative = -1
                continue
            
            if "0" <= s[i] <= "9":
                result += s[i]
            else:
                break
        
        if result == "":
            return 0
        
        result = int(result)
        if is_negative == 1:
            result *= -1
        
        if result >= 2**31 -1:
            return 2**31 -1
        
        if result <= -2**31:
            return -2**31
        
        return result