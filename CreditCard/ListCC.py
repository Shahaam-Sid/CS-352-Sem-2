from CreditCard import CreditCard

class ListCC:
    def __init__(self):
        self._list = []
        
        
    def add(self, credit_card):
        if not isinstance(credit_card, CreditCard):
            raise TypeError("ListCC Only Works with Credit Card Objects")
        
        initial_lenght = len(self._list)
        final_lenght = initial_lenght + 1
        
        new_list = [None] * final_lenght
        
        for i in range(initial_lenght):
            new_list[i] = self._list[i]
            
        new_list[-1] = credit_card
        
        self._list = new_list
        
                                   
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
        
        if index < 0:
            if len(self._list) >= -(index):
                return self._list[index]
            else:
                raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                return self._list[index]
            
            else:
                raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")
            
    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not isinstance(value, CreditCard):
            raise TypeError("Value must be Credit Card Object")
        
        if index < 0:
            if len(self._list) >= -(index):
                self._list[index] = value
            else:
                raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                self._list[index] = value
            
            else:
                raise IndexError(f"Index Not Found ListCC Contains {len(self._list)} items")
            
    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
            
        if index < 0:
            index = len(self._list) + index
    
        if index < 0 or index >= len(self._list):
            raise IndexError(f"Index Not Found. ListCC Contains {len(self._list)} items")
            
        new_list = [None] * (len(self._list) - 1)
        j = 0
        for i in range(len(self._list)):
            if i == index:
                continue
            new_list[j] = self._list[i]
            j += 1
                
            
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
l[2] = CreditCard('Taimoor', 'JS Bank', '9999', 100000)

print(l)