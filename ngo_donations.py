from contract import SmartContract,DonationDetails, SupplierContract, OrderDetails

class NGO:
    def __init__(self,balance):
        self.contract = SmartContract
        self.supplierContract = SupplierContract
        self.balance = balance

    def deploy(self, blockchain):
        self.contract = SmartContract();
        blockchain.add_new_transaction(self.contract);
        
    
    def deploy1(self,blockchain):
        self.supplierContract = SupplierContract()
        blockchain.add_new_transaction(self.supplierContract);
    
    def encrypt_and_store_details(self, blockchain):
        blockchain.mine()

    def receiveDonation(self):
        self.balance+=self.contract.owner_balance;
        self.contract.owner_balance = 0;

    def add_donation(self,donorName):
        self.contract.add_donation_details(DonationDetails(donorName,self.contract.owner_balance))
    
    def add_order(self,supplierName):
        self.supplierContract.add_order_details(OrderDetails(supplierName,self.supplierContract.owner_balance1))
    
    def order(self,ether,blockchain):
        #  self.supplierContract = blockchain.get_unconfirmed_transactions()[0]
         self.supplierContract.supplier_deposit(ether)
         self.balance -= ether   
    
    def placeOrder(self):
        self.balance-= self.supplierContract.owner_balance1;

    
class Donator:
    def __init__(self,name,balance):
        self.contract = SmartContract
        self.balance = balance
        self.name = name
    def donate(self, ether, blockchain):
        self.contract = blockchain.get_unconfirmed_transactions()[0]
        self.contract.owner_deposit(ether)
        self.balance -= ether

class Supplier:
     def __init__(self,name,balance):
        self.contract = SupplierContract
        self.balance = balance
        self.name = name
     def receiveOrder(self):
        self.balance += self.contract.owner_balance1;
        self.contract.owner_balance1 = 0;
    
    