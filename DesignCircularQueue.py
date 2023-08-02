class MyCircularQueue:

    def __init__(self, k: int):
        self.__front = -1 # Its constant here also , just increment it to 0
        self.__end = -1
        self.__Queue = []
        self.__totalsize = k+1

    def enQueue(self, value: int) -> bool:
        if self.__end == -1 and self.__front==-1:
            self.__end = 0
            self.__front = 0
        if self.isFull():
            return False
        else:
            self.__Queue.insert(self.__end,value)
            self.__end=(self.__end+1)%self.__totalsize
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.__end==self.__front:
            self.__end=0
        else:
            data=self.__Queue[self.__front]
            self.__Queue.remove(data)
            self.__end=self.__end-1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return None
        else:
            return self.__Queue[self.__front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return None
        else:
            return self.__Queue[len(self.__Queue)-1]
        

    def isEmpty(self) -> bool:
        if len(self.__Queue)==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if (self.__end+1)%self.__totalsize == self.__front :
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()