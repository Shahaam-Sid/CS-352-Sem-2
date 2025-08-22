class NdVector:
    def __init__(self, d):
        if not isinstance(d, int):
            raise TypeError("Enter a Number")
        
        if d <= 0:
            raise ValueError("Number of Dimensions must be atleast 1")
            
        self._coords = [0] * d
        
    def __len__(self):
        """Returns Dimension of the Vector"""
        
        return len(self._coords)
    
    def __getitem__(self, j):
        """Returns the Value of the given Axis"""
        if j < -len(self) or j >= len(self):
            raise IndexError(f"Index {j} out of range for vector of dimension {len(self)}")
        
        return self._coords[j]
    
    def __setitem__(self, j, value):
        """Set the value of the given Axis"""
        if j < -len(self) or j >= len(self):
            raise IndexError(f"Index {j} out of range for vector of dimension {len(self)}")
        self._coords[j] = value

        
    def __add__(self, other):
        """Addition of two Vectors"""
        if len(self) != len(other):
            raise ValueError("Dimensions must be same")
        
        result = NdVector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        
        return result    
    def __sub__(self, other):
        """Subtraction of two Vectors"""
        
        if len(self) != len(other):
            raise ValueError("Dimensions must be same")
            
        result = NdVector((len(self)))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
            
        return result
    
    def __mul__(self, scalar):
        """Multiplication of the Vector with a Scalar  Value"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Must be mulitplied by a Scalar Number")
          
        result = NdVector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * scalar
            
        return result
        
    def __abs__(self):
        """Returns the Magnitude of the Vector"""
        result = 0
        for i in range(len(self)):
            result += self[i] ** 2
        
        return result ** 0.5
        
    def __eq__(self, other):
        """Check if two vectors are equal"""
        if not isinstance(other, NdVector):
            return False
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __ne__(self, other):
        """Check if two vectors are unequal"""
        return not self == other


    
    def __str__(self):
        """Returns a user-friendly string representation of the vector."""
        return f"<{str(self._coords)[1:-1]}>"

    
    def __repr__(self):
        """Returns the official string representation of the vector."""
        return f"NdVector({self._coords!r})"