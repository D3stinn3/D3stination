print("Hello World!")


class Sample:
    def __new__(cls, parameter):
        print("New param invoked ", parameter)
        return super().__new__(cls)

    def __init__(self, parameter):
        print("Init param invoked", parameter)


obj = Sample("Destinne")

