print("Hello World!")


class Sample:
    def __new__(cls, parameter):
        print("New param invoked ", parameter)
        return super().__new__(cls)

    def __init__(self, parameter):
        print("Init param invoked", parameter)


obj = Sample("Destinne")


class Streams:

    def __init__(self, class_number, class_name):
        self.class_number = class_number
        self.class_name = class_name

    def __str__(self):
        return f"%s, %s" % (self.class_name, self.class_number)


Classifications = Streams('4 EAST', '21')
print(Classifications)

"""Intricate Add Functions"""


class DictList:
    def __init__(self, *args):
        self.n = args

    def __add__(self, new):
        list_repr = list(self.n)

        if isinstance(new, DictList):  # for the add method to work, it must be an instance of the class
            list_repr.extend(new.n)
            return list_repr
        elif isinstance(new, dict):
            list_repr.append(new)
        else:
            raise TypeError("Must be an instance of the Class")

        return DictList(*list_repr)

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return "DictList" + repr(self.n)


Working_add = DictList(dict(a=1, b=2, c=3), dict(a=2, b=3, c=4))
print(Working_add)
Working_add.__add__(dict(a=3, b=4, c=5))
print(Working_add)


class School(Streams):

    def __init__(self, number_of_classes, class_number, class_name):
        super().__init__(class_number, class_name)

        self.number_of_classes = number_of_classes

    def __add__(self, other):
        if isinstance(other, School):
            return self.number_of_classes + other.number_of_classes

        raise Exception(f"{other} is not of class Account")


"""The generator function"""


class Gen:

    def __init__(self, rang):
        self.rang = rang

    def gen_func(self):
        for i in range(self.rang):
            yield i


first_gen = Gen(5)
first_gen1 = first_gen.gen_func()
print(first_gen1)

"""While loops"""


class FruityLoop:

    def __init__(self, maximum_count):
        self.maximum_count = maximum_count

    def the_math_behind_loops(self):
        count = 0
        while count < self.maximum_count:
            count += 1
            # this becomes the main stepwise counter
            print("Hello sIR!")
        print("-------------")

    def __repr__(self):
        return self.the_math_behind_loops()


f_o = FruityLoop(5)
f_o.the_math_behind_loops()
f_o.__repr__()
