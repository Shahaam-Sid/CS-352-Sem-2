from CreditCard import CreditCard

class ListCC:
    """
    A Custom List Class made for CreditCard Objects
    """
    def __init__(self, wallet=None):
        """
        Initializes Class
        If Wallet is None Creates an Empty List
        If Wallet is Entered(Must be List containing CreditCard object Only)
            assigns it to the List
        Args:
            wallet (List): Defaults to None.
        """
        
        if not (isinstance(wallet, list)) and (wallet is not None):
            raise TypeError("ListCC must be A List or None")
        
        if wallet is None:
            self._list = []
        else:
            if any(not isinstance(x, CreditCard) for x in wallet):
                raise TypeError("ListCC Must Only Contain Credit Card Object")
            
            self._list = wallet[:]
        
    def display(self):
        """
        Displays Credit Cards
        """
        
        print("No. of Cards:", len(self))
        for card in self._list:
            print(card)
        
    def add(self, credit_card):
        """
        Creates a new index and adds Credit Card
        Args:
            credit_card (CreditCard)

        """

        if not isinstance(credit_card, CreditCard):
            raise TypeError("ListCC Only Works with Credit Card Objects")
        
        initial_lenght = len(self._list)
        final_lenght = initial_lenght + 1
        
        new_list = [None] * final_lenght
        
        for i in range(initial_lenght):
            new_list[i] = self._list[i]
            
        new_list[-1] = credit_card
        
        self._list = new_list
        
    def empty(self):
        """
        Empties the List
        """
        self._list = []
        
    def add_collection(self, collection):
        """
        Adds the entered List of Credit Cards to the
            end of the existing list

        Args:
            collection (List)
        """
        if not isinstance(collection, list):
            raise TypeError("Collection must be a List")
        if any(not isinstance(x, CreditCard) for x in collection):
            raise TypeError("Collection must contain Credit Card Objects")
        
        for i in collection:
            self.add(i)
            
    def index(self, id):
        """
        Returns the Index of The Given Account ID

        Args:
            id (str)

        Returns:
            int
        """
        if not isinstance(id, str):
            raise TypeError("Account ID must be a string")
        
        id = id.strip()
        
        if id is None or len(id) == 0:
            raise ValueError("Account ID must contain Numbers") 
                
        if id.isspace():
            raise ValueError("Account ID cannot be whitespaces")        
        
        if any(not x.isdecimal() for x in id.split()):
            raise ValueError("Account ID must only contain Numbers")
        
        for i in range(len(self._list)):
            if self._list[i].account_id == id:
                return i
            
        raise ValueError("ID Not Matched | Credit Card Not Found")
                
    def insert(self, index, credit_card):
        """
        Inserts the credit card to the
        given Index

        Args:
            index (int)
            credit_card (CreditCard)
        """
        
        if not isinstance(index, int):
            raise TypeError("Index must be an Integer Value")
        if not isinstance(credit_card, CreditCard):
            raise TypeError("Can only insert Credit Card object")
        
        n = len(self._list)
        
        if index < 0:
            index = n + index
        
        new_list = [None] * (n + 1)
        
        for i in range(n + 1):
            if i < index:
                new_list[i] = self._list[i]
            if i == index:
                new_list[i] = credit_card
            if i > index:
                new_list[i] = self._list[i - 1]
                
        self._list = new_list
        
    def pop(self, index):
        """
        Removes the CreditCard from the given Index and returns it

        Args:
            index (int)
        
        Returns:
            CreditCard
        """
        
        if not isinstance(index, int):
            raise ValueError("Index must be a Integer Value")
        
        credit_card = self._list[index]
        
        del self[index]
        
        return credit_card
                
    def remove(self, id):
        """
        Removes the Credit Card of the given Account ID

        Args:
            id (str)
        """

        index = self.index(id)
        
        del self[index]
                                   
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
        
    def __len__(self):
        lenght = 0
        for _ in self._list:
            lenght += 1
                
        return lenght
            
    def __reversed__(self):
        n = len(self._list)
        new_list = [None] * n
        for i in range(n):
            new_list[i] = self._list[n - 1 - i]
            
        self._list = new_list
            
    def __str__(self):
        return "[" + ", ".join(str(card) for card in self._list) + "]"