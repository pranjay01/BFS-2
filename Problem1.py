#Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity -> On
# Space complexity -> On
# Logic -> Use levelOrderTraversal to maintaing all the elements of the same level in a same level and do it in such a way 
        #  that always rightmost is enetered 1st then the 1st element will always be the 1 that will be seen from the right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        levelQueue = deque()
        levelQueue.append(root)

        while len(levelQueue) > 0:
            itemsInCurrentLevel = len(levelQueue)

            for i in range(itemsInCurrentLevel):
                node = levelQueue.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    levelQueue.append(node.right)

                if node.left:
                    levelQueue.append(node.left)

        return result
                
