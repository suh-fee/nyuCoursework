class ShoppingCart:
    def __init__(self, objects=[], cart={}):
        self.cart = cart
        self.cost = 0
        for i in self.cart:
            self.cost += self.cart[i].total_cost
        self.cost = 0
        for i in objects:
            self.add_item(i)

    def add_item(self, object):
        self.cart[object.name] = object
        amount = object.amount
        self.__init__([], self.cart)
        self.cost += round(object.total_cost, 2)

    def __repr__(self):
        string = '\nShopping Cart:\n===========\n\n'
        for i in self.cart:
            string += str(self.cart[i].amount) + ' ' + i + '(s) for $' + str(self.cart[i].total_cost) + ' after shipping.\n'
        string += 'Your total cost is: $' + str(self.cost)
        return string




class Item:
    def __init__(self, name, cost, shipping_amount, amount=1):
        self.name = name
        self.cost = round(cost, 2)
        self.amount = amount
        self.shipping_amount = shipping_amount
        self.total_cost = round(((self.cost * self.amount) + self.shipping_amount), 2)

    def __repr__(self):
        string = "You're purchasing " + str(self.amount) + " " + self.name + "(s) for $" + str(self.cost) + \
                 " each for a total cost of $" + str((self.cost * self.amount) + self.shipping_amount)
        return string

    def add_more(self):
        amount = int(input("How many more items would you like to purchase?: "))
        self.amount += amount
        self.total_cost += (amount * self.cost)
        print("You are now buying " + str(self.amount) + " " + self.name + "(s).")



def main():
    cart = ShoppingCart()
    objects = [Item('Dildo', 20.00, 2.99), Item('iPhone Charger', 8.50, 1.99), Item('Juul', 30.00, 4.99), Item('Mint Pods',
                20.00, 1.99), Item('Menthol Pods', 20.00, 1.99), Item('Mango Pods', 20.00, 1.99),
                Item('Shitty Champion Hoodie', 12.00, 2.99), Item("Your cousin's old Call of Duty", 5.00, 0)]
    print('Welcome to AliExpress! Please shop our wares:')
    while True:
        print('\nItems for sale:\n===============\n')
        print('1. Dildo for $20.00 ($3.99 shipping)\n2. iPhone Charger for $8.50 ($1.99 shipping)\n3. '
          'Juul for $20.00 ($4.99 shipping)\n4. Mint Pods for $20.00 ($1.99 shipping)\n5. Menthol Pods for $20.00 ($1.99 shipping)'
          '\n6. Mango Pods for $20.00 ($3.99 shipping)\n7. Shitty Champion Hoodie for $12.00 ($2.99 shipping)\n8. A copy of CoD4 from your cousin for $5.00 '
          '(FREE shipping!)\n')
        print("\na) Buy Item\nb) Show cart\nc) Increase amount of specific item in cart\nd) Delete item from cart"
              "\ne) Quit\n")
        inp1 = input('Please enter the letter of the action you wish to do: ')
        if inp1 == 'a':
            inp2 = int(input("Please enter the number of the item you wish to purchase: ")) - 1
            cart.add_item(objects[inp2])
            print('Added!')
        elif inp1 == 'b':
            print(cart)
        elif inp1 == 'c':
            print(cart)
            inp3 = input('\n\nWhich item would you like to increase? Please enter its name exactly: ')
            cart.cart[inp3].add_more()
        elif inp1 == 'd':
            print(cart)
            inp4 = input("\n\nWhich item would you like to delete? Please enter its name exactly:")
            del cart.cart[inp4]
        elif inp1 == 'e':
            break







main()
