class Node:
    def __init__(self,data:int,next = None):
        self.data = data
        self.next:Node = next

class LinkStack:
    def __init__(self):
        self.top:Node = None
    def push(self,data:int):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top!=None:
            data:int = self.top.data
            self.top = self.top.next
            return data
    @property
    def show_top(self):
        if self.top:
            # print(self.top.data)
            return self.top.data
    @property
    def is_null(self):
        if self.top:
            return False
        else:
            return True
    def __repr__(self):
        list = []
        temp:Node = self.top
        while temp:
            list.append(str(temp.data))
            temp = temp.next
        return ",".join(list)

if __name__=="__main__":
    temp_stack = LinkStack()
    for k in range(100):
        temp_stack.push(k)
    temp_stack.pop()
    temp_stack.show_top()
    print(temp_stack)

