


class decorator:
    def __init__(self, cls, func):
        self.cls = cls
        self.function = func
    
    def __call__(self, *args, **kwargs):
        args, kwargs = self.convert(*args, **kwargs)
        result = self.function(self.cls, *args, **kwargs)
        return result

    def convert(self, *args, **kwargs):
        func_args = [i for i in self.function.__code__.co_varnames if i not in ('self')]
        annotions = self.function.__annotations__
        out_args = ()
        out_kwargs = {}
        index = 0
        for arg in args:
            if func_args[index] in annotions:
                try:
                    result = self.function.__annotations__[func_args[index]]
                    out_args = (*out_args, result().convert(arg))
                except Exception as e:
                    raise e
            index += 1
        for arg in kwargs:
            if arg[0] in annotions:
                try:
                    result = self.function.__annotations__[arg[0]]
                    kwargs[arg[0]] = result(arg[1])
                except Exception as e:
                    raise e
                
        return (out_args, out_kwargs)


class Cog:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        return self
    
    def __init__(self):
        
        # * Annotations auto decorator
        class_func_list = [i for i in type(self).__dict__ if not i.startswith('__')]
        for func_name in class_func_list:
            class_func = type(self).__dict__[func_name]
            setattr(self, func_name, decorator(self, class_func))
