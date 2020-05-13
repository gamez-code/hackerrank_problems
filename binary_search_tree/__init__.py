class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def findRigth(self, root):
        if root.right is not None:
            return 1 + self.findRigth(root.right)
        else:
            return 0

    def findLeft(self, root):
        if root.left is not None:
            return 1 + self.findLeft(root.left)
        else:
            return 0

    def finAllWay(self, root):
        acum = []
        if not root:
            return 0
        if root.left is not None and root.right is not None:
            acum.append(1 + self.findLeft(root.left) + self.findRigth(root.right))
        elif root.left is not None:
            acum.append(1 + self.findLeft(root.left))
        elif root.right is not None:
            acum.append(1 + self.findRigth(root.right))
        acum.append(1 + self.finAllWay(root.left))
        acum.append(1 + self.finAllWay(root.right))
        return max(acum)

    def getHeight(self, root):
        # Write your code here
        return self.finAllWay(root) - 1


with open('data.txt', 'r') as file:
    _data = file.read().split('\n')

T = int(_data[0])
myTree = Solution()
root = None
for i in range(T):
    data = int(_data[i + 1])
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
