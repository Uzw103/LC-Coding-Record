\#

\# @lc app=leetcode id=169 lang=python3

\#

\# *<u>**[169] Majority Element**</u>*

\#

#### ==Methodology：==

1. **摩尔投票法**：<u>适用于众数数量大于数组长度的一半。</u>不断消除不同元素知道没有不同元素 剩下的元素就是众数。counter相+-累加和抵消众数和非众数，最后得到的就是众数
2. **Divide and Conquer：**
   * 不断二分***<递归>***，找到子问题（即每个元素表示为他的众数）
   * **合并子问题** 判断左右序列众数是否相等 不相等就返回左右序列众数出现次数最多的数

\# @lc code=start

```python
'''摩尔投票法'''
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		'''抵消法（摩尔投票法）'''
    counter = 0
    curnum = None
    for num in nums:
        if counter == 0:
            curnum = num
            counter += 1
        elif curnum == num:
            counter += 1
        elif curnum != num:
            counter -= 1
    return curnum
```

```python
'''分治法'''
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
        def findBaseMajority(nums, left, right):
            if left == right:
                return nums[left] #递归终止条件
            mid = (left + right) // 2
            left_maj = findBaseMajority(nums, left, mid) #二分找到base case
            right_maj = findBaseMajority(nums, mid + 1, right)
            if left_maj == right_maj: #判断众数是否相同 不相同则遍历当前切片内元素看看哪边众数出现次数多
                return left_maj
            left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_maj)
            right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_maj)
            return left_maj if left_count > right_count else right_maj
        return findBaseMajority(nums, 0, len(nums) - 1)
```



