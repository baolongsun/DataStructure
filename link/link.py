class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Link:
    def __init__(self):
        self.head:Node = None

    def get_link_len(self):
        sum:int=0
        temp:Node = self.head
        if temp ==None:
            sum = 0
        else:
            while temp:
                sum += 1
                temp = temp.next
        return sum

    def go_to_index(self,k:int)->Node:
        final:int = self.get_link_len()
        temp:Node = self.head
        if not temp:
            return temp
        else:
            if 0<= k< final:
                for _ in range(k):
                    temp = temp.next
            elif final>k | final == -1:
                while temp.next:
                    temp = temp.next
            elif final<-1:
                pass
        return temp

    def push(self,data:int):
        new_node = Node(data)
        last_node = self.go_to_index(-1)
        if not self.head:
            self.head = new_node
        else:
            last_node.next = new_node

    def insert(self,data:int,index:int=-1):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            front_node = self.go_to_index(index-1)
            next_node = front_node.next
            front_node.next =  new_node
            new_node.next = next_node

    def delete(self,index:int):
        if index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                if self.head:
                    self.head = None
        else:
            front_node = self.go_to_index(index - 1)
            temp_node = front_node.next
            if temp_node == None:
                front_node.next=None
            else:
                front_node.next = temp_node.next

    def __repr__(self):
        list = []
        temp:Node = self.head
        while temp:
            list.append(temp.data)
            temp = temp.next
        return ",".join([str(i) for i in list])

if __name__ == "__main__":
    a = 2


