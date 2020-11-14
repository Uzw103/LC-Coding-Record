#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
'''
        1. 主要用到了分治+递归的思想。
        2. 分情况讨论:
                        1. 首先看题目要求的是什么：要求返回他们的最深的公共父节点 即可判断出 要么p q在左右两个不同分支，要么在同一分支下
                        2. 因此采用分治思想，判断出递归的终止条件是：该分支到头了
                        3. 当当前结点=p或q时，直接停止递归 返回这个root即可 
                        4. 当不=时，分别递归左右子树，哪个子树有返回值就返回那个子树 ，如果两个都有返回值，说明p q分别存在于当前root的左右两边，因此返回当前公共root
‘’‘

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''lowest表示的是最低的，不是 最小的 即越接近两个结点越好'''
        if not root:
            return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q) #寻找左右子树 有无返回值 没有返回值说明p q不在这个分支里 在另一个分支
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
