# Binary Tree

#### 分治法

模板

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        left_result = self.preorderTraversal(root.left)
        right_result = self.preorderTraversal(root.right)
        
        return [root.val] + left_result + right_result
```

类似题目整理

1. [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
2. [ #110 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)





#### BFS

模板

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        if root is None:
            return levels
        
        node_list = collections.deque([root])
        
        while len(bfs) > 0:
            levels.append([])
            
            node_list_size = len(node_list)
            for _ in range(node_list_size):
                node = node_list.popleft()
                levels[-1].append(node.val)
                
                if node.left is not None:
                    node_list.append(node.left)
                if node.right is not None:
                    node_list.append(node.right)
        
        return levels
```

类似题目整理

1. [#102 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
2. [ #199 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/)
3. [#107 二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)
4. [#103 二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)
5. 