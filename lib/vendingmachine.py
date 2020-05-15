
class VendingMachine():
    def __init__(self, items=[]):
        self.items = items
        self.coin = [100, 50, 10, 5, 1]
        self.payment = 0

    def refund(self):
        refund_coin = {}
        for c in self.coin:
            while self.payment >= int(c):
                self.payment -= int(c)
                if refund_coin.get(c):
                    refund_coin[c] += 1
                else:
                    refund_coin[c] = 1

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
                if self.payment >= item["price"]:
                    item["amount"] -= 1
                    self.payment -= item["price"]
                    self.refund()
                    return 1

        return 0

    def set_item(self, itemID, key, value):
        for item in self.items:
            if item["itemID"] == itemID:
                item[key] = value
                return 1
        return 0
