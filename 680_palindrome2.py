s = "abca"
class Solution:
  def validPalindrome(self, s: str) -> bool:

    l = 0
    r = len(s) - 1
    
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if s[l:r] == s[r:l:-1] or s[l+1:r+1] == s[r:l:-1]:
                # print(True)
                return True
                
            else:
              return False
                # print(False)
                # break
    
#Ye question ka slicing loda bhi samajh nhi aa raha bc vapas dekhna padega