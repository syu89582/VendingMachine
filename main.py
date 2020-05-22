import json
from lib.vendingmachine import VendingMachine


def main():
    with open('items.json', 'r') as f:
        items = json.load(f)

    vm = VendingMachine(items)
    while True:
        # show all items
        cmd = input("command:pay, buy, refund")
        print("sum", vm.get_money())

        if cmd == "pay":
            while True:
                print("coin type:1, 5, 10, 50, 100")
                print("quit:q")
                coin = input("coin:")
                if coin == "q":
                    break
                if not vm.insert_coin(int(coin)):
                    print("wrong coin type")
                print("sum:", vm.get_money())
        elif cmd == "buy":
            # show available items
            print("quit:q")
            itemID = input("itemID:")
            if itemID == "q":
                continue
            if not vm.buy(itemID):
                print("not enough money ")
        elif cmd == "refund":
            print(vm.refund())
        elif cmd == "admin":
            # show all items
            itemID = input("product itemID:")
            key = input("attribute of the product:")
            value = input("value of the attribute:")
            if vm.set_item(itemID, key, value):
                print("modify success")
            else:
                print("modify fail")
        else:
            pass


if __name__ == '__main__':
    main()
