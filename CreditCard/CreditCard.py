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
            raise ValueError("Value must be a string")  
                
        if value.isspace():
            raise ValueError("Name cannot be whitespaces")
        
        temp = value.strip()
                
        if any(not x.isalpha() for x in temp.split()):
            raise ValueError("Name must only contain Alphabet")
    
        self._name = value
            
    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
        
    @account_id.setter
    def account_id(self, value):
        self._account_id = value
        
    @limit.setter
    def limit(self, value):
        self._limit = value
    
    @balance.setter
    def balance(self, value):
        self._balance = value
        
    def __str__(self):
        return f"Credit Card(Name: '{self.name}' Bank: '{self.bank_name}', ID: '{self.account_id}', Limit: '{self.limit}', Balance: '{self.balance}')"
    
    
try:
    acc = CreditCard('Test', 'Test Bank', '1010101', 1000)
    acc.name = "Muhammad Shahaam Siddiqui"
    print(acc)     
    
except ValueError as e:
    print("Error:", e)
    
except TypeError as e:
    print("Error", e)