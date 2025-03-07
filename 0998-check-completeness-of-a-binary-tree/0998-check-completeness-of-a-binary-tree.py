# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        traversal_queue = deque( [ root ] )
        prev_node = root 
        while traversal_queue: 
            cur_node = traversal_queue.popleft() 
            if cur_node: 
                if not prev_node:  
                    return False
                traversal_queue.append( cur_node.left )
                traversal_queue.append( cur_node.right )
            prev_node = cur_node 
        return True