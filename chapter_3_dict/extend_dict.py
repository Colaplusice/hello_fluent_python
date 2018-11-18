# encoding=utf-8
import sys
class my_dict(dict):
    __name__='fjl2041的dict'
    __class__ ='fjl2401_class'

    def __getitem__(self, item):
        print('调用了getitem方法')
        return self[item]

    def __setitem__(self, key, value):
        print('调用了setitem方法')
        self[key]=value
        return

    def __missing__(self, key):
        print('{}不存在'.format(key))

    def __repr__(self):
        return 'fjl'

a_dict=my_dict()
a_dict['sd']=23
print  a_dict['sd']