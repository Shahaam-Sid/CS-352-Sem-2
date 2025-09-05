from CreditCard import CreditCard

class ListCC:
    def __init__(self):
        self._list = []
        
        
    def add(self, credit_card):
        if not isinstance(credit_card, CreditCard):
            raise TypeError("ListCC Only Works with Credit Card Objects")
        
        self._list.append(credit_card)
        
    def __contains__(self, credit_card):
        if not isinstance(credit_card, CreditCard):
            raise TypeError("ListCC Only Works with Credit Card Objects")
        
        for card in self._list:
            if credit_card == card:
                return True
            
        return False
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if len(self._list) == 0 and index == -1:
            raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")
        
        if index < 0:
            if len(self._list) > -(index):
                return self._list[index]
            else:
                raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                return self._list[index]
            
            else:
                raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")

        
        
    def __str__(self):
        for card in self._list:
            print(card)
        
        return f""
            
    
    
a = CreditCard("Muhammad Shahaam Siddiqui", "Habib Bank", "2411 0001 6101", 1000)
b = CreditCard("Muhammad Hanzala Siddiqui", "UBL", "1001 1901 8765", 1000)
c = CreditCard("Muhammad Umer Farooq", "NBP", "1000 0900 0040 0007", 1000)


l = ListCC()

l.add(a)
l.add(b)
l.add(c)

print(l)