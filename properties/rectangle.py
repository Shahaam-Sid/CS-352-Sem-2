#@property = Decorator used to define a method as a property (It can be accessed like an attribute)
#Benefit = Add additional logic when read, write or delete attributes
# Gives you getter, setter and deleter method


class Rectangle:
    def __init__(self, width, hieght):
        self._width = width
        self._hieght = hieght
    
    #Getter    
    @property
    def width(self):
        return f"{self._width:.2f} cm"
    
    @property
    def hieght(self):
        return f"{self._hieght:.2f} cm"
    
    
    #Setter
    @width.setter
    def width(self, newWidth):
        if newWidth > 0:
            self._width = newWidth
            
    @hieght.setter
    def hieght(self, newHieght):
        if newHieght > 0:
            self._hieght = newHieght

    #Deleter
    @width.deleter
    def width(self):
        del self._width
        print("Width Deleted")
        
    @hieght.deleter
    def hieght(self):
        del self._hieght
        print("Hieght Deleted")  
        
    
rect = Rectangle(2, 3)

#Getter
print(rect.hieght)
print(rect.width)

#Setter
rect.hieght = 4
rect.width = 6

print(rect.hieght)
print(rect.width)

#Deleter
del rect.width
del rect.hieght