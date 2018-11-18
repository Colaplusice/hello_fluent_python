# encoding=utf-8
import bobo

@bobo.query('/')

#对函数进行内省，发现需要参数person,从请求中自动获得person参数
def hello(person):
    return 'hello%s!'%person

