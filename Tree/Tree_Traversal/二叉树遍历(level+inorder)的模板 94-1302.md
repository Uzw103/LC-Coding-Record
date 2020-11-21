题目有：
 **94 Binary Tree Inorder Traversal**
**144 Binary Tree Preorder Traversal**
**145 Binary Tree Postorder Traversal**
**429 N-ary Tree Level Order Traversal**
**589 N-ary Tree Preorder Traversal**
**590 N-ary Tree Postorder Traversal**
**987 Vertical Order Traversal of a Binary Tree**
==**1302**== **Deepest Leaves Sum** **==+ 104==  Maximum Depth of Binary Tree**——*需要定义一个全局最大深度和sum*

**429 N-ary Tree Level Order Traversal**

**872 Leaf-Similar Trees**

**102+107 Binary Tree Level Order Traversal** 

**965 Univalued Binary Tree**



---

*<u>共同标签：</u>二叉树的==结点遍历==方式*

*二叉树的TreeNode：有**val、left 和 right**三个初始值*

*N叉树是有**.children**作为root的子节点*

---

```python
def preorder(root):
    if not root:
        return []
    '''前序preorder——迭代iteration'''
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res
'''中序inorder——迭代iteration'''
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right
    return res

'''后序遍历postorder——迭代iteration''' #和前序一致，只是res翻转了一下
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res[::-1]
```

'''递归版本'''

```python
res = []
def dfs(root):
    if not root:
        return 
    res.append(root.val)
    dfs(root.left)
    dfs(root.right)
```

> ==注：==
>
> * **使用递归模板时，res必须定义在函数外，**因为递归函数时必须每一次都有返回值，因此需要定义非局部变量来记录res值
>
> * **非递归版本只有一个返回值，就是res，因此可以直接函数内部定义列表来记录值**

'''N叉树的前/后序遍历'''

```python
def preorder(root):
    if not root:
        return[]
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        for child in root.children[::-1]:
            stack.append(child)
        #stack.extend(root.children[::-1])
    return res            

```

'''***二叉树的层级遍历——迭代***'''

```python
def levelorder(root):
    if not root:
        return []
    from collections import deque
    queue, res = deque([root]), []
    while queue:
        level_val = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_val.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_val)
    return res
```

''' 

​    对于二叉树的垂直方向遍历和最深叶子和，
​    都是DFS的递归，只不过要更改递归的结束条件，
​    在新的**dfs函数**中，传递**可变参数、全局变量**，以实现题目的要求
​    认真分析 **题目的本质/可递归的点**是什么 
​    还可以使用**存储元组**的方式得到多个结果
'''

