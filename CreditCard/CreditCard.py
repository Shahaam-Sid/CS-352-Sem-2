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