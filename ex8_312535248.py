import random

class CellPhone:
    def __init__(self, model, price, year):
        self.model=str(model)
        self.price=int(price)
        self.year=int(year)
        if not self.valicell():
            raise ValueError('Invalid CellPhone')
    def valicell(self):
        if type(self.model) is str and type(self.price) is int and type(self.year) is int:
            return True
        else:return False
    def get_price(self):
        return self.price
    def get_modle(self):
        return self.model
    def change_price(self, price):
        self.price=price
        if self.price<=0:
            raise ValueError
        else: self.price=price
    def __repr__(self):
        return str(self.model)+' '+ str(self.price)
    def discount(self, rate):
        self.rate=rate
        a=self.rate/float(100)
        return int(self.price-(self.price*a)+0.9)
    def __eq__(self, other):
        return self.price==other.price
    def __lt__(self, other):
        return self.price<other.price
    def __le__(self, other):
        return self.price<=other.price
    def __gt__(self, other):
        return self.price>other.price
    def __ge__(self, other):
        return self.price>=other.price

class Order:
    def __init__(self,phones):
        self.phones=phones
        self.id=random.randint(1,10000)
        if not self.valiorder():
            raise ValueError('Invalid Order')
    def valiorder(self):
        if type(self.phones) is list:
            return True
        else:
            return False
    def get_id(self):
        return self.id

class Client:
    def __init__(self, name, id_num):
        self.name=str(name)
        self.id_num=int(id_num)
        self.balance=0
        self.orders=Order([])
        if not self.valiclient():
            raise ValueError('Invalid Client')
    def valiclient(self):
            if type(self.name) is str and type(self.id_num) is int:
                return True
            else:return False
    def get_balance(self):
            return self.balance
    def add_money(self, amount):
        self.amount=amount
        self.balance=self.balance+self.amount
    def maximize(self, order, d=0):
        phon=order.phones
        pric=[]
        for cell in phon:
            pric.append(cell.discount(d))
        count=0
        money=self.balance
        for i in pric:
            if self.balance>=i:
                money=money-i
                count+=1
        return count
    def buy(self, order, d=0):
        if self.maximize(order,d)!=len(order.phones):
            return self.balance
        else:
            self.orders=order
            pri=0
            for i in order.phones:
                pri+=i.get_price()
            self.add_money(-pri)
            lst=[]
            for i in order.phones:
                if i not in lst:
                    lst.append(i)
            for i in lst:
                i.change_price(i.discount(d))
            return self.get_balance()

    def find_order(self, ord_num):
        if self.orders.id==ord_num:
            cell=[]
            for i in self.orders.phones:
                return [i.get_modle()]
        else:
            return None






