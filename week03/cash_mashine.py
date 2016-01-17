class Bill():
    def __init__(self, bill):
        self.bill = bill

    def __str__(self):
        return "a {}$ bill".format(self.bill)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.bill

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.bill)


class BillBatch():
    def __init__(self, bills):
        self.bills = bills

    def __str__(self):
        return "a {}$ bill".format(self.bills)

    def __len__(self):
        return len(self.bills)

    #def __iter__(self):
        #return iter(self.bills)
    def __getitem__(self, item):
        return self.bills[item]

    def total(self):
        result = 0
        for bill in self.bills:
            result += int(bill)
        return result
        #return sum(int(bill) for bill in self.bills)


class CashDesk():
    def __init__(self):
        self.money_catch = {}

    def take_money(self, money):
        self.money = money
        try:
            for x in self.money:
                if x in self.money_catch:
                    self.money_catch[x] += 1
                else:
                    self.money_catch[x] = 1
        except:
            if self.money in self.money_catch:
                self.money_catch[self.money] += 1
            else:
                self.money_catch[self.money] = 1

    def total(self):
        result = 0
        for bill in self.money_catch:
            result += int(self.money_catch[bill]) * int(bill)
        return result

    def inspect(self):
        for bill in self.money_catch:
            print(str(bill) + " - ", self.money_catch[bill])