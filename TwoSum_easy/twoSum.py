def twoSum(nums, target):
	dict = {str(nums[0]): 0}
	for i in range(1,len(nums)):
		if dict.get(str(target - nums[i])) != None:
			return (dict[str(target - nums[i])], i)
		else:
			dict.update({str(nums[i]): i})

print(twoSum([2, 2, 7, 11, 15], 9))