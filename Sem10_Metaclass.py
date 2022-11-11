class OneObgect(type):
    def __init__(self, *args, **kwargs):
        self.Second = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.Second is None:
            self.Second = super(OneObgect, self).__call__(*args, **kwargs)
            return self.Second
        else:
            return self.Second

class Myclass(metaclass=OneObgect):
    pass
obj_1 = Myclass()
obj_2 = Myclass()
obj_3 = Myclass()
obj_4 = Myclass()
print(obj_1 is obj_3) 
print(obj_3 is obj_1) 
print(obj_2 is obj_4) 
print(obj_1 is obj_2) 