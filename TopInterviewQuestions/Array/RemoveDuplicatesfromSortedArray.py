class Solution:
	def removeDuplicates(self, nums) -> int:
		x = 0
		if len(nums) == 0:
			return x

		p = nums[0]
		for i in range(1, len(nums)):
			if p != nums[i]:
				print(p, nums[i])
				x += 1

			p = nums[i]
			nums[x] = nums[i]

		nums = nums[:x + 1]
		print(nums)
		return x + 1

if __name__ == '__main__':
	print('start')
	ex1 = [0,0,1,1,1,2,2,3,3,4]
	ret = Solution().removeDuplicates(ex1)
	print(ret)
	print(ex1)
