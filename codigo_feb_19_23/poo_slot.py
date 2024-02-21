class Example:
    __slots__ = ("slot_0", "slot_1")

    def __init__(self):
        self.slot_0 = "zero"
        self.slot_1 = "one"


x1 = Example()
print(x1.slot_0)
print(x1.slot_1)
# No se puede modificar el objeto
# Y no soporta la propiedad __dict__
# x1.slot_2 = "two"
# print(x1.__dict__)
# print(x1.slot_2)
