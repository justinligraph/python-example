
class Base(object):
    @classmethod
    def printName(cls):
        print cls.__name__


class Child(Base):
    pass


Base.printName()
Child.printName()
