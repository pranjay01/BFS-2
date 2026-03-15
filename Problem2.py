#Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time -> On
# Space -> On

from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # get the elements at depth A usign elvel order traversal, if both elements at that level
        # but have different parents then they are cousins else not

        levelQueue = deque()

        levelQueue.append(root)
        foundCousingX = False
        foundCousingY = False
        while levelQueue:
            totalItemsInCurrentLevel = len(levelQueue)
            for i in range(totalItemsInCurrentLevel):
                node = levelQueue.popleft()

                # check for same parent
                if node.left and node.right:
                    vals = {node.left.val, node.right.val}
                    if x in vals and y in vals:
                        return False
                # check if found val then update the flag
                for child in filter(None, [node.left, node.right]):
                    foundCousingX =  child.val == x or foundCousingX
                    foundCousingY = child.val == y or foundCousingY
                    levelQueue.append(child)

            # if in the last level found both and reached here means sibling
            if foundCousingX and foundCousingY:
                return True
            # if in the last level found only 1 then not sibling
            if foundCousingX or foundCousingY:
                return False