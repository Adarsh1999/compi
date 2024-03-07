nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
  
    length=len(nums)
    
    num_set= (set(nums))
    all_nums= set([i+1 for i in range(len(nums)) ])
    return(list(all_nums-num_set))



#set magic used differnce between 2 numbers