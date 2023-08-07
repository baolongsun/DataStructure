import numpy as np

#以矩阵方式保存边权重
class UndirectedGraph:
    def __init__(self,*name):
        self.name = name
        self.name_vertix = {k:index for index,k in enumerate(self.name)}
        self.vertix_name = {index:k for index,k in enumerate(self.name)}
        self.max_point = len(self.name)-1
        self.edge = np.zeros((self.max_point,self.max_point))

    def change_weight(self,name_1:str,name_2:str,weight:int):
        index_1,index_2 = self.name_vertix[name_1],self.name_vertix[name_2]
        self.edge[index_1,index_2] = weight
        self.edge[index_2,index_1] = weight

    def show_connect(self,name:str):
        index = self.name_vertix[name]
        if index < self.max_point:
            for con_index,i in enumerate(self.edge[index]):
                if i != 0:
                    print(self.vertix_name[i])
    def is_connect(self,name_1:str,name_2:str):
        index_1,index_2 = self.name_vertix[name_1],self.name_vertix[name_2]
        if index_1<self.max_point-1 & index_2<self.max_point-1:
            return True if self.edge[index_1,index_2] !=0 else False


if __name__ == "__main__":
    a = UndirectedGraph("a","b","c","d","e","f","g")
    a.show_connect("a")
    b = 2