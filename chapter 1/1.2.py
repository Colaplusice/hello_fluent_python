#encoding=utf-8
from  math import hypot

#设计一个向量类
#hypot 返回欧氏距离

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pass

    #求欧式距离
    def __abs__(self):
        return hypot(self.x,self.y)
        pass
##打印对象
    def __repr__(self):
        return "Vector({},{})".format(self.x,self.y)
        pass
#  如果模是0，返回false
    def __bool__(self):
        return bool(abs(self))


    #两个向量相加
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)

    #两个向量相乘
    def __mul__(self, other):
        x=self.x*other.x
        y=self.y*other.y
        return Vector(x,y)
vector=Vector(2,5)

vector2=Vector(3,4)
print vector
v3=vector+vector2
print(v3)
print abs(vector)

