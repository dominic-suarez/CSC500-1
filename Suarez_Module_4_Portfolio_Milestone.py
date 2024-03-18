class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

def main():
    #Create two items.
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    #Prompt user for item 1 details.
    item1.item_name = input("Enter item 1: ")
    item1.item_price = float(input("Enter the item price: "))
    item1.item_quantity = int(input("Enter the item quantity: "))

    #Prompt user for item 2 details.
    item2.item_name = input("Enter item 2: ")
    item2.item_price = float(input("Enter the item price: "))
    item2.item_quantity = int(input("Enter the item quantity: "))

    #Calculate total cost.
    total_cost = item1.item_quantity * item1.item_price + item2.item_quantity * item2.item_price

    #Print item costs and total cost.
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost}")

if __name__ == "__main__":
    main()
