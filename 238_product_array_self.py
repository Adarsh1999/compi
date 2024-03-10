nums = [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    
    output=[]
    
    # prefix loop
    prefix=1
    
    for i in range(len(nums)):
      output.append(prefix)
      prefix= nums[i]*prefix
    
    # postfix loop
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
      output[i]*= postfix
      postfix= nums[i]*postfix

    return output


# couldnt able to solve bymyself the hint was the prefix and postfix loops to calculate multiples of nums beside the number and then multiply them together