#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
'''
        1. 主要用到递归
        2. 判断函数的返回值是什么：dfs函数返回的是当前子树的最大值，与0比较，小于0则剪枝
        3. 使用max-num全局变量记录每一次递归得到的子树值的最大值，可能为一个结点，也可能为一个路径
        4. 重要的是后序遍历 
'''
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = -1000
        
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(root):
    '''最后dfs返回的是要判断当前子树（加上根节点）是否大于0，如果小于0则把这棵树就剪枝了'''
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.max_sum = max(self.max_num, left + right + root.val)
            return max(0, max(left, right) + root.val)
        dfs(root)
        return self.max_sum
