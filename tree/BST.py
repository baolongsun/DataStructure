from queue import Queue

class NodeTree:
    def __init__(self,data,left=None,right=None):
        self.data:int = data
        self.left:NodeTree = left
        self.right:NodeTree = right

#generate binary search tree:int

class BST:

    def __init__(self):
        self.root:NodeTree = None

    def push(self,data):
        def push_data(root:NodeTree,data):
            if root == None:
                root = NodeTree(data=data)
            else:
                if data<root.data:
                    root.left = push_data(root.left,data)
                else:
                    root.right = push_data(root.right,data)
            return root
        self.root = push_data(self.root,data=data)

    def find_max(self):
        if not self.root:
            print("empty tree")
        else:
            temp_root = self.root
            max_tree = temp_root.data
            while temp_root.right:
                temp_root = temp_root.right
                max_tree = temp_root.data
            print(f"maximum of tree is {max_tree}")

    def find_min(self):
        if not self.root:
            print("empty tree")
        else:
            temp_root = self.root
            min_tree = temp_root.data
            while temp_root.left:
                temp_root = temp_root.left
                min_tree = temp_root.data
            print(f"maximum of tree is {min_tree}")

    def search(self,data:int)->bool:
        def search_func(root:NodeTree,data):
            if root == None:
                return False
            if root.data == data:
                return True
            if data < root.data:
                return search_func(root.left,data)
            else:
                return search_func(root.right,data)
        return search_func(self.root,data)

    def find_height(self):
        def find_height_func(root:NodeTree):
            if root == None:
                return -1
            else:
                return max(find_height_func(root.left),find_height_func(root.right))+1
        return find_height_func(self.root)

    def level_order(self):
        def level_order_func(root:NodeTree):
            if root==None:
                pass
            queu = Queue()
            queu.put(root)
            while not queu.empty():
                current:NodeTree = queu.get()
                print(current.data,end=',')
                if current.left != None:
                    queu.put(current.left)
                if current.right != None:
                    queu.put(current.right)
        level_order_func(self.root)

    def first_order(self):
        def first_order_func(root:NodeTree):
            if root == None:
                pass
            else:
                print(root.data,end=",")
                first_order_func(root.left)
                first_order_func(root.right)
        first_order_func(self.root)

    def middle_order(self):
        def middle_order_func(root:NodeTree):
            if root == None:
                pass
            else:
                middle_order_func(root.left)
                print(root.data,end=",")
                middle_order_func(root.right)
        middle_order_func(self.root)

    def last_order(self):
        def last_order_func(root:NodeTree):
            if root == None:
                pass
            else:
                last_order_func(root.left)
                last_order_func(root.right)
                print(root.data,end=",")
        last_order_func(self.root)

if __name__ == "__main__":
    tree = BST()
    for i in range(100):
        tree.push(i)
    tree.find_max()
    tree.search(5)
    tree.level_order()



