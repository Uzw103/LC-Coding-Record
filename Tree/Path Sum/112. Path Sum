#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

'''
        1. 本题用DFS(Recursion）或BFS
        2. DFS每次递归的时候减去上一层的结点值 
        3. BFS用两个队列，遍历到叶子结点后开始比对当前sum和目标sum的值 可以用queue的原因是需要每个结点和他对应的sum值同步才行 也就是不能用两个栈做 只能用queue
        4. 用栈也可以，但是栈内保存的是每个结点的元组（结点，结点值）
'''

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''BFS版本'''
        if not root:
            return False
        queue = collections.deque([root])
        queue_val = collections.deque([root.val])
        while queue:
            node = queue.popleft()
            cur_sum = queue_val.popleft()
            if node.left:
                queue.append(node.left)
                queue_val.append(cur_sum + node.left.val)
            if node.right:
                queue.append(node.right)
                queue_val.append(cur_sum + node.right.val)
            if not node.left and not node.right:
                if sum == queue_val:
                    return True
        return False
        
    
    
    '''DFS版本'''
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
