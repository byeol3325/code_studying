class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        # PAYPALISHIRING numRows 3 => 0 4 8 12 1 3 5 7 9 11 13 2 6 10
        # PAYPALISHIRING numRows 4 => 0 6 12 (1 5 7 11 13) (2 4 8 10) 3 9
        # 0 + (numRows-1)*2 * n 
        # 1 + sum (numRows + (-1)**(i))
        # 2 + sum (numRows + (-1)**(i-1))
        # total (numRows-1)*2 
        #       (numRows-1) 
        # 0 1 2 3 => 0/6    1/42  2 /24   3/6
        n = len(s)
        result = ""
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                for j in range(i, n, (numRows-1)*2):
                    result += s[j]
                    #print(s[j], end=" ")
            else:
                now = i
                if now >= n:
                    break
                result += s[now]
                #print(s[now], end="")
                nums = [(numRows-1-i)*2, i*2]
                for j in range(n):
                    now += nums[j%2]
                    if now >= n:
                        break
                    #print(result, now)
                    result += s[now]
                    #print(s[now], end= " ")
        return result
