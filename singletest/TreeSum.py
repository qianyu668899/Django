
class TreeNode:
    def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    
    import copy
    list=[]
    l=[]
    def copylist(self, s):
        return self.copy.copy(s)

    def dfs(self, root, su):
        if root.left is None and root.right is None:
            self.list.append(root.val)
            print self.list
            if sum(self.list) == su:
				#print 'ok'
				nl=self.copylist(self.list)
				self.l.append(nl)
				#print self.l
				return
            else:
                return
        else:
            self.list.append(root.val)
            if root.left is not None:
                self.dfs(root.left, su)
                if self.list:
					self.list.pop()
					print self.list

            if root.right is not None:
                self.dfs(root.right, su)
                if self.list:
					self.list.pop()
					print self.list
            
        
    def pathSum(self, root, su):
        if root is None:
            return self.l
        elif root.left is None and root.right is None:
            self.list.append(root.val)
            if sum(self.list) == su:
                self.l.append(self.list)
            return self.l
        else:
            self.dfs(root, su)
            return self.l

if __name__=='__main__':
	t1=TreeNode(5)
	t2=TreeNode(4)
	t3=TreeNode(8)
	t4=TreeNode(11)
	t5=TreeNode(13)
	t6=TreeNode(4)
	t7=TreeNode(7)
	t8=TreeNode(2)
	t9=TreeNode(5)
	t10 = TreeNode(1)

	t1.left = t2
	t1.right = t3
	t2.left=t4
	t3.left=t5
	t3.right=t6
	t4.left=t7
	t4.right=t8
	t6.left=t9
	t6.right=t10

	sol = Solution()
	#print t1.val
	print sol.pathSum(t1, 22)