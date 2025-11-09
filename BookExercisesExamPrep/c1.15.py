class Unique:
    def __init__(self, l):
        self._l = l

    def produce(self):
        n = len(self._l)
        for i in range(n):
            for j in range(i + 1, n):
                if self._l[i] == self._l[j]:
                    return False
                
        return True

print(Unique([1, 2, 2]).produce())