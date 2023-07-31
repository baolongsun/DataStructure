class Array:
    def __init__(self,data:int):
        self.data = data

class ArrayList:
    def __init__(self,cap:int):
        self.cap = cap
        self.len = 0
        self.array_map = {}

    def show_array_len(self):
        return self.len if self.len >= 0 else None

    def push(self,data):
        if self.len<self.cap:
            temp_data:Array = Array(data)
            self.array_map[self.len] = temp_data
            self.len += 1
        else:
            print("cap is not enough")

    def insert(self,data,index:int):
        if self.len<self.cap-1:
            temp_data = Array(data)
            self.array_map[self.len] = None
            self.len += 1
            for i in range(self.len,index,-1):
                self.array_map[i] = self.array_map[i-1]
            self.array_map[index] = temp_data
        else:
            print("cap is not enough")

    def delete(self,index:int):
        for i in range(index,self.len-1):
            self.array_map[i] = self.array_map[i+1]
        self.len -= 1

    def find(self,index:int):
        return self.array_map[index].data if index<self.len-1 else None

    def edit(self,data,index:int):
        if index <self.len:
           self.array_map[index].data = data

    def __repr__(self):
        list = [str(self.array_map[i].data) for i in range(self.len)]
        return ",".join(list)


if __name__ == "__main__":
    q = ArrayList(100)
    for k in range(10):
        q.push(k)
    print(q)
    q.edit(100,0)
    print(q)
    q.find(10)

