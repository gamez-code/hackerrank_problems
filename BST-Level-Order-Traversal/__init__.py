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

    def levelOrder(self, root):
        queue = [root] if root else []

        while queue:
            node = queue.pop()
            print(node.data, end=" ")

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        # Write your code here


if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        _data = file.read().split('\n')
    T = int(_data[0])
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(_data[i + 1])
        root = myTree.insert(root, data)
    myTree.levelOrder(root)

    "25 12 39 9 19 31 55 23 35 41 60 70 90"
    "3 2 5 1 4 7"
