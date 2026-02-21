class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Data: {self.data}'

class BinarySearchTree:
    def __init__(self):
        self.root = None # BSTNode

    def add(self, data):
        new_node = BSTNode(data)

        if self.root is None:
            self.root = new_node
            return

        itr = self.root
        while itr:
            curr = itr.data
            if data < curr:
                if itr.left is None:
                    itr.left = new_node
                    return
                else:
                    itr = itr.left
            elif data > curr:
                if itr.right is None:
                    itr.right = new_node
                    return
                else:
                    itr = itr.right
            else:
                raise Exception('Cannot add duplicate data to BST!')

    def inorder(self):
        inorder = []

        def f(root):
            if root is None:
                return
            else:
                f(root.left)
                inorder.append(root.data)
                f(root.right)

        f(self.root)
        return inorder

    def preorder(self):
        preorder = []

        def f(root):
            if root is None:
                return
            else:
                preorder.append(root.data)
                f(root.left)
                f(root.right)

        f(self.root)
        return preorder

    def postorder(self):
        postorder = []

        def f(root):
            if root is None:
                return
            else:
                f(root.left)
                f(root.right)
                postorder.append(root.data)

        f(self.root)
        return postorder

    def levelorder(self):
        queue = []
        levelorder = []
        if self.root is None:
            return []

        queue.append(self.root)
        levelorder.append(self.root.data)

        while len(queue) > 0:
            front = queue[0]
            if front.left is not None:
                queue.append(front.left)
                levelorder.append(front.left.data)
            if front.right is not None:
                queue.append(front.right)
                levelorder.append(front.right.data)

            queue.pop(0)

        return levelorder

    def search(self, data):

        def search_helper(root):
            if root is None:
                return False
            else:
                if data < root.data:
                    return search_helper(root.left)
                elif data > root.data:
                    return search_helper(root.right)
                else:
                    return True

        return search_helper(self.root)

    def remove(self, data):

        def remove_helper(root):
            if root is None:
                raise Exception('Data not found in tree!')

            if data < root.data:
                root.left = remove_helper(root.left)
                return root
            elif data > root.data:
                root.right = remove_helper(root.right)
                return root
            else:
                # gotcha !
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    dummy = BSTNode(None)

                    successor = root.right

                    if successor.left is None:
                        dummy.right = successor.right
                    else:
                        parent = successor
                        successor = successor.left
                        while successor.left:
                            successor = successor.left
                            parent = parent.left

                        dummy.right = root.right
                        parent.left = successor.right

                    dummy.data = successor.data
                    dummy.left = root.left

                    return dummy

        self.root = remove_helper(self.root)

