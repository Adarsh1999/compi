class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
    def sumRange(self, left: int, right: int) -> int:

        output= sum(self.nums[left:right+1])
        return output


#this question we learn more about OOPS in python then the question itself the usage of self.nums 

#the solution is not optmized and we need to optimize it in future mostly my taking the sum of the array