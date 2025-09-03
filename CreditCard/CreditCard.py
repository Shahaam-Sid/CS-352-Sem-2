import re
from tkinter import NO


class CreditCard:
    def __init__ (self, customer, bank_name, account_id, limit):
        
        self.customer = customer
        self.bank_name = bank_name
        self.account_id = account_id
        self.limit = limit
        self.balance = 0
        
    @property
    def customer(self):
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
    
    @customer.setter
    def customer(self, value):

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
        
        if value < 0:
            raise ValueError("Limit must be a positive value")
        
        self._limit = value
    
    @balance.setter
    def balance(self, value):
        self._balance = value
        
    def get_customer(self):
        return self.customer
    
    def get_bank_name(self):
        return self.bank_name
    
    def get_account_id(self):
        return self.account_id
    
    def get_limit(self):
        return self.limit
    
    def get_balance(self):
        return self.balance
        
    def charge(self, price=None):
        if price is None:
            raise TypeError("Amount must be An Integer or Float Value")
        if not isinstance(price, (int, float)):
            raise TypeError("Amount must be An Integer or Float Value")
        if price <= 0:
            raise ValueError("Amount cannot be less then or equals to zero")
    
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True
        
    def make_payment(self, amount=None):
        if amount is None:
            raise TypeError("Amount must be An Integer or Float Value")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be An Integer or Float Value")
        if amount <= 0:
            raise ValueError("Amount cannot be less then or equals to zero")
        
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
        
    def __str__(self):
        return f"""
------------------------Credit Card Details------------------------
Account Holder: Mr/Ms. {self.customer}
BankName: {self.bank_name}
ID: {self.account_id}
Limit: ${self.limit}
Balance: ${self.balance}
-------------------------------------------------------------------
"""

    def __repr__(self):
        return f"CreditCard(customer = '{self.customer}', bank_name = '{self.bank_name}', account_id = '{self.account_id}', limit = '{self.limit}', balance = '{self.balance}')"