from multiprocessing.dummy import Value


class CreditCard:
    def __init__ (self, name, bank_name, account_id, limit):
        
        self.name = name
        self.bank_name = bank_name
        self.account_id = account_id
        self.limit = limit
        self.balance = 0
        
    @property
    def name(self):
        return self._name
    
    @property
    def bank_name(self):
        return self._bank_name
    
    @property
    def account_id(self):
        return self._account_id
    
    @property
    def limit(self):
        return self._limit
    
    @property
    def balance(self):
        return self._balance
    
    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        value = value.strip()
        
        if value is None or len(value) == 0:
            raise ValueError("Name must contain Alphabet")
                     
        if value.isspace():
            raise ValueError("Name cannot be whitespaces")
        
        if any(not x.isalpha() for x in value.split()):
            raise ValueError("Name must only contain Alphabet")
    
        self._name = value
            
    @bank_name.setter
    def bank_name(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Bank name must be a string")
        
        value = value.strip()
        
        if value is None or len(value) == 0:
            raise ValueError("Bank name must contain Alphabet")  
                
        if value.isspace():
            raise ValueError("Bank name cannot be whitespaces")
        
        if value.isdigit():
            raise ValueError("Bank name must contain Alphabet")
        
        self._bank_name = value
        
    @account_id.setter
    def account_id(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Account ID must be a string")
        
        value = value.strip()
        
        if value is None or len(value) == 0:
            raise ValueError("Account ID must contain Numbers") 
                
        if value.isspace():
            raise ValueError("Account ID cannot be whitespaces")        
        
        if any(not x.isdecimal() for x in value.split()):
            raise ValueError("Account ID must only contain Numbers")
        
        
        self._account_id = value
        
    @limit.setter
    def limit(self, value):
        
        if not isinstance(value, int):
            raise TypeError("Limit must be an Integer")
        
        if value < 500:
            raise ValueError("Limit cannot be less then $500.00")
        
        self._limit = value
    
    @balance.setter
    def balance(self, value):
        self._balance = value
        
    def __str__(self):
        return f"""
------------------------Credit Card Details------------------------
Account Holder: Mr/Ms. {self.name}
BankName: {self.bank_name}
ID: {self.account_id}
Limit: ${self.limit}
Balance: ${self.balance}
-------------------------------------------------------------------
"""

    def __repr__(self):
        return f"CreditCard(name = '{self.name}', bank_name = '{self.bank_name}', account_id = '{self.account_id}', limit = '{self.limit}', balance = '{self.balance}')"
    
try:
    acc = CreditCard('Muhammad Shahaam Siddiqui', 'UBL Bank Limited', '1010 0101', 1000)
    print(acc)
    print(repr(acc))
    
except ValueError as e:
    print("Error:", e)
    
except TypeError as e:
    print("Error:", e)