class A:
    def __init__(self):
        self.a = 1
class B:
    def __init__(self):
        self.b = 1

class C(A,B):
    def __init__(self):
        self.c = 1
        print(super.mro())
        import pdb;pdb.set_trace()
        super().__init__()

c = C()