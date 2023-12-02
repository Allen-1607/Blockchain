from Blockchain import Blockchain
from ngo_donations import NGO, Donator, Supplier

def showBalance(text,value):
    print(text,value)

def start():
    blockchain = Blockchain()
    supplierBlockchain = Blockchain()
    ngo = NGO(0)
    donator = Donator("Allen",100);
    donator2 = Donator("Sam",100);
    showBalance("NGO_balance",ngo.balance)
    print(donator.name)
    showBalance("Donator_balance",donator.balance)
    print(donator2.name)
    showBalance("Donator_balance",donator2.balance)
    ngo.deploy(blockchain);
    donator.donate(10,blockchain);
    donator2.donate(20,blockchain);
    print(donator.name)
    showBalance("Donator_balance",donator.balance)
    print(donator2.name)
    showBalance("Donator_balance",donator2.balance)
    ngo.add_donation(donator.name)
    ngo.encrypt_and_store_details(blockchain)
    ngo.receiveDonation()
    ngo.add_donation(donator2.name)
    ngo.encrypt_and_store_details(blockchain)
    ngo.receiveDonation()
    print(blockchain)
    showBalance("NGO_balance",ngo.balance)
   

    # supplier = Supplier("ABC",0);
    # print("Supplier Name:",supplier.name, "Balance",supplier.balance);
    # ngo.deploy1(supplierBlockchain);
    # ngo.order(10,blockchain)
    # ngo.add_order(supplier.name)
    # ngo.encrypt_and_store_details(supplierBlockchain)
    # ngo.placeOrder()
    # supplier.receiveOrder()
    # showBalance("NGO_balance",ngo.balance)
    # print("Supplier Name:",supplier.name, "Balance",supplier.balance);



if __name__ == '__main__':
    start()
    
