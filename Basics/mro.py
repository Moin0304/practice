class A:
    def __init__(self):
        self.a = 10
        self.b = 20

class B:
    def __init__(self):
        self.a = 30
        self.b = 40

class C(A,B):
    def __init__(self):
        super().__init__()
        # self.a = 50
        # self.b = 60


    def print_attr(self):
        print(self.a,self.b)
        
        # print(super().b)
        # print(A().a)
        # print(B().a)
        # print(B().b)

d = C()
d.print_attr()

