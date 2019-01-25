from collections import deque
class Node():
    def __init__(self, x): 
        self.value = x 
        self.right = None
        self.left = None
    def __repr__(self):
        return str(self.value)
class BinaryTree(): 
    def __init__(self): 
        self.head = None 
        self.size = 0 
        self.level = 0
    def add(self,val):
        to_add = Node(val)
        self.size += 1
        
        if self.head is None: 
            self.head = to_add
            self.level = 1
            return 
        temp = self.head
        curr_level = 0
        while temp is not None:

            if temp.value > val:
                if temp.left is None: 
                    temp.left = to_add
                    break 
                temp = temp.left 
            else: 
                if temp.right is None: 
                    temp.right = to_add
                    break
                temp = temp.right
            curr_level += 1
        self.level = curr_level
    def __str__(self):
        q = deque()
        q.appendleft(self.head)
        ret = "Preorder traversal : \n"
        s = ""
        while len(q) > 0: 
            temp = q.pop()
            if temp is None: 
                s+= "None,"
                continue
            s+= str(temp.value)
            s+= ","
            q.appendleft(temp.left)
            q.appendleft(temp.right)
        ret += s
        ret += "\nInorder traversal\n"
        ret += self.inorder()
        ret += "\nPostorder traversal\n"
        ret += self.postorder()
        ret += "\nLevelorder traversal\n"
        ret += self.levelorder()
        ret += "\nLeftView traversal\n"
        ret += self.leftview()
        return ret
    def leftview(self):
        def levelorderfirstelement(head): 
            q = deque()
            q_next = deque()
            q.appendleft(head)
            ret = ""
            while len(q_next) > 0 or len(q) > 0:
                curr = q.pop()
                ret+= str(curr.value) + ","
                if curr.left is not None: 
                    q_next.appendleft(curr.left)
                if curr.right is not None: 
                    q_next.appendleft(curr.right)
                while len(q) > 0:
                    curr = q.pop() 
                    if curr is not None: 
                        if curr.left is not None: 
                            q_next.appendleft(curr.left)
                        if curr.right is not None: 
                            q_next.appendleft(curr.right)
                q = q_next.copy()
                q_next = deque()
            return ret      
        return levelorderfirstelement(self.head)          
    def levelorder(self):
        def levelorder_iter(head):
            q = deque()
            q_next = deque()
            q.appendleft(head)
            ret = ""
            curr = head
            while len(q_next) > 0 or len(q) > 0:
                while len(q) > 0:
                    curr = q.pop() 
                    if curr is not None: 
                        ret += str(curr.value) + ","
                        q_next.appendleft(curr.left)
                        q_next.appendleft(curr.right)
                    else: 
                        ret += "None,"
                q = q_next.copy()
                q_next = deque()
            return ret                 
        return levelorder_iter(self.head)

    def postorder(self):
        def postorder_recur(head):
            if head is None:
                return "None,"
            ret = postorder_recur(head.left)
            ret += postorder_recur(head.right)
            ret += str(head.value) + ","
            return ret
        def postorder_iter(head):
            q = []
            curr = head
            ret = ""
            while len(q) > 0 or curr is not None: 
                while curr is not None: 
                    q.append(curr.left)
                    curr = curr.left 
                curr = q.pop()
                while curr is not None: 
                    q.append(curr.right)
                    curr = curr.right
                if curr is not None: 
                    ret += str(curr.value) + ","
                else:
                    ret += "None,"
            return ret
        return postorder_recur(self.head)+"\n" + postorder_iter(self.head)
    def inorder(self):
        def inorder_recur(head):
            if head is None:
                return "None,"
            ret = inorder_recur(head.left)
            ret += str(head.value) + ","
            ret += inorder_recur(head.right)
            return ret
        def inorder_iter(head):
            q = []
            q.append(head)
            ret = ""
            curr = head
            while len(q) > 0 or curr is not None: 
                while curr is not None: 
                    q.append(curr.left)
                    curr = curr.left
                curr = q.pop()
                if curr is not None:
                    ret += str(curr.value)+","
                    q.append(curr.right)
                    curr = curr.right
                else: 
                    ret += "None,"
            return ret
        return inorder_recur(self.head) + "\n" + inorder_iter(self.head)
class BalancedBinaryTree(BinaryTree):
    def isbalanced(self):
        def height(head):
            if head is None: 
                return 0 
            return max(height(head.left),height(head.right)) + 1
        def recur(head):
            if head is None: 
                return True
            l = height(head.left)
            r = height(head.right)
            return (abs(l-r) <= 1 ) and recur(head.left) and recur(head.right)
        return recur(self.head)
class RBTree(BalancedBinaryTree):
    #Todo insert delete
    pass
class AVLTree(BalancedBinaryTree):
    #Todo difference in height
    pass

b = RBTree() 
b.add(5)
b.add(2)
b.add(4)
print(b.isbalanced())
print(b)