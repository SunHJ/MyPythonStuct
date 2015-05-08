#encoding: utf-8
'''
Created on 2015年5月9日

@author: SunHongjian
'''
class PArray:
    def __init__(self, nSize, *defValue):
        if type(nSize) is not int or nSize < 0:
            raise "`nSize` must be a positive int value"
        
        self.__data = [0 for _i in range(nSize)]
        self.__size = nSize
        i = 0
        for v in defValue:
            if i < nSize: self.__data[i] = v
            else: break
            i += 1

    def Size(self):
        return self.__size
    
    def __getitem__(self, nIndex):
        if type(nIndex) is not int:
            raise "`nIndex` must be an int value"
        return self.__data[nIndex]
    
    def __setitem__(self, nIndex, value):
        if type(nIndex) is not int:
            raise "`nIndex` must be an int value"
        self.__data[nIndex] = value
    
    def __len__(self):
        return self.__size
    
    def __str__(self):
        return "< type:Array size:%d value:%s >" % (self.__size, str(self.__data))
        
        
if __name__ == "__main__":
    arr = PArray(10,2,3,4,5,6,7,8,9)
    print(arr)
#     print(arr.__data) # AttributeError: Array instance has no attribute '__data'
    arr[0] = 10
    arr[-1] = 12
#     arr[11] = 3 # IndexError: list assignment index out of range
    print(arr)
    print(len(arr))
    print(arr[3], arr[0])