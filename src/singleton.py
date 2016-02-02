'''
Created on Feb 2, 2016

@author: bob@huashanpai.net
'''
# 
# __instances = {}
# def x(cls, *args, **kwarg):
#     print 'x'
#     def y(*args, **kwarg):
#         print 'y'
#         instance = cls(*args, **kwarg)
#         if not __instances.has_key(cls.__name__):
#             __instances[cls.__name__] = instance
#         return __instances.get(cls.__name__)
#     return y
# #@x #todo: this is the bug by this way
# class A(object):
#     def __init__(self, m):
#         self.m = m
# @x
# class B(A):
#     def __init__(self, x):
#         print type(B)
#         A.__init__(self, x)
#     def showm(self):
#         print self.m
# 
# i = B(9527)
# j = B(9527)
# print i,j,i==j

class Singleton(type):
    def __call__(self, *args, **kwargs):
#         print "Singleton call"
        if not hasattr(self, 'instance'):
            self.instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.instance
    def __new__(self, name, bases, properties):
#         print "Singleton new"
        return type.__new__(self, name, bases, properties)
    def __init__(self, name, bases, properties):
#         print "Singleton init"
        super(Singleton, self).__init__(name, bases, properties)
  
# def makesingleton(cls):
#     cls.__metaclass__ = Singleton #todo: can not modify CLASS/TYPE's __dict__ :(

if __name__ == '__main__':
    # @makesingleton
    class Example(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kwargs):
            print 'Example.__init__'
    #     def __new__(self, *args, **kwargs):
    #         print 'Example.__new__'
    #         return object.__new__(self, *args, **kwargs)
    #     def __call__(self, *args, **kwargs):
    #         print 'Example.__call__'
    # @makesingleton
    class ExampleEx(Example):
        __metaclass__ = Singleton
        def __init__(self, *args, **kwargs):
            print 'ExampleEx.__init__'
            Example.__init__(self, *args, **kwargs)
    #     def __new__(self, *args, **kwargs):
    #         print 'ExampleEx.__new__'
    #         return Example.__new__(self, *args, **kwargs)
    #     def __call__(self, *args, **kwargs):
    #         print 'ExampleEx.__call__'
    
    e_1 = Example()
    e_2 = Example()
    print e_1,e_2
    print e_1==e_2,e_1 is e_2
    
    ex_1 = ExampleEx()
    ex_2 = ExampleEx()
    print ex_1,ex_2
    print ex_1==ex_2,ex_1 is ex_2
