# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		v = None
		l = None
		r = None

		if t1 is None and t2 is None:
			return None
		if t1 is not None and t2 is None:
			l = t1.left
			r = t1.right
			v = t1.val
		if t1 is None and t2 is not None:
			l = t2.left
			r = t2.right
			v = t2.val
		if t1 is not None and t2 is not None:
			v = t1.val + t2.val
			l = self.mergeTrees(t1.left, t2.left)
			r = self.mergeTrees(t1.right, t2.right)

		ntn = TreeNode(v)
		ntn.left = l
		ntn.right = r

		return ntn

if __name__ == '__main__':
	print('start')

	tl3 = TreeNode(5)
	tl2 = TreeNode(3)
	tl2.left = tl3
	tr2 = TreeNode(2)
	t1 = TreeNode(1)
	t1.left = tl2
	t1.right = tr2

	tt3 = TreeNode(4)
	tt2 = TreeNode(1)
	tt2.right = tt3
	tt5 = TreeNode(7)
	tt4 = TreeNode(3)
	tt4.right = tt5
	tt1 = TreeNode(2)
	tt1.left = tt2
	tt1.right = tt4

	ntn = Solution().mergeTrees(t1, tt1)
	print(vars(ntn))
	print(vars(ntn.left))
	print(vars(ntn.right))
