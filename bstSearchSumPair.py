# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        for every node find counterpart 
        target - node.val  = counterpart 
        """
        seen_nodes=set()

        def bstsearch(root,k,curr_node):
            if root == None:
                return False
            curr = root
            while curr != None:
                if curr.val == k and curr_node != curr:
                    return True 
                elif curr.val < k:
                    curr = curr.right
                elif curr.val > k:
                    curr = curr.left
            return False
        q = []
        q.append([root,k])
        while len(q) > 0:
            node, target = q.pop() 
            if node.val not in seen_nodes:
                seen_nodes.add(node.val)
                if target-node.val != node.val and bstsearch(root,target-node.val,node):
                    return True
            if node.left != None:
                q.append([node.left,target])
            if node.right != None:
                q.append([node.right,target])
        return False
                    
            
            