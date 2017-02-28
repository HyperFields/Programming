class MyClass:
    """A simple example class"""
    i = 123

    def f(self):
        return 'hello world'


print MyClass.i
# MyClass.i = 10
print MyClass.i
x = MyClass()
print 'instance', x.i
print MyClass.f(x),x.f()
