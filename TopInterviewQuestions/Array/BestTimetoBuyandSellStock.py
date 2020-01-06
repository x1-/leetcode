class Solution:
	def maxProfit(self, prices) -> int:
		profit = self.search(prices, len(prices), 0, 0, 'n')
		if profit < 0:
			return 0
		return profit

	def search(self, prices, ln, idx, pos, status) -> int:
		if idx >= ln:
			return 0

		max_p = 0
		if status == 'h':
			case_sell = self.search(prices, ln, idx+1, 0, 'n') + (prices[idx] - pos)
			case_hold = self.search(prices, ln, idx+1, pos, 'h')
			max_p = max([case_sell, case_hold])
		if status == 'n':
			case_buy  = self.search(prices, ln, idx+1, prices[idx], 'h')
			case_stay = self.search(prices, ln, idx+1, 0, 'n')
			max_p = max([case_buy, case_stay])

		return max_p

if __name__ == '__main__':
	print('start')
	ps = [7,6,4,3,1]
	print(Solution().maxProfit(ps))
