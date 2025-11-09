class Reverser:
    def __init__(self, seq):
        self.__seq = seq
        self.__n = len(self.__seq)
    
    def produce(self):
        array = []

        for i in range(self.__n):
            array.append(self.__seq[self.__n - i - 1])

        return array

#OR

    def produce_pythonic(self):
        return list(reversed(self.__seq))


obj = Reverser([1, 2, 3])
print(obj.produce())
print(obj.produce_pythonic())

