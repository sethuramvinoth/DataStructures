class CustomArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def getItem(self,index):
        return self.data[index]

    def pushItem(self,item):
        self.data[self.length] = item
        self.length+=1

    def popItem(self):
        del self.data[self.length-1]
        self.length-=1

    def delelteItem(self,index):
        del self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1

arr1 = CustomArray()
arr1.pushItem('hi')
arr1.pushItem('new')
arr1.pushItem('data')
arr1.pushItem('is')
arr1.pushItem('added')
arr1.pushItem('dummy')

arr1.popItem()
print('After Pop', arr1.data)

arr1.delelteItem(1)

print(arr1)