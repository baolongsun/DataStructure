class Array:
    def __init__(self,num:int):
        self.num = num
        self.data = []

    @property
    def _len(self):
        return len(self.data)

    @property
    def _get(self,index:int):
        if index<self.num:
            return self.data[index]
        else:
            return None

    def insert(self,data,index:int):
        if self._len < self.num-1:
            if index < self._len:
                self.data.append(0)
                for i in range(self._len-2,self.index,-1):
                     self.data[i+1] = self.data

        else:
            print("above the maximum of array!!!")
