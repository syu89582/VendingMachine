class VendingMachine():
    def __init__(self, items=[]):
        self.items = items
        self.coin = [100, 50, 10, 5, 1]
        self.payment = 0
    #    
    def show_items(self, price=999, showall=0):
        if showall == 1:
            print("No\tItem\tPrice\tAmount\t\n")
            for item in self.items:
                print('%s %10s %3d  %8s' % (item["itemID"], item["itemName"], item["price"], int(item["amount"]))
        else:
            print("No\tItem\tPrice\t\n")
            for item in self.items:
                if price >= int(item['price']) and int(item["amount"]) > 0:
                    print('%s %10s %s' % (item["itemID"], item["itemName"], item["price"]))

    #         
    
    def refund(self):
        refund_coin = {}
        for c in self.coin:
            while self.payment >= int(c):
                self.payment -= int(c)
                if refund_coin.get(c):
                    refund_coin[c] += 1
                else:
                    refund_coin[c] = 1
        self.payment = 0
        return refund_coin

    def insert_coin(self, coin):
        if coin in self.coin:
            self.payment += int(coin)
            return 1
        return 0

    def get_money(self):
        return self.payment

    def buy(self, itemID):
        for item in self.items:
            if item["itemID"] == itemID:
                if self.payment >= int(item["price"]):
                    int(item["amount"]) -= 1
                    self.payment -= int(item["price"])
                    return 1

        return 0

    def set_item(self, itemID, key, value):
        for item in self.items:
            if item["itemID"] == itemID:
                item[key] = value
                return 1
        return 0
