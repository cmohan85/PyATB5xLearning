from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self, balance, acc_no):
        self.__balance = balance
        self.acc_no = acc_no

class ICICI(BankAccount):
    def withdraw(self):
        print("Yes")
    @abstractmethod
    def loan(self):
        pass
    @staticmethod
    def call_customer_care():
        print("Calling")
