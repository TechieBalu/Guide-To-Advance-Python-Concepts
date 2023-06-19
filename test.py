# l1 =  [value for value in range(0,5000000)]
# import time

# startTime = time.time()
# l2 = l1[:]
# endTime = time.time()
# print((endTime - startTime))

# # l2[0] =555
# # print(l1)
# # print(l2)

# startTime2 = time.time()
# l3 = l1.copy()
# endTime2 = time.time()
# print((endTime2-startTime2))



def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sums = []
        
        for index, val in enumerate(nums): 
            
            for i in range(index+1,len(nums)):
                sum = 0
                sum = val + nums[i]
                if sum == target:
                    sums.extend([index,i])
                    return sums
                
# print(twoSum(nums = [3,2,3], target = 6))

# print( type(3.96) is float)
import math 

x = math.modf(len([1,2,3,4,5])/2)
print(x)

y = len([1,2,3,4,5])/2
z = int(len([1,2,3])/2)
print('y is: ', y)
yz = y-z
if yz != 0.0:
     print(yz)
     median = math.ceil(y)
     print("median", median)
else:
     print("OK", yz)