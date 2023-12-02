from datetime import datetime

class SmartContract:
    idCounter = 1

    def __init__(self):
        self.id = SmartContract.idCounter
        SmartContract.idCounter += 1
        self.owner_balance = 0
        self.donation_details = DonationDetails
    
    def withdraw_earnings(self):
        return self.owner_balance
    
    def owner_deposit(self, ether):
        self.owner_balance += ether
    
    def add_donation_details(self, donation_details):
        self.donation_details = donation_details

    def get_donationValue(self):
        return self.donation_details.get_donationValue()
    
    def get_donation_details(self):
        return self.donation_details
    
class SupplierContract:
    idCounter = 1

    def __init__(self):
        self.id = SupplierContract.idCounter
        SupplierContract.idCounter += 1
        self.owner_balance1 = 0
        self.order_details = OrderDetails

    def owner_deposit(self, ether):
        self.owner_balance += ether
    
    def supplier_deposit(self,ether):
        self.owner_balance1 += ether

    def get_orderValue(self):
        return self.order_details.get_OrderValue()
    
    def get_Order_details(self):
        return self.order_details
    
    def add_order_details(self, order_details):
        self.order_details = order_details

class OrderDetails:
    def __init__(self, sender, orderValue):
        self.sender = sender
        self.orderValue = orderValue
    def get_OrderValue(self):
        return self.orderValue
    
    
class DonationDetails:
    def __init__(self, sender, donationValue):
        self.sender = sender
        self.donationValue = donationValue

    def get_donationValue(self):
        return self.donationValue
    