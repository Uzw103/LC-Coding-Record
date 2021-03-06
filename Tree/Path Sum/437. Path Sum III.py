#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
'''
        1. 首先是暴力搜索法，自顶向下
        2. 优化方法是：使用前缀+回溯法 利用字典记录当前路径的合和这个合已出现的频率
        3. 使用一个字典，存放当前遍历路径的sum值作为key，以便当满足target出现在当前路径下时，能将cursum-target作为key在字典中查找，已遍历的sum值中是否存在这个key，
        存在说明这条路径上有能使结点值相加为sum的路径，在counter中+1
        4. 重点就是公式：pastsum + target = cursum。即找到是否存在过去已遍历过的结点sum，再加上target等于现在的cursum。
        5. 暴力搜索时间复杂度n^2: 每个node结点都要判断以它为root的树往下遍历是否有path，寻找树的path又得从左右两棵子树找，因此两层递归
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
        self.path_num = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return self.path_num
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.getPath(root, sum)
        return self.path_num
        
    def getPath(root, sum):
        if not root:
            return 
        if root.val == sum:
            self.path_num += 1
        self.getPath(root.left, sum - root.val)
        self.getPath(root.right, sum - root.val)


​        
​        
    '''使用hashmap存储当前pathsum的key和value，递归一次即可'''
    def __init__(self):
        self.result = 0
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        dic = {0:1} #存储的是当前遍历到的分支的累加和，和这个和出现的次数 这里首先传进去0，1表示当pastsum值为0，也就是遍历到的结点和恰好是sum时，result要加1，否则就错过了
        self.getSumNum(root, 0, sum, dic)
        return self.result
    
    def getSumNum(self, root, cursum, target, dic):
        if not root:
            return
        cursum += root.val
        pastsum = cursum - target
        self.result += dic.get(pastsum, 0) #更新result的值 说明当前总路径内存在一条合等于sum的路径
        dic[cursum] = dic.get(cursum, 0) + 1 #在字典中更新当前的cursum值，以便判断下个结点的加入是否能存在合为sum的路径
        self.getSumNum(root.left, cursum, target, dic)
        self.getSumNum(root.right, cursum, target, dic)
        dic[cursum] -= 1
