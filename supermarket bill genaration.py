from datetime import datetime

name = input("Enter Your Name:")

# lists of items
items_lists = '''
Rice    RS 20/kg
Sugar   Rs 30/kg
Salt    RS 20/kg
Oil     RS 80/litre
Panner  Rs 110/kg
Maggie  Rs 50/kg
Boost   Rs 90/each
Colgate Rs 85/each
'''

# declaration
print(items_lists)
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilists = []
qlist = []
plist = []

# rates for items
item_prices = {'rice': 20, 'sugar': 30, 'salt': 20, 'oil': 80, 'panner': 110, 'maggie': 50, 'boost': 90, 'colgate': 85}

option = int(input("For list of items press 1: "))
if option == 1:
    print(items_lists)

while True:
    inp1 = int(input("If you want to buy press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your item: ").lower()
        quantity = int(input("Enter quantity: "))
        if item in item_prices:
            price = quantity * item_prices[item]
            pricelist.append((item, quantity, price))
            totalprice += price
            ilists.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5) / 100
            finalamount = gst + totalprice
        else:
            print("Sorry, the item entered is not available.")
    else:
        print("You entered a wrong number.")

inp = input("Can I bill the items? Yes or No: ")
if inp.lower() == 'yes':
    print(25 * "=", "seetharama Supermarket", 25 * "=")
    print(28 * " ", "Wanaparthy")
    print("Name:", name, 30 * " ", "Date:", datetime.now())
    print(75 * "-")
    print("Sno", 8 * " ", 'Items', 8 * " ", 'Quantity', 3 * " ", 'Price')
    for i in range(len(pricelist)):
        print(i, 8 * ' ', ilists[i], 8 * ' ', qlist[i], 3 * ' ', plist[i])
        print(75 * "-")
    print(50 * " ", 'Total Price:', 'Rs', totalprice)
    print("GST Amount", 50 * " ", 'Rs', gst)
    print(75 * "-")
    print(50 * " ", 'Final Amount:', 'Rs', finalamount)
    print(75 * "-")
    print(50 * "-", "Thanks for visiting")
    print(75 * "-")
