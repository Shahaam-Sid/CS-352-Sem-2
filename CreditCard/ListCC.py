from CreditCard import CreditCard

class Wallet:
    def __init__(self, wallet=None):
        if not (isinstance(wallet, list)) and (wallet is not None):
            raise TypeError("Wallet must be A List or None")
        
        if wallet is None:
            self._list = []
        else:
            if any(not isinstance(x, CreditCard) for x in wallet):
                raise TypeError("Wallet Must Only Contain Credit Card Object")
            
            self._list = wallet[:]
        
        
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
                
        self._list = new_list
            
    def __str__(self):
        for card in self._list:
            print(card)
        
        return f""