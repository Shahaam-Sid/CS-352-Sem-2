class CustomRange:
    def __init__(self, start, stop = None, step = 1):
        if not all(isinstance(x, int) for x in (start, step)):
            raise TypeError('start and stop can only be Integer Values')
        if not isinstance(stop, (int, type(None))):
            raise TypeError('stop must be None(default) or an Integer Value')
        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop is None:
            self._start = 0
            self._stop = start
            self._step = step
        else:
            self._start = start
            self._stop = stop
            self._step = step
        
        if (self._start > self._stop and step > 0) or (self._start < self._stop and step < 0):
            raise ValueError("Invalid range")
            
        if self._start == self._stop:
            self._length = 0
        elif self._start > self._stop and step < 0:
            self._length = (self._start - self._stop + abs(step) - 1) // abs(step)
        else:
            self._length = (self._stop - self._start + step - 1) // step
            
        self._index = -1

    def __getitem__(self, index):
        
        if index < 0:
            index += len(self)
        if not (index >= 0 and index < len(self)):
            raise IndexError("Index out of range")

        return self._start + (index * self._step)

    def __iter__(self):
        self._iter_index = -1
        return self

    def __next__(self):
        if self._iter_index < len(self) - 1:
            self._iter_index += 1
            return self._start + (self._iter_index * self._step)
        else:
            raise StopIteration
                    
    def __len__(self):
        return self._length

    def __str__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"