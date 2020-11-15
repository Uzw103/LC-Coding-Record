#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
'''
        1. 首先 本题的关键是：找到二叉树结点数最多的一条路径就是找到左右子树的最长路径然后合并在一起就是整体最长的diameter
        2. 因此 通过递归（后序遍历） 找到左右子树的最长长度是多少
        3. 使用一个全局变量保存当前递归得到的左右子树的长度最大值+1（这个+1就是加的根节点）
        4. 和124的模板 套路都是一样的 都是DFS-postorder的套路 只不过函数返回值/全局变量保存值/更新的方式不同
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
        self.diameter = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right + 1) #左右子树的长度相加 再加上根节点就是当前树最长的路径
            return max(left, right) + 1 #函数返回的是当前结点下（包括当前节点），得到的最多结点个数（长度），其实也就是该结点为root的子树的最大长度
        dfs(root)
        return self.diameter
        
            
