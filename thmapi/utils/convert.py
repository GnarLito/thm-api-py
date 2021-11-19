
# import discord
# from typing import List





class _type_convertor:
    TYPES = ()
    def __init__(self, ctx, arg):
        if arg in self.TYPES:
            return arg
        else:
            print("sup")

class _vpn_types: # (_type_convertor):
    TYPES = ('machines', 'networks')
    
    def __call__(self, *args, **kwds):
        pass
        

class test:
    def test(self, t: _vpn_types):
        print(type(t))


# def convert(cls, args):
#     func_list = [i for i in cls.__dict__ if not i.startswith('__')]
#     for func in func_list:
#         anno_list = [i for i in func.__annotations__]
#         for anno in anno_list:
#             pass

m=test()
m.test("h")