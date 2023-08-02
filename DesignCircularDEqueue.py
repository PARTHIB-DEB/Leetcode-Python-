class MyCircularDeque:

    def __init__(self, k: int):
        self.__front = -1 # Its constant here also , just increment it to 0
        self.__end = -1
        self.__Queue = []
        self.__totalsize = k
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.__end=(self.__end+1)%self.__totalsize
            self.__Queue.insert(self.__front,value)
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.__end=(self.__end+1)%self.__totalsize
            self.__Queue.insert(self.__end,value)
            return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            data=self.__Queue[self.__front]
            self.__Queue.remove(data)
            return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.__end==self.__front:
            self.__end=0
        else:
            self.__end-=1
            data=self.__Queue[self.__end]
            self.__Queue.remove(data)
            return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.__Queue[self.__front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
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
    
    def display(self):
        print(f"\n\t\t\tCIRCULAR-DEQUEUE : {self.__Queue}")
        
Queue_Obj = MyCircularDeque(int(input("\n\t QUEUE SIZE:")))
while (True):
    print("\n")
    print("\t\tPRESS 1 OR 2")
    Queue_Obj.display()
    op = int(input("\n\tOPERATION:"))
    match op:
        case 1:
            print("\t\t \"ene\" TO INSERT FROM END \n\t\t \"def\" TO DELETE FROM FRONT")
            option=input("\n\t\tENQUEUE BY END or DEQUEUE BY FRONT??-->")
            if option == "ene":
                Queue_Obj.insertLast(input("\n\t\tENTER VALUE:"))
            elif option == "def":
                Queue_Obj.deleteFront()
            else:
                print("\n\t\tNO OPTIONS MATCHED")

        case 2:
            print("\t\t \"enf\" TO INSERT FROM FRONT \n\t\t \"dee\" TO DELETE FROM END")
            option=input("\n\t\tENQUEUE BY FRONT or DEQUEUE BY END??-->")
            if option == "enf":
                Queue_Obj.insertFront(input("\n\t\tENTER VALUE:"))
            elif option == "dee":
                Queue_Obj.deleteLast()
            else:
                print("\n\t\tNO OPTIONS MATCHED")


        case _:
            print("\n\n\t\tNO OPERATIONS MATCHED")
            break


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()