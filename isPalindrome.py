class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #use a stack implementation, 
        
        xString = str(x)
        
        stack = []
        reverse = ''

        for ch in xString:
            stack.append(ch)
        
        for ch in xString:
            reverse += stack.pop()
        
        print(reverse)
    
        if xString == reverse:
            return True 


