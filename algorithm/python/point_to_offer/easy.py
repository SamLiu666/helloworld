def findRepeatNumber(nums):
	for i, j in enumerate(nums):
		if j in nums[i:]:
			return i

