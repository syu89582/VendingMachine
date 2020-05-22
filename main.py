import json
from lib.vendingmachine import VendingMachine


def main():
    with open('items.json', 'r') as f:
        items = json.load(f)

    vm = VendingMachine(items)
    while True:
        # show all items
        vm.show_items(0)
        #
        cmd = input("command:pay, buy, refund\n")
        print("sum", vm.get_money())

        if cmd == "pay":
            while True:
                print("coin type:1, 5, 10, 50, 100\n")
                print("quit:q\n")
                coin = input("coin:")
                if coin == "q":
                    break

                if not vm.insert_coin(coin):
                    print("wrong coin type")
                print("sum:", vm.get_money())
        elif cmd == "buy":
            # show available items
            vm.show_items(vm.get_money())
            #
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
            vm.show_items(0)
            #
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
